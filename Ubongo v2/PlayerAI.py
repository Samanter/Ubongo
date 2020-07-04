from Table import Table
from Piece import Piece
from Puzzle import Puzzle
from Player import Player
import numpy as np

def fixPos(matrix):
    while (matrix[0] == -1).all():
        perm_y = [1, 2, 3, 4, 5, 0]
        matrix[[0, 1, 2, 3, 4, 5]] = matrix[perm_y]
    return matrix

def rot(matrix):
    matrix = np.rot90(matrix, 1, (0, 1))
    matrix = fixPos(matrix)
    return matrix

def flip(matrix):
    matrix = np.flipud(matrix)
    matrix = fixPos(matrix)
    return matrix

class PlayerAI(Player):
    def generateInitialPos(self):
        self.pos = np.random.randint(0, 6)

    def chooseRow(self, table: Table):
        bp = False
        bckp = np.zeros(2, dtype=int)
        min_x = max(0, self.pos - (table.n_players - self.turn_place))
        max_x = min(5, self.pos + (table.n_players - self.turn_place))

        for j in range(min_x, max_x + 1):
            for i in range(0, 11, 2):
                if table.gems_pos[i, j] > 0:
                    if table.gems_pos[i, j] == table.gems_pos[i + 1, j]:
                        self.gems[table.gems_pos[i, j] - 1] += 2
                        table.gems_pos[i, j] = table.gems_pos[i + 1, j] = 0
                        self.pos = j
                        return
                    if not bp:
                        bckp = [i, j]
                        bp = True
                    break

        self.gems[table.gems_pos[bckp[0], bckp[1]] - 1] += 1
        self.gems[table.gems_pos[bckp[0] + 1, bckp[1]] - 1] += 1
        table.gems_pos[bckp[0], bckp[1]] = table.gems_pos[bckp[0] + 1, bckp[1]] = 0
        self.pos = bckp[1]

    def setPieceTimes(self, time):
        self.piece_time = np.flip(np.sort(np.random.randint(100, time - 100, size=4)))
        while self.piece_time[0] == self.piece_time[1] or self.piece_time[0] == self.piece_time[2] or \
                self.piece_time[0] == self.piece_time[3] or self.piece_time[1] == self.piece_time[2] or \
                self.piece_time[1] == self.piece_time[3] or self.piece_time[2] == self.piece_time[3]:
            self.piece_time = np.flip(np.sort(np.random.randint(100, time - 100, size=4)))
        while len(self.pieces_on) > 0:
            self.pieces_on = np.delete(self.pieces_on, [0])

    def removePieceTime(self):
        self.piece_time = np.delete(self.piece_time, [0])
        self.pieces_on = np.append(self.pieces_on, len(self.pieces_on))

    def getSol(self, puzzle: Puzzle, piece: Piece, n):
        self.solved = False
        self.solving_puzzle = np.full((6, 6), -1, dtype=int)
        pieces = np.zeros((4, 6, 6), dtype=int)
        pieces_id = np.copy(puzzle.p_pieces[n])
        self.solving_puzzle = np.copy(puzzle.form)
        for i in range(4):
            pieces[i] = np.copy(piece.pieces[pieces_id[i]])
        self.recursiveSol(pieces, 0, pieces_id)
        used_pieces = np.full((4, 6, 6), -1, dtype=int)
        id_ = 0

        for k in range(12):
            if (self.solving_puzzle == k).any():
                for i in range(6):
                    for j in range(6):
                        if self.solving_puzzle[i][j] == k:
                            used_pieces[id_][i][j] = k
                id_ += 1
        self.sols = used_pieces

    def recursiveSol(self, pieces, n, piece_id):
        if n == 4:
            self.solved = True
            return
        piece_areas = [[], [], [], [], [], [], [], []]
        max_i = np.array([0, 0, 0, 0, 0, 0, 0, 0], dtype=int)
        max_j = np.array([0, 0, 0, 0, 0, 0, 0, 0], dtype=int)
        for f in range(2):
            pieces[n] = flip(pieces[n])
            for r in range(4):
                for i in range(6):
                    for j in range(6):
                        if pieces[n][i][j] > 0:
                            piece_areas[r + f * 4].append((i, j))
                            max_i[r + f * 4] = max(i, max_i[r + f * 4])
                            max_j[r + f * 4] = max(j, max_j[r + f * 4])
                pieces[n] = rot(pieces[n])
        for r in range(8):
            for i in range(6 - max_i[r]):
                for j in range(6 - max_j[r]):
                    rejected = False
                    for k in range(len(piece_areas[r])):
                        if self.solving_puzzle[piece_areas[r][k][0] + i][piece_areas[r][k][1] + j] >= 0:
                            rejected = True
                            break

                    if not rejected:
                        for k in range(len(piece_areas[r])):
                            self.solving_puzzle[piece_areas[r][k][0] + i][piece_areas[r][k][1] + j] = piece_id[n]
                        self.recursiveSol(pieces, n + 1, piece_id)
                        if self.solved:
                            return
                        else:
                            for k in range(len(piece_areas[r])):
                                self.solving_puzzle[piece_areas[r][k][0] + i][piece_areas[r][k][1] + j] = -1
