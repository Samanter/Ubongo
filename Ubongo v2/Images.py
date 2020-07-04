import pygame

number_0 = pygame.image.load("images/0.png")
number_1 = pygame.image.load("images/1.png")
number_2 = pygame.image.load("images/2.png")
number_3 = pygame.image.load("images/3.png")
number_4 = pygame.image.load("images/4.png")
number_5 = pygame.image.load("images/5.png")
number_6 = pygame.image.load("images/6.png")
number_7 = pygame.image.load("images/7.png")
number_8 = pygame.image.load("images/8.png")
number_9 = pygame.image.load("images/9.png")

arrow_up = pygame.image.load("images/arrow_up.png")
arrow_down = pygame.image.load("images/arrow_down.png")
arrow_left = pygame.image.load("images/arrow_left.png")
arrow_right = pygame.image.load("images/arrow_right.png")

banner_player = pygame.image.load("images/banner_player.png")
banner_cpu = pygame.image.load("images/banner_cpu.png")

begin_turn1 = pygame.image.load("images/begin_turn1.png")
begin_turn2 = pygame.image.load("images/begin_turn2.png")

card = pygame.image.load("images/card.png")
card_none = pygame.image.load("images/card_none.png")

dice_1 = pygame.image.load("images/dice1.png")
dice_2 = pygame.image.load("images/dice2.png")
dice_3 = pygame.image.load("images/dice3.png")
dice_4 = pygame.image.load("images/dice4.png")
dice_5 = pygame.image.load("images/dice5.png")
dice_6 = pygame.image.load("images/dice6.png")

game_background = pygame.image.load("images/game_background.png")
game_config = pygame.image.load("images/game_config.png")
game_instructions = pygame.image.load("images/game_instructions.png")
game_menu = pygame.image.load("images/game_menu.png")
game_pause = pygame.image.load("images/game_pause.png")
game_play_area = pygame.image.load("images/game_play_area.png")
game_win = pygame.image.load("images/game_win.png")

gem_0 = pygame.image.load("images/gem0.png")
gem_1 = pygame.image.load("images/gem1.png")
gem_2 = pygame.image.load("images/gem2.png")
gem_3 = pygame.image.load("images/gem3.png")
gem_4 = pygame.image.load("images/gem4.png")

hints = pygame.image.load("images/hints.png")
hints_hidden = pygame.image.load("images/hints_hidden.png")

piece_0 = pygame.image.load("images/piece0.png")
piece_1 = pygame.image.load("images/piece1.png")
piece_2 = pygame.image.load("images/piece2.png")
piece_3 = pygame.image.load("images/piece3.png")
piece_4 = pygame.image.load("images/piece4.png")
piece_5 = pygame.image.load("images/piece5.png")
piece_6 = pygame.image.load("images/piece6.png")
piece_7 = pygame.image.load("images/piece7.png")
piece_8 = pygame.image.load("images/piece8.png")
piece_9 = pygame.image.load("images/piece9.png")
piece_10 = pygame.image.load("images/piece10.png")
piece_11 = pygame.image.load("images/piece11.png")
piece_12 = pygame.image.load("images/piece12.png")

piece_blocked = pygame.image.load("images/piece_blocked.png")

pos_1 = pygame.image.load("images/pos1.png")
pos_2 = pygame.image.load("images/pos2.png")
pos_3 = pygame.image.load("images/pos3.png")
pos_4 = pygame.image.load("images/pos4.png")

return_ = pygame.image.load("images/return.png")
shadow = pygame.image.load("images/shadow.png")

selected_arrow_left = pygame.image.load("images/selected_arrow_left.png")
selected_arrow_right = pygame.image.load("images/selected_arrow_right.png")
selected_back = pygame.image.load("images/selected_back.png")
selected_begin_turn = pygame.image.load("images/selected_begin_turn.png")
selected_config = pygame.image.load("images/selected_config.png")
selected_exit = pygame.image.load("images/selected_exit.png")
selected_instructions = pygame.image.load("images/selected_instructions.png")
selected_piece = pygame.image.load("images/selected_piece.png")
selected_play = pygame.image.load("images/selected_play.png")
selected_return = pygame.image.load("images/selected_return.png")
selected_shadow = pygame.image.load("images/selected_shadow.png")
selected_space = pygame.image.load("images/selected_space.png")

tile_colorn1 = pygame.image.load("images/tile_color-1.png")
tile_color0 = pygame.image.load("images/tile_color0.png")
tile_color1 = pygame.image.load("images/tile_color1.png")
tile_color2 = pygame.image.load("images/tile_color2.png")
tile_color3 = pygame.image.load("images/tile_color3.png")
tile_color4 = pygame.image.load("images/tile_color4.png")
tile_color5 = pygame.image.load("images/tile_color5.png")
tile_color6 = pygame.image.load("images/tile_color6.png")
tile_color7 = pygame.image.load("images/tile_color7.png")
tile_color8 = pygame.image.load("images/tile_color8.png")
tile_color9 = pygame.image.load("images/tile_color9.png")
tile_color10 = pygame.image.load("images/tile_color10.png")
tile_color11 = pygame.image.load("images/tile_color11.png")
tile_color12 = pygame.image.load("images/tile_color12.png")
tile_color13 = pygame.image.load("images/tile_color13.png")
tile_color14 = pygame.image.load("images/tile_color14.png")

user_cpu1 = pygame.image.load("images/user_cpu1.png")
user_cpu2 = pygame.image.load("images/user_cpu2.png")
user_cpu3 = pygame.image.load("images/user_cpu3.png")
user_player = pygame.image.load("images/user_player.png")

winner_0 = pygame.image.load("images/winner_0.png")
winner_1 = pygame.image.load("images/winner_1.png")
winner_2 = pygame.image.load("images/winner_2.png")
winner_3 = pygame.image.load("images/winner_3.png")

def Number(window, x, y, n):
    if n == 0:
        window.blit(number_0, (x, y))
    elif n == 1:
        window.blit(number_1, (x, y))
    elif n == 2:
        window.blit(number_2, (x, y))
    elif n == 3:
        window.blit(number_3, (x, y))
    elif n == 4:
        window.blit(number_4, (x, y))
    elif n == 5:
        window.blit(number_5, (x, y))
    elif n == 6:
        window.blit(number_6, (x, y))
    elif n == 7:
        window.blit(number_7, (x, y))
    elif n == 8:
        window.blit(number_8, (x, y))
    elif n == 9:
        window.blit(number_9, (x, y))

def arrowUp(window, x, y):
    window.blit(arrow_up, (x, y))

def arrowDown(window, x, y):
    window.blit(arrow_down, (x, y))

def arrowLeft(window, x, y):
    window.blit(arrow_left, (x, y))

def arrowRight(window, x, y):
    window.blit(arrow_right, (x, y))

def bannerPlayer(window, x, y):
    window.blit(banner_player, (x, y))

def bannerCPU(window, x, y):
    window.blit(banner_cpu, (x, y))

def beginTurn(window, x, y, n):
    if n == 1:
        window.blit(begin_turn1, (x, y))
    elif n == 2:
        window.blit(begin_turn2, (x, y))

def Card(window, x, y):
    window.blit(card, (x, y))

def cardNone(window, x, y):
    window.blit(card_none, (x, y))

def Dice(window, x, y, n):
    if n == 1:
        window.blit(dice_1, (x, y))
    elif n == 2:
        window.blit(dice_2, (x, y))
    elif n == 3:
        window.blit(dice_3, (x, y))
    elif n == 4:
        window.blit(dice_4, (x, y))
    elif n == 5:
        window.blit(dice_5, (x, y))
    elif n == 6:
        window.blit(dice_6, (x, y))

def gameBackground(window, x, y):
    window.blit(game_background, (x, y))

def gameConfig(window, x, y):
    window.blit(game_config, (x, y))

def gameInstructions(window, x, y):
    window.blit(game_instructions, (x, y))

def gameMenu(window, x, y):
    window.blit(game_menu, (x, y))

def gamePlayArea(window, x, y):
    window.blit(game_play_area, (x, y))

def gamePause(window, x, y):
    window.blit(game_pause, (x, y))

def gameWin(window, x, y):
    window.blit(game_win, (x, y))

def Gem(window, x, y, n):
    if n == 0:
        window.blit(gem_0, (x, y))
    elif n == 1:
        window.blit(gem_1, (x, y))
    elif n == 2:
        window.blit(gem_2, (x, y))
    elif n == 3:
        window.blit(gem_3, (x, y))
    elif n == 4:
        window.blit(gem_4, (x, y))

def Hints(window, x, y):
    window.blit(hints, (x, y))

def hintsHidden(window, x, y):
    window.blit(hints_hidden, (x, y))

def Piece(window, x, y, n):
    if n == 0:
        window.blit(piece_0, (x, y))
    elif n == 1:
        window.blit(piece_1, (x, y))
    elif n == 2:
        window.blit(piece_2, (x, y))
    elif n == 3:
        window.blit(piece_3, (x, y))
    elif n == 4:
        window.blit(piece_4, (x, y))
    elif n == 5:
        window.blit(piece_5, (x, y))
    elif n == 6:
        window.blit(piece_6, (x, y))
    elif n == 7:
        window.blit(piece_7, (x, y))
    elif n == 8:
        window.blit(piece_8, (x, y))
    elif n == 9:
        window.blit(piece_9, (x, y))
    elif n == 10:
        window.blit(piece_10, (x, y))
    elif n == 11:
        window.blit(piece_11, (x, y))
    elif n == 12:
        window.blit(piece_12, (x, y))

def pieceBlocked(window, x, y):
    window.blit(piece_blocked, (x, y))

def Pos(window, x, y, n):
    if n == 1:
        window.blit(pos_1, (x, y))
    elif n == 2:
        window.blit(pos_2, (x, y))
    elif n == 3:
        window.blit(pos_3, (x, y))
    elif n == 4:
        window.blit(pos_4, (x, y))

def Return(window, x, y):
    window.blit(return_, (x, y))

def Shadow(window, x, y):
    window.blit(shadow, (x, y))

def selectedArrowLeft(window, x, y):
    window.blit(selected_arrow_left, (x, y))

def selectedArrowRight(window, x, y):
    window.blit(selected_arrow_right, (x, y))

def selectedBack(window, x, y):
    window.blit(selected_back, (x ,y))

def selectedBeginTurn(window, x, y):
    window.blit(selected_begin_turn, (x, y))

def selectedConfig(window, x, y):
    window.blit(selected_config, (x, y))

def selectedExit(window, x, y):
    window.blit(selected_exit, (x, y))

def selectedInstructions(window, x, y):
    window.blit(selected_instructions, (x, y))

def selectedPiece(window, x, y):
    window.blit(selected_piece, (x, y))

def selectedPlay(window, x, y):
    window.blit(selected_play, (x, y))

def selectedReturn(window, x, y):
    window.blit(selected_return, (x, y))

def selectedShadow(window, x, y):
    window.blit(selected_shadow, (x, y))

def selectedSpace(window, x, y):
    window.blit(selected_space, (x, y))

def tileColor(window, x, y, n):
    if n == -1:
        window.blit(tile_colorn1, (x, y))
    elif n == 0:
        window.blit(tile_color0, (x, y))
    elif n == 1:
        window.blit(tile_color1, (x, y))
    elif n == 2:
        window.blit(tile_color2, (x, y))
    elif n == 3:
        window.blit(tile_color3, (x, y))
    elif n == 4:
        window.blit(tile_color4, (x, y))
    elif n == 5:
        window.blit(tile_color5, (x, y))
    elif n == 6:
        window.blit(tile_color6, (x, y))
    elif n == 7:
        window.blit(tile_color7, (x, y))
    elif n == 8:
        window.blit(tile_color8, (x, y))
    elif n == 9:
        window.blit(tile_color9, (x, y))
    elif n == 10:
        window.blit(tile_color10, (x, y))
    elif n == 11:
        window.blit(tile_color11, (x, y))
    elif n == 12:
        window.blit(tile_color12, (x, y))
    elif n == 13:
        window.blit(tile_color13, (x, y))
    elif n == 14:
        window.blit(tile_color14, (x, y))

def userCPU(window, x, y, n):
    if n == 1:
        window.blit(user_cpu1, (x, y))
    elif n == 2:
        window.blit(user_cpu2, (x, y))
    elif n == 3:
        window.blit(user_cpu3, (x, y))

def userPlayer(window, x, y):
    window.blit(user_player, (x, y))

def Winner(window, x, y, n):
    if n == 0:
        window.blit(winner_0, (x, y))
    elif n == 1:
        window.blit(winner_1, (x, y))
    elif n == 2:
        window.blit(winner_2, (x, y))
    elif n == 3:
        window.blit(winner_3, (x, y))
