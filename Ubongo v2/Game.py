from PlayerAI import PlayerAI
from PlayerHuman import PlayerHuman
from Table import Table
from Puzzles import Puzzles
from Piece import Piece
from WindowManager import Window
import numpy as np

def comp(a, b):
    if a[3] == b[3]:
        if a[2] == b[2]:
            if a[1] == a[1]:
                return a[0] < b[0]
            return a[1] < b[1]
        return a[2] < b[2]
    return a[3] < b[3]

def customSort(matrix):
    for i in range(3):
        for j in range(i + 1, 4):
            if comp(matrix[i], matrix[j]):
                matrix[[i, j]] = matrix[[j, i]]

class Game:
    def __init__(self):
        self.player_ai = np.ndarray(3, dtype=PlayerAI)
        for i in range(3):
            self.player_ai[i] = PlayerAI()
        self.player_human = PlayerHuman()
        self.table = Table()
        self.puzzles = Puzzles()
        self.piece = Piece()
        self.window = Window()
        self.turn = 0
        self.time = 0
        self.dice = 0
        self.winner = 0
        self.set_time = 1000
        self.set_turn = 9

    def startGame(self):
        self.gotoGame()
        self.resetPos()
        self.resetGems()
        self.resetTurn()
        self.resetPlaces()
        self.resetTimer()
        self.resetUserTurns()
        self.resetTable()
        self.resetPuzzle()

    def Window(self):
        return self.window.window_Type

    def nPlayers(self):
        return self.table.n_players

    def playerTurnPlace(self):
        return self.player_human.turn_place

    def gotoMenu(self):
        self.window.window_Type = 0

    def gotoGame(self):
        self.window.window_Type = 1

    def gotoInstructions(self):
        self.window.window_Type = 2

    def gotoConfig(self):
        self.window.window_Type = 3

    def throwDice(self):
        self.dice = np.random.randint(0, 6)

    def resetTimer(self):
        self.time = 0

    def resetTurn(self):
        self.turn = 1

    def resetPlaces(self):
        self.player_human.game_place = 1
        for i in range(3):
            self.player_ai[i].game_place = 1

    def resetUserTurns(self):
        self.player_human.turn_place = 10
        for i in range(3):
            self.player_ai[i].turn_place = 10

    def resetPos(self):
        self.player_human.pos = -1
        self.player_ai[0].pos = -1
        self.player_ai[1].pos = -1
        self.player_ai[2].pos = -1

    def resetGems(self):
        self.player_human.resetGems()
        self.player_ai[0].resetGems()
        self.player_ai[1].resetGems()
        self.player_ai[2].resetGems()

    def startTimer(self):
        self.time = self.set_time

    def resetTable(self):
        self.table.generateTable()

    def resetPuzzle(self):
        self.puzzles.createPuzzles()
        self.puzzles.shufflePuzzles()

    def chooseRow(self):
        self.player_human.chooseRow(self.table)

    def updatePlaces(self):
        users_gems = np.zeros((4, 4), dtype=int)
        users_gems[0] = self.player_human.gems.copy()
        users_gems[0] = np.sort(users_gems[0])
        for i in range(1, 4):
            users_gems[i] = self.player_ai[i - 1].gems.copy()
            users_gems[i] = np.sort(users_gems[i])

        customSort(users_gems)

        for i in range(4):
            aux = self.player_human.gems.copy()
            aux = np.sort(aux)
            if np.array_equal(aux, users_gems[i]):
                self.player_human.game_place = i + 1
                break

        for i in range(3):
            for j in range(4):
                aux = self.player_ai[i].gems.copy()
                aux = np.sort(aux)
                if np.array_equal(aux, users_gems[j]):
                    self.player_ai[i].game_place = j + 1
                    break

    def isAIPlaying(self, n):
        return self.player_ai[n].playing

    def setAiPieceTimes(self):
        for i in range(3):
            self.player_ai[i].setPieceTimes(self.set_time)

    def removeAiPieceTime(self, n):
        self.player_ai[n].removePieceTime()

    def getSol(self, index, n):
        self.player_ai[n].getSol(self.puzzles.puzzles[index], self.piece, self.dice)

    def getPuzzles(self, n):
        return self.puzzles.puzzles[n].form

    def getPiece(self, n):
        return self.piece.pieces[n]

    def getPieces(self, n):
        return self.puzzles.puzzles[n].p_pieces[self.dice]

    def refreshPuzzles(self):
        for i in range(self.table.n_players):
            self.puzzles.puzzles = np.delete(self.puzzles.puzzles, 0)

    def getWinner(self):
        if self.player_human.game_place == 1:
            self.winner = 0
        elif self.player_ai[0].game_place == 1:
            self.winner = 1
        elif self.player_ai[1].game_place == 1:
            self.winner = 2
        elif self.player_ai[2].game_place == 1:
            self.winner = 3
