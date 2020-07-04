import pygame
import Images as image
import Music as music
import numpy as np
from Game import Game


def setIcon():
    icon = pygame.image.load('images/icon.png')
    icon = pygame.transform.scale(icon, (32, 32))
    surface = pygame.Surface(icon.get_size())
    surface.fill((0, 255, 0))
    surface.set_colorkey((0, 255, 0))
    surface.blit(icon, (0, 0))
    return surface


class Application:
    def __init__(self):
        # game loading
        self.disp = pygame.display
        self.window = self.disp.set_mode((1138, 640))
        self.disp.set_caption("Ubongo")
        self.disp.set_icon(setIcon())
        music.loadMenuMusic()
        self.game = Game()

        # game management
        self.program_running = True
        self.phase = -1
        self.paused_phase = -1
        self.hints_hidden = 1
        self.current_turn = 0
        self.col = 0
        self.making_puzzle = False
        self.tp_mouse = False
        self.selected_piece = None
        self.selected_piece_id = 0
        self.turn_queue = -1
        self.puzzle = np.copy(self.game.getPuzzles(0))
        self.puzzle_ai = np.full((3, 6, 6), -1, dtype=int)
        self.completed_puzzle = False

        # mouse hovering
        self.play_hover = False
        self.instructions_hover = False
        self.config_hover = False
        self.exit_hover = False
        self.return_hover = False
        self.space_hover = False
        self.begin_turn_hover = False
        self.hints_hover = False
        self.piece_hover = np.array([False, False, False, False])
        self.blocked_piece = np.array([False, False, False, False])
        self.new_game_hover = False
        self.back_menu_hover = False
        self.minus_time_hover = False
        self.plus_time_hover = False
        self.minus_turns_hover = False
        self.plus_turns_hover = False
        self.minus_cpu_hover = False
        self.plus_cpu_hover = False

    def Run(self):
        while self.program_running:
            # window management
            image.gameBackground(self.window, 0, 0)
            if self.game.Window() == 0:
                self.runMenu()
            elif self.game.Window() == 1:
                self.runGame()
            elif self.game.Window() == 2:
                self.runInstructions()
            elif self.game.Window() == 3:
                self.runConfig()
            self.disp.update()

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.program_running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                        if 0 <= self.phase <= 3:
                            self.paused_phase = self.phase
                            self.phase = 4
                            music.loadMenuMusic()
                        elif self.phase == 4:
                            self.phase = self.paused_phase
                            music.loadGameMusic()
                    elif event.key == pygame.K_t:
                        if self.phase == 2 and not self.completed_puzzle:
                            self.making_puzzle = False
                            self.puzzle = np.copy(self.game.getPuzzles(0))
                            self.blocked_piece[:] = False
                    elif self.making_puzzle:
                        if event.key == pygame.K_w or event.key == pygame.K_s or \
                                event.key == pygame.K_a or event.key == pygame.K_d:
                            if event.key == pygame.K_w:
                                self.selected_piece = np.flipud(self.selected_piece)
                            elif event.key == pygame.K_s:
                                self.selected_piece = np.fliplr(self.selected_piece)
                            elif event.key == pygame.K_a:
                                self.selected_piece = np.rot90(self.selected_piece, 1, (0, 1))
                            elif event.key == pygame.K_d:
                                self.selected_piece = np.rot90(self.selected_piece, 3, (0, 1))
                            self.fixMousePos()

                elif event.type == pygame.MOUSEBUTTONUP:
                    # if menu screen
                    if self.game.Window() == 0:
                        if self.play_hover:
                            self.loadGame()
                            self.play_hover = False
                            music.loadGameMusic()
                        elif self.instructions_hover:
                            self.game.gotoInstructions()
                            self.instructions_hover = False
                        elif self.config_hover:
                            self.game.gotoConfig()
                            self.config_hover = False
                        elif self.exit_hover:
                            self.program_running = False
                            break
                        elif self.return_hover:
                            self.game.gotoGame()
                            self.phase = 4
                            self.return_hover = False
                            music.loadMenuMusic()

                    # if game screen
                    elif self.game.Window() == 1:
                        if self.space_hover:
                            self.game.player_human.pos = self.col
                            self.game.player_human.turn_place = 10
                            if self.phase > 0:
                                self.game.chooseRow()
                                self.game.updatePlaces()
                                self.current_turn += 1
                                if self.game.turn < self.game.set_turn:
                                    self.game.refreshPuzzles()
                                    self.puzzle = np.copy(self.game.getPuzzles(0))
                            else:
                                for i in range(self.game.nPlayers() - 1):
                                    self.game.player_ai[i].generateInitialPos()
                                    self.phase = 1
                            if self.game.turn < self.game.set_turn:
                                self.game.throwDice()
                                for i in range(3):
                                    if self.game.player_ai[i].playing:
                                        self.puzzle_ai[i] = np.copy(self.game.getPuzzles(i + 1))
                                        self.game.getSol(i + 1, i)
                                self.space_hover = False
                                break
                        if self.begin_turn_hover:
                            self.game.startTimer()
                            self.game.setAiPieceTimes()
                            self.phase = 2
                            self.game.player_human.turn_place = -1
                            for i in range(3):
                                if self.game.player_ai[i].playing:
                                    self.game.player_ai[i].turn_place = -1
                            self.turn_queue = 0
                            break
                        if self.making_puzzle:
                            self.Combine()
                            break
                        if self.hints_hover:
                            self.hints_hidden *= -1
                            self.hints_hover = False
                        if self.new_game_hover:
                            self.loadGame()
                            self.new_game_hover = False
                            music.loadGameMusic()
                            break
                        if self.back_menu_hover:
                            self.game.gotoMenu()
                            self.back_menu_hover = False
                            music.loadMenuMusic()
                            if self.phase == 4:
                                self.phase = 6
                            break
                        for i in range(4):
                            if self.piece_hover[i]:
                                pygame.mouse.set_pos(92, 138)
                                self.tp_mouse = True
                                self.making_puzzle = True
                                self.selected_piece = np.copy(self.game.getPiece(self.game.getPieces(0)[i]))
                                self.selected_piece_id = i
                                self.piece_hover[i] = False
                                break

                    # if instructions screen
                    elif self.game.Window() == 2:
                        if self.back_menu_hover:
                            self.game.gotoMenu()
                            self.back_menu_hover = False

                    # if config screen
                    elif self.game.Window() == 3:
                        if self.minus_cpu_hover or self.plus_cpu_hover or self.minus_turns_hover or \
                                self.plus_turns_hover or self.minus_time_hover or self.plus_time_hover:
                            self.phase = 0

                        if self.minus_cpu_hover or self.plus_cpu_hover:
                            self.changeUsers()
                            self.minus_cpu_hover = self.plus_cpu_hover = False
                        elif self.minus_turns_hover or self.plus_turns_hover:
                            self.changeTurns()
                            self.minus_turns_hover = self.plus_turns_hover = False
                        elif self.minus_time_hover or self.plus_time_hover:
                            self.changeTime()
                            self.minus_time_hover = self.plus_time_hover = False
                        elif self.back_menu_hover:
                            self.game.gotoMenu()
                            self.back_menu_hover = False

    def loadGame(self):
        self.game.startGame()
        self.puzzle = np.copy(self.game.getPuzzles(0))
        self.phase = 0

    def runMenu(self):
        image.gameMenu(self.window, 0, 0)
        if self.phase == 6:
            image.Return(self.window, 760, 277)
        self.mouseHovering()

    def runGame(self):
        # shows in all game phases except pause
        if self.phase != 4:
            image.gamePlayArea(self.window, 0, 0)
            image.Dice(self.window, 464, 506, self.game.dice + 1)
            image.Number(self.window, 727, 473, self.game.turn)
            self.showUserCards()
            self.showUserGems()
            self.showUserPlaces()
            self.showGems()
            self.showTimer()
            if self.hints_hidden == 1:
                image.hintsHidden(self.window, 330, 198)
            else:
                image.Hints(self.window, 330, 90)

        # game phase 0 (choose starting place)
        if self.phase == 0:
            for i in range(6):
                for j in range(3):
                    image.arrowDown(self.window, 476 + 34 * i, 336 + 12 * j)
                    image.arrowUp(self.window, 476 + 34 * i, 404 + 12 * j)

        # game phase 1 (rolling dice)
        if self.phase == 1:
            image.beginTurn(self.window, 538, 506, 1)
            self.showUnknownPieces()
            if self.game.turn == 1:
                for i in range(3):
                    for j in range(3):
                        image.arrowLeft(self.window, 676 + 12 * i, 515 + 16 * j)
            image.Dice(self.window, 464, 506, np.random.randint(1, 7))
        elif self.phase != 4:
            image.beginTurn(self.window, 538, 506, 2)

        # game phase 2 (making puzzle)
        if self.phase == 2:
            self.aiTurn()
            self.game.time -= 1
            if self.game.turn == 1 and self.game.time >= 966:
                for i in range(4):
                    for j in range(3):
                        image.arrowDown(self.window, 198 + 32 * i, 98 + 12 * j)
                        image.arrowUp(self.window, 198 + 32 * i, 166 + 12 * j)
                for i in range(3):
                    image.arrowLeft(self.window, 281 + 12 * i, 310)
                    image.arrowRight(self.window, 88 + 12 * i, 310)

            if self.completed_puzzle:
                while self.game.time > 0:
                    self.aiTurn()
                    self.game.time -= 1

            if self.game.time == 0:
                self.phase = 3
                self.completed_puzzle = False
                self.blocked_piece[:] = False
                self.current_turn = 0
                self.making_puzzle = False
                for i in range(3):
                    if self.game.player_ai[i].turn_place == -1:
                        self.game.player_ai[i].turn_place = self.turn_queue
                        self.turn_queue += 1
                if self.game.player_human.turn_place == -1:
                    self.game.player_human.turn_place = self.turn_queue
                    self.turn_queue += 1

        # game phase 3 (choosing gem row)
        if self.phase == 3:
            for i in range(3):
                if self.game.player_ai[i].playing:
                    if self.game.player_ai[i].turn_place == self.current_turn:
                        self.game.player_ai[i].chooseRow(self.game.table)
                        self.game.updatePlaces()
                        self.game.player_ai[i].turn_place = 10
                        self.current_turn += 1
            if self.current_turn == self.game.nPlayers():
                if self.game.turn < self.game.set_turn:
                    self.phase = 1
                    self.game.turn += 1
                else:
                    self.game.updatePlaces()
                    self.game.getWinner()
                    self.phase = 5
                    music.loadCheersMusic()

        # game phase 4 (pause)
        if self.phase == 4:
            image.gamePause(self.window, 438, 86)

        # game phase 5 (win screen)
        if self.phase == 5:
            image.gameWin(self.window, 438, 86)
            image.Winner(self.window, 532, 126, self.game.winner)

        # after rolling the dice
        if self.phase == 2 or self.phase == 3 or self.phase == 5:
            self.showPieces()

        # handles mouse hovering
        self.mouseHovering()

        # after choosing initial position
        if self.phase > 0 and self.phase != 4:
            self.showUsers()
            self.showPuzzles()
            if self.space_hover and self.col == self.game.player_human.pos:
                image.selectedShadow(self.window, 474 + 34 * self.col, 394)

        if self.tp_mouse:
            self.tp_mouse = False
        elif self.making_puzzle and self.phase == 2:
            self.makingPuzzle()

    def runInstructions(self):
        image.gameInstructions(self.window, 0, 0)
        self.mouseHovering()

    def runConfig(self):
        image.gameConfig(self.window, 0, 0)
        image.Number(self.window, 560, 292, int((self.game.set_time / 1000) * 6))
        image.Number(self.window, 572, 292, int((self.game.set_time / 1000) * 60) % 10)
        image.Number(self.window, 566, 348, self.game.set_turn)
        image.Number(self.window, 566, 410, self.game.nPlayers() - 1)
        self.mouseHovering()

    def mouseHovering(self):
        # get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # handle if menu screen
        if self.game.Window() == 0:
            self.back_menu_hover = False

            if 492 <= mouse_x <= 654 and 264 <= mouse_y <= 330:
                image.selectedPlay(self.window, 488, 264)
                self.play_hover = True
            else:
                self.play_hover = False

                if 507 <= mouse_x <= 636 and 346 <= mouse_y <= 379:
                    image.selectedInstructions(self.window, 503, 346)
                    self.instructions_hover = True
                else:
                    self.instructions_hover = False

                    if 643 <= mouse_x <= 662 and 357 <= mouse_y <= 376:
                        image.selectedConfig(self.window, 641, 355)
                        self.config_hover = True
                    else:
                        self.config_hover = False

                        if 539 <= mouse_x <= 604 and 401 <= mouse_y <= 438:
                            image.selectedExit(self.window, 535, 397)
                            self.exit_hover = True
                        else:
                            self.exit_hover = False

                            if self.phase == 6 and 760 <= mouse_x <= 861 and 277 <= mouse_y <= 348:
                                image.selectedReturn(self.window, 756, 273)
                                self.return_hover = True
                            else:
                                self.return_hover = False

        else:
            self.play_hover = False
            self.instructions_hover = False
            self.config_hover = False
            self.exit_hover = False
            self.return_hover = False

        # handle if game screen
        if self.game.Window() == 1:
            if 370 <= mouse_y <= 399:
                if self.phase == 0 and 466 <= mouse_x <= 669:
                    self.col = int((mouse_x - 466) / 34)
                    image.selectedSpace(self.window, 466 + 34 * self.col, 370)
                    self.space_hover = True
                else:
                    self.space_hover = False

                    if self.phase == 3 and self.game.playerTurnPlace() == self.current_turn:
                        mini = max(0, self.game.player_human.pos - (self.game.nPlayers() - self.game.playerTurnPlace()))
                        maxi = min(5, self.game.player_human.pos + (self.game.nPlayers() - self.game.playerTurnPlace()))
                        for i in range(mini, maxi + 1):
                            if 466 + 34 * i < mouse_x <= 466 + 34 * (i + 1):
                                self.col = i
                                image.selectedSpace(self.window, 466 + 34 * i, 370)
                                self.space_hover = True
                                break
                            else:
                                self.space_hover = False
            else:
                self.space_hover = False

                if self.phase == 1 and 538 <= mouse_x <= 671 and 506 <= mouse_y <= 569:
                    image.selectedBeginTurn(self.window, 534, 502)
                    self.begin_turn_hover = True
                else:
                    self.begin_turn_hover = False

                    if self.phase == 2 and 194 <= mouse_x <= 311 and 136 <= mouse_y <= 161:
                        selected = int((mouse_x - 194) / 32)
                        if (194 <= mouse_x <= 215 or 226 <= mouse_x <= 247 or
                            258 <= mouse_x <= 279 or 290 <= mouse_x <= 311) and not self.blocked_piece[selected]:
                            image.selectedPiece(self.window, 190 + 32 * selected, 132)
                            self.piece_hover[selected] = True
                        else:
                            self.piece_hover[selected] = False
                    else:
                        self.piece_hover[:] = False

                        if (self.phase == 4 or self.phase == 5) and 508 <= mouse_x <= 631 and 228 <= mouse_y <= 245:
                            image.arrowRight(self.window, 491, 228)
                            self.new_game_hover = True
                        else:
                            self.new_game_hover = False

                            if (self.phase == 4 or self.phase == 5) and 508 <= mouse_x <= 631 and 252 <= mouse_y <= 267:
                                image.arrowRight(self.window, 491, 252)
                                self.back_menu_hover = True
                            else:
                                self.back_menu_hover = False

                                if self.phase < 4 and ((330 <= mouse_x <= 423 and 198 <= mouse_y <= 227) or
                                                       (336 <= mouse_x <= 413 and 208 <= mouse_y <= 221)):
                                    if self.hints_hidden == 1:
                                        image.selectedArrowRight(self.window, 400, 204)
                                    else:
                                        image.selectedArrowLeft(self.window, 334, 206)
                                    self.hints_hover = True
                                else:
                                    self.hints_hover = False
        else:
            self.space_hover = False
            self.begin_turn_hover = False
            self.piece_hover[:] = False
            self.new_game_hover = False

        # handles if instructions screen
        if self.game.Window() == 2:
            if 153 <= mouse_x <= 238 and 553 <= mouse_y <= 584:
                image.selectedBack(self.window, 155, 555)
                self.back_menu_hover = True
            else:
                self.back_menu_hover = False

        # handles if config screen
        if self.game.Window() == 3:
            if 410 <= mouse_y <= 423:
                if 550 <= mouse_x <= 559:
                    image.selectedArrowLeft(self.window, 548, 408)
                    self.minus_cpu_hover = True
                else:
                    self.minus_cpu_hover = False

                    if 582 <= mouse_x <= 591:
                        image.selectedArrowRight(self.window, 580, 408)
                        self.plus_cpu_hover = True
                    else:
                        self.plus_cpu_hover = False
            else:
                self.minus_cpu_hover = False
                self.plus_cpu_hover = False

                if 348 <= mouse_y <= 360:
                    if 550 <= mouse_x <= 559:
                        image.selectedArrowLeft(self.window, 548, 346)
                        self.minus_turns_hover = True
                    else:
                        self.minus_turns_hover = False

                        if 582 <= mouse_x <= 591:
                            image.selectedArrowRight(self.window, 580, 346)
                            self.plus_turns_hover = True
                        else:
                            self.plus_turns_hover = False
                else:
                    self.minus_turns_hover = False
                    self.plus_turns_hover = False

                    if 292 <= mouse_y <= 305:
                        if 544 <= mouse_x <= 553:
                            image.selectedArrowLeft(self.window, 542, 290)
                            self.minus_time_hover = True
                        else:
                            self.minus_time_hover = False

                            if 588 <= mouse_x <= 597:
                                image.selectedArrowRight(self.window, 586, 290)
                                self.plus_time_hover = True
                            else:
                                self.plus_time_hover = False
                    else:
                        self.minus_time_hover = False
                        self.plus_time_hover = False

                        if 424 <= mouse_x <= 495 and 426 <= mouse_y <= 439:
                            image.selectedArrowLeft(self.window, 422, 424)
                            self.back_menu_hover = True
                        else:
                            self.back_menu_hover = False
        else:
            self.minus_time_hover = False
            self.plus_time_hover = False
            self.minus_turns_hover = False
            self.plus_turns_hover = False
            self.minus_cpu_hover = False
            self.plus_cpu_hover = False

    def changeUsers(self):
        if self.minus_cpu_hover and self.game.table.n_players > 2:
            self.game.table.n_players -= 1
            self.game.player_ai[self.game.table.n_players - 1].playing = False
        elif self.plus_cpu_hover and self.game.table.n_players < 4:
            self.game.player_ai[self.game.table.n_players - 1].playing = True
            self.game.table.n_players += 1

    def changeTurns(self):
        if self.minus_turns_hover and self.game.set_turn > 1:
            self.game.set_turn -= 1
        elif self.plus_turns_hover and self.game.set_turn < 9:
            self.game.set_turn += 1

    def changeTime(self):
        if self.minus_time_hover and self.game.set_time > 336:
            self.game.set_time -= 83
        elif self.plus_time_hover and self.game.set_time < 1000:
            self.game.set_time += 83

    def showUserCards(self):
        image.Card(self.window, 68, 68)
        image.userPlayer(self.window, 94, 92)
        image.bannerPlayer(self.window, 128, 84)

        if self.game.isAIPlaying(0):
            image.Card(self.window, 806, 64)
            image.userCPU(self.window, 832, 88, 1)
            image.bannerCPU(self.window, 866, 80)
        else:
            image.cardNone(self.window, 806, 64)

        if self.game.isAIPlaying(1):
            image.Card(self.window, 68, 380)
            image.userCPU(self.window, 94, 404, 2)
            image.bannerCPU(self.window, 128, 396)
        else:
            image.cardNone(self.window, 68, 380)

        if self.game.isAIPlaying(2):
            image.Card(self.window, 806, 376)
            image.userCPU(self.window, 832, 400, 3)
            image.bannerCPU(self.window, 866, 392)
        else:
            image.cardNone(self.window, 806, 376)

    def showGems(self):
        for i in range(12):
            for j in range(6):
                image.Gem(self.window, 470 + 34 * j, 338 - 30 * i, self.game.table.gems_pos[i, j])

    def showUsers(self):
        image.userPlayer(self.window, 474 + 34 * self.game.player_human.pos, 374)
        image.Shadow(self.window, 474 + 34 * self.game.player_human.pos, 394)

        for i in range(3):
            if self.game.player_ai[i].playing:
                image.userCPU(self.window, 474 + 34 * self.game.player_ai[i].pos, 374 + 30 * (i + 1), i + 1)
                image.Shadow(self.window, 474 + 34 * self.game.player_ai[i].pos, 394 + 30 * (i + 1))

    def showUserGems(self):
        for i in range(4):
            image.Number(self.window, 194 + 32 * i, 208, int(self.game.player_human.gems[i] / 10))
            image.Number(self.window, 206 + 32 * i, 208, self.game.player_human.gems[i] % 10)

        if self.game.isAIPlaying(0):
            for i in range(4):
                image.Number(self.window, 932 + 32 * i, 204, int(self.game.player_ai[0].gems[i] / 10))
                image.Number(self.window, 944 + 32 * i, 204, self.game.player_ai[0].gems[i] % 10)

        if self.game.isAIPlaying(1):
            for i in range(4):
                image.Number(self.window, 194 + 32 * i, 520, int(self.game.player_ai[1].gems[i] / 10))
                image.Number(self.window, 206 + 32 * i, 520, self.game.player_ai[1].gems[i] % 10)

        if self.game.isAIPlaying(2):
            for i in range(4):
                image.Number(self.window, 932 + 32 * i, 516, int(self.game.player_ai[2].gems[i] / 10))
                image.Number(self.window, 944 + 32 * i, 516, self.game.player_ai[2].gems[i] % 10)

    def showUserPlaces(self):
        image.Pos(self.window, 284, 84, self.game.player_human.game_place)

        if self.game.isAIPlaying(0):
            image.Pos(self.window, 1024, 80, self.game.player_ai[0].game_place)

        if self.game.isAIPlaying(1):
            image.Pos(self.window, 284, 398, self.game.player_ai[1].game_place)

        if self.game.isAIPlaying(2):
            image.Pos(self.window, 1024, 394, self.game.player_ai[2].game_place)

    def showPuzzles(self):
        for i in range(6):
            for j in range(6):
                image.tileColor(self.window, 84 + 16 * i, 130 + 16 * j, self.puzzle[j][i])

        if self.game.isAIPlaying(0):
            for i in range(6):
                for j in range(6):
                    image.tileColor(self.window, 822 + 16 * i, 126 + 16 * j, self.puzzle_ai[0][j][i])

        if self.game.isAIPlaying(1):
            for i in range(6):
                for j in range(6):
                    image.tileColor(self.window, 84 + 16 * i, 442 + 16 * j, self.puzzle_ai[1][j][i])

        if self.game.isAIPlaying(2):
            for i in range(6):
                for j in range(6):
                    image.tileColor(self.window, 822 + 16 * i, 438 + 16 * j, self.puzzle_ai[2][j][i])

    def showUnknownPieces(self):
        for i in range(4):
            image.Piece(self.window, 194 + 32 * i, 136, 12)

        if self.game.isAIPlaying(0):
            for i in range(4):
                image.Piece(self.window, 932 + 32 * i, 132, 12)

        if self.game.isAIPlaying(1):
            for i in range(4):
                image.Piece(self.window, 194 + 32 * i, 448, 12)

        if self.game.isAIPlaying(2):
            for i in range(4):
                image.Piece(self.window, 932 + 32 * i, 444, 12)

    def showPieces(self):
        for i in range(4):
            image.Piece(self.window, 194 + 32 * i, 136, self.game.getPieces(0)[i])
            if self.blocked_piece[i]:
                image.pieceBlocked(self.window, 194 + 32 * i, 136)

        if self.game.isAIPlaying(0):
            for i in range(4):
                image.Piece(self.window, 932 + 32 * i, 132, self.game.getPieces(1)[i])

        if self.game.isAIPlaying(1):
            for i in range(4):
                image.Piece(self.window, 194 + 32 * i, 448, self.game.getPieces(2)[i])

        if self.game.isAIPlaying(2):
            for i in range(4):
                image.Piece(self.window, 932 + 32 * i, 444, self.game.getPieces(3)[i])

    def showTimer(self):
        image.Number(self.window, 204, 310, int((self.game.time / 1000) * 6))
        image.Number(self.window, 216, 310, int((self.game.time / 1000) * 60) % 10)
        image.Number(self.window, 236, 310, int((self.game.time / 1000) * 600) % 10)
        image.Number(self.window, 248, 310, int((self.game.time / 1000) * 6000) % 10)

    def makingPuzzle(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x < 86 or mouse_x > 179 or mouse_y < 132 or mouse_y > 225:
            self.making_puzzle = False
            return

        ini_x = ini_y = -1
        pos_x = int((mouse_x - 86) / 15)
        pos_y = int((mouse_y - 132) / 15)

        for i in range(6):
            for j in range(6):
                if self.selected_piece[i][j] == 2:
                    ini_x = j
                    ini_y = i

        if pos_x != ini_x:
            if pos_x > ini_x:
                perm_x = [1, 2, 3, 4, 5, 0]
            else:
                perm_x = [5, 0, 1, 2, 3, 4]

            id_ = np.empty_like(perm_x)
            id_[perm_x] = np.arange(len(perm_x))
            self.selected_piece[:] = self.selected_piece[:, id_]

            if (self.selected_piece[:, 0] > 0).any() and (self.selected_piece[:, 5] > 0).any():
                self.making_puzzle = False
                return

        if pos_y != ini_y:
            if pos_y < ini_y:
                perm_y = [1, 2, 3, 4, 5, 0]
            else:
                perm_y = [5, 0, 1, 2, 3, 4]
            self.selected_piece[[0, 1, 2, 3, 4, 5]] = self.selected_piece[perm_y]

            if (self.selected_piece[0] > 0).any() and (self.selected_piece[5] > 0).any():
                self.making_puzzle = False
                return

        table = np.copy(self.puzzle)
        for i in range(6):
            for j in range(6):
                if self.selected_piece[i][j] > 0:
                    if table[i][j] >= 0:
                        table[i][j] = 13
                    else:
                        table[i][j] = 14

        for i in range(6):
            for j in range(6):
                image.tileColor(self.window, 84 + 16 * i, 130 + 16 * j, table[j][i])

    def Combine(self):
        for i in range(6):
            for j in range(6):
                if self.selected_piece[i][j] > 0 and self.puzzle[i][j] >= 0:
                    return

        for i in range(6):
            for j in range(6):
                if self.selected_piece[i][j] > 0:
                    self.puzzle[i][j] = self.game.getPieces(0)[self.selected_piece_id]

        self.making_puzzle = False
        self.blocked_piece[self.selected_piece_id] = True

        if (self.puzzle >= 0).all():
            self.completed_puzzle = True
            self.game.player_human.turn_place = self.turn_queue
            self.turn_queue += 1
            for i in range(6):
                for j in range(6):
                    if self.puzzle[i][j] < 12:
                        self.puzzle[i][j] = 14

    def fixMousePos(self):
        x = y = -1

        for i in range(6):
            for j in range(6):
                if self.selected_piece[i][j] == 2:
                    x = j
                    y = i

        new_x = 15 * x + 92
        new_y = 15 * y + 138
        pygame.mouse.set_pos(new_x, new_y)

    def aiTurn(self):
        for i in range(3):
            if self.game.player_ai[i].playing:
                if len(self.game.player_ai[i].piece_time) > 0:
                    if self.game.player_ai[i].piece_time[0] == self.game.time:
                        self.updateAiBoard(i)
                        if len(self.game.player_ai[i].piece_time) == 0:
                            self.game.player_ai[i].turn_place = np.copy(self.turn_queue)
                            self.turn_queue += 1

    def updateAiBoard(self, n):
        self.game.removeAiPieceTime(n)

        if len(self.game.player_ai[n].piece_time) == 0:
            for i in range(6):
                for j in range(6):
                    if self.puzzle_ai[n][i][j] != 12:
                        self.puzzle_ai[n][i][j] = 14
        else:
            for i in range(6):
                for j in range(6):
                    if self.game.player_ai[n].sols[len(self.game.player_ai[n].pieces_on) - 1][i][j] >= 0:
                        self.puzzle_ai[n][i][j] = \
                            self.game.player_ai[n].sols[len(self.game.player_ai[n].pieces_on) - 1][i][j]
