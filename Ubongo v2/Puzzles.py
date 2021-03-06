from Puzzle import Puzzle
import numpy as np


class Puzzles:
    def __init__(self):
        self.puzzles = np.ndarray(36, dtype=Puzzle)
        for i in range(36):
            self.puzzles[i] = Puzzle()

    def createPuzzles(self):
        self.puzzles = np.ndarray(36, dtype=Puzzle)
        for i in range(36):
            self.puzzles[i] = Puzzle()

        self.puzzles[0].form = [[12, 12, 12, 12, 12, -1],
                                [12, -1, -1, -1, -1, -1],
                                [12, 12, -1, -1, -1, -1],
                                [12, 12, -1, -1, -1, -1],
                                [12, 12, 12, 12, -1, -1],
                                [12, 12, 12, 12, -1, -1]]

        self.puzzles[1].form = [[12, 12, 12, -1, 12, 12],
                                [12, 12, -1, -1, -1, 12],
                                [12, 12, -1, -1, -1, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, -1, -1, 12, 12, 12]]

        self.puzzles[2].form = [[12, 12, 12, 12, 12, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, 12, -1, -1, -1, -1],
                                [12, 12, -1, -1, -1, -1],
                                [12, 12, 12, 12, 12, 12]]

        self.puzzles[3].form = [[12, 12, -1, -1, -1, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, 12, -1, -1, -1, 12],
                                [12, 12, -1, -1, 12, 12],
                                [12, 12, -1, -1, 12, 12]]

        self.puzzles[4].form = [[12, 12, 12, 12, -1, 12],
                                [12, 12, 12, 12, -1, 12],
                                [12, 12, 12, 12, -1, -1],
                                [12, 12, -1, -1, -1, -1],
                                [12, -1, -1, -1, -1, -1],
                                [12, -1, -1, -1, -1, 12]]

        self.puzzles[5].form = [[12, -1, -1, -1, -1, -1],
                                [12, -1, -1, -1, -1, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, 12, -1, 12, 12, 12],
                                [12, 12, 12, 12, 12, 12]]

        self.puzzles[6].form = [[12, 12, -1, -1, 12, 12],
                                [12, 12, -1, -1, -1, 12],
                                [12, 12, -1, -1, -1, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, -1, -1, 12, 12, 12],
                                [12, -1, -1, 12, 12, 12]]

        self.puzzles[7].form = [[12, 12, 12, 12, 12, 12],
                                [12, 12, -1, -1, -1, -1],
                                [12, 12, -1, -1, -1, -1],
                                [12, -1, -1, -1, -1, -1],
                                [12, -1, -1, 12, -1, 12],
                                [12, 12, 12, 12, 12, 12]]

        self.puzzles[8].form = [[12, -1, -1, -1, -1, 12],
                                [12, -1, -1, 12, 12, 12],
                                [12, -1, -1, 12, 12, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, 12, 12, 12, -1, 12]]

        self.puzzles[9].form = [[12, 12, 12, 12, 12, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, -1, -1, -1, -1, 12],
                                [12, -1, -1, -1, -1, -1],
                                [12, -1, -1, 12, 12, -1],
                                [12, 12, 12, 12, 12, 12]]

        self.puzzles[10].form = [[12, 12, 12, 12, 12, 12],
                                 [12, 12, 12, -1, -1, 12],
                                 [12, 12, 12, -1, -1, 12],
                                 [12, 12, 12, -1, -1, -1],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, -1]]

        self.puzzles[11].form = [[12, 12, 12, 12, 12, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, 12, -1, 12, 12]]

        self.puzzles[12].form = [[12, 12, 12, 12, 12, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, 12, 12, 12, 12, 12]]

        self.puzzles[13].form = [[12, 12, 12, 12, 12, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, -1, 12, 12],
                                 [12, -1, -1, -1, 12, 12],
                                 [12, 12, -1, -1, 12, 12]]

        self.puzzles[14].form = [[12, 12, 12, 12, 12, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, 12, 12, -1, -1],
                                 [12, 12, 12, 12, 12, 12]]

        self.puzzles[15].form = [[12, 12, 12, 12, 12, 12],
                                 [12, 12, 12, -1, 12, 12],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, 12, 12, 12, 12]]

        self.puzzles[16].form = [[12, 12, 12, 12, 12, 12],
                                 [12, 12, 12, -1, -1, -1],
                                 [12, 12, 12, -1, -1, -1],
                                 [12, 12, 12, -1, -1, -1],
                                 [12, 12, 12, -1, -1, -1],
                                 [12, -1, -1, -1, -1, -1]]

        self.puzzles[17].form = [[12, 12, 12, 12, 12, 12],
                                 [12, 12, 12, -1, -1, -1],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, 12, 12, -1, 12]]

        self.puzzles[18].form = [[12, 12, 12, 12, 12, 12],
                                 [12, -1, -1, 12, 12, 12],
                                 [12, -1, -1, 12, 12, 12],
                                 [12, -1, -1, -1, 12, -1],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, 12, 12, -1, -1, -1]]

        self.puzzles[19].form = [[12, 12, 12, 12, 12, 12],
                                 [12, 12, 12, -1, -1, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, 12, -1, -1, -1]]

        self.puzzles[20].form = [[12, 12, 12, 12, 12, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, 12, 12],
                                 [12, 12, 12, 12, 12, 12]]

        self.puzzles[21].form = [[12, 12, 12, 12, 12, 12],
                                 [12, -1, -1, 12, 12, 12],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, 12, 12, 12, 12, 12]]

        self.puzzles[22].form = [[12, 12, -1, 12, 12, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, 12, 12, 12, 12]]

        self.puzzles[23].form = [[12, 12, 12, 12, 12, 12],
                                 [12, 12, -1, -1, 12, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, 12, 12],
                                 [12, -1, -1, -1, 12, 12]]

        self.puzzles[24].form = [[12, -1, -1, -1, 12, 12],
                                 [12, -1, -1, -1, 12, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, 12, 12, -1, 12]]

        self.puzzles[25].form = [[12, 12, 12, 12, 12, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, 12, 12, 12, 12, 12]]

        self.puzzles[26].form = [[12, 12, -1, -1, -1, 12],
                                 [12, 12, -1, -1, 12, 12],
                                 [12, 12, -1, -1, 12, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, 12, -1, -1, 12]]

        self.puzzles[27].form = [[12, 12, 12, 12, 12, -1],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, 12, -1, -1, -1, -1],
                                 [12, 12, -1, -1, -1, -1],
                                 [12, 12, 12, 12, -1, -1],
                                 [12, 12, 12, 12, -1, -1]]

        self.puzzles[28].form = [[12, 12, 12, -1, 12, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, 12, 12, 12]]

        self.puzzles[29].form = [[12, 12, 12, 12, 12, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, -1, -1, -1, -1],
                                 [12, 12, -1, -1, -1, -1],
                                 [12, 12, 12, 12, 12, 12]]

        self.puzzles[30].form = [[12, 12, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, 12, -1, -1, 12, 12],
                                 [12, 12, -1, -1, 12, 12]]

        self.puzzles[31].form = [[12, 12, 12, 12, -1, 12],
                                 [12, 12, 12, 12, -1, 12],
                                 [12, 12, 12, 12, -1, -1],
                                 [12, 12, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, 12]]

        self.puzzles[32].form = [[12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, -1, 12, 12, 12],
                                 [12, 12, 12, 12, 12, 12]]

        self.puzzles[33].form = [[12, 12, -1, -1, 12, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, 12, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, 12, 12, 12],
                                 [12, -1, -1, 12, 12, 12]]

        self.puzzles[34].form = [[12, 12, 12, 12, 12, 12],
                                 [12, 12, -1, -1, -1, -1],
                                 [12, 12, -1, -1, -1, -1],
                                 [12, -1, -1, -1, -1, -1],
                                 [12, -1, -1, 12, -1, 12],
                                 [12, 12, 12, 12, 12, 12]]

        self.puzzles[35].form = [[12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, 12, 12, 12],
                                 [12, -1, -1, 12, 12, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, -1, -1, -1, -1, 12],
                                 [12, 12, 12, 12, -1, 12]]

        self.puzzles[0].p_pieces = [[2, 5, 8, 10],
                                    [2, 3, 10, 11],
                                    [0, 7, 10, 11],
                                    [1, 5, 7, 8],
                                    [2, 9, 10, 11],
                                    [1, 5, 7, 9]]

        self.puzzles[1].p_pieces = [[1, 2, 8, 10],
                                    [0, 1, 7, 11],
                                    [0, 1, 10, 11],
                                    [3, 4, 10, 11],
                                    [0, 5, 9, 10],
                                    [3, 4, 5, 11]]

        self.puzzles[2].p_pieces = [[0, 8, 9, 10],
                                    [1, 5, 6, 11],
                                    [0, 4, 7, 11],
                                    [3, 6, 7, 10],
                                    [1, 2, 4, 5],
                                    [3, 4, 5, 9]]

        self.puzzles[3].p_pieces = [[8, 9, 10, 11],
                                    [2, 7, 9, 11],
                                    [1, 5, 8, 10],
                                    [2, 8, 10, 11],
                                    [3, 5, 8, 10],
                                    [1, 5, 9, 11]]

        self.puzzles[4].p_pieces = [[4, 5, 9, 10],
                                    [4, 5, 8, 11],
                                    [1, 2, 5, 9],
                                    [4, 8, 10, 11],
                                    [1, 2, 9, 11],
                                    [1, 4, 5, 11]]

        self.puzzles[5].p_pieces = [[2, 5, 9, 11],
                                    [1, 2, 7, 10],
                                    [2, 5, 9, 10],
                                    [0, 7, 10, 11],
                                    [1, 2, 5, 11],
                                    [3, 5, 9, 11]]

        self.puzzles[6].p_pieces = [[0, 4, 5, 10],
                                    [0, 8, 9, 11],
                                    [3, 6, 7, 11],
                                    [0, 1, 2, 10],
                                    [1, 4, 8, 11],
                                    [1, 5, 6, 11]]

        self.puzzles[7].p_pieces = [[3, 6, 10, 11],
                                    [3, 5, 6, 11],
                                    [6, 8, 10, 11],
                                    [2, 4, 8, 11],
                                    [0, 1, 8, 11],
                                    [1, 2, 4, 11]]

        self.puzzles[8].p_pieces = [[0, 1, 5, 11],
                                    [4, 5, 9, 11],
                                    [1, 4, 10, 11],
                                    [3, 4, 10, 11],
                                    [5, 6, 10, 11],
                                    [0, 5, 9, 10]]

        self.puzzles[9].p_pieces = [[1, 5, 6, 7],
                                    [2, 6, 10, 11],
                                    [0, 1, 5, 9],
                                    [5, 6, 7, 8],
                                    [1, 5, 6, 10],
                                    [0, 1, 7, 8]]

        self.puzzles[10].p_pieces = [[3, 4, 5, 11],
                                     [6, 7, 10, 11],
                                     [1, 2, 9, 10],
                                     [2, 3, 5, 8],
                                     [0, 2, 7, 10],
                                     [1, 2, 8, 11]]

        self.puzzles[11].p_pieces = [[1, 7, 8, 9],
                                     [1, 2, 5, 9],
                                     [1, 4, 5, 10],
                                     [1, 4, 7, 11],
                                     [0, 8, 10, 11],
                                     [3, 4, 7, 11]]

        self.puzzles[12].p_pieces = [[3, 4, 6, 10],
                                     [2, 4, 6, 11],
                                     [3, 4, 5, 6],
                                     [2, 4, 6, 10],
                                     [1, 2, 6, 9],
                                     [4, 6, 8, 10]]

        self.puzzles[13].p_pieces = [[4, 5, 9, 11],
                                     [5, 6, 10, 11],
                                     [2, 8, 9, 11],
                                     [4, 7, 8, 10],
                                     [1, 2, 8, 11],
                                     [3, 8, 9, 11]]

        self.puzzles[14].p_pieces = [[3, 4, 5, 8],
                                     [0, 4, 10, 11],
                                     [1, 3, 4, 7],
                                     [2, 3, 4, 10],
                                     [1, 6, 7, 11],
                                     [1, 6, 10, 11]]

        self.puzzles[15].p_pieces = [[0, 3, 4, 7],
                                     [1, 6, 8, 11],
                                     [0, 2, 4, 10],
                                     [1, 5, 6, 9],
                                     [2, 6, 8, 10],
                                     [2, 3, 4, 8]]

        self.puzzles[16].p_pieces = [[4, 7, 8, 11],
                                     [5, 6, 10, 11],
                                     [0, 5, 9, 10],
                                     [2, 4, 10, 11],
                                     [1, 4, 5, 11],
                                     [2, 4, 5, 10]]

        self.puzzles[17].p_pieces = [[5, 6, 7, 10],
                                     [1, 4, 7, 11],
                                     [1, 4, 10, 11],
                                     [1, 4, 5, 11],
                                     [0, 1, 5, 11],
                                     [0, 5, 9, 11]]

        self.puzzles[18].p_pieces = [[1, 5, 6, 11],
                                     [2, 4, 8, 11],
                                     [3, 6, 10, 11],
                                     [1, 3, 4, 7],
                                     [0, 3, 8, 11],
                                     [6, 7, 8, 11]]

        self.puzzles[19].p_pieces = [[1, 5, 6, 11],
                                     [1, 6, 10, 11],
                                     [1, 2, 4, 7],
                                     [1, 4, 8, 10],
                                     [6, 7, 8, 10],
                                     [0, 1, 2, 5]]

        self.puzzles[20].p_pieces = [[1, 2, 5, 6],
                                     [0, 1, 4, 10],
                                     [4, 6, 7, 11],
                                     [0, 1, 3, 8],
                                     [3, 5, 6, 8],
                                     [6, 8, 9, 11]]

        self.puzzles[21].p_pieces = [[0, 1, 7, 11],
                                     [1, 8, 9, 10],
                                     [2, 3, 8, 10],
                                     [0, 2, 5, 11],
                                     [0, 3, 5, 10],
                                     [1, 2, 9, 11]]

        self.puzzles[22].p_pieces = [[3, 5, 6, 10],
                                     [5, 6, 7, 8],
                                     [3, 4, 5, 9],
                                     [5, 6, 8, 10],
                                     [1, 2, 4, 5],
                                     [1, 3, 4, 11]]

        self.puzzles[23].p_pieces = [[1, 6, 8, 11],
                                     [0, 4, 5, 8],
                                     [1, 2, 6, 7],
                                     [0, 6, 10, 11],
                                     [1, 5, 6, 8],
                                     [4, 6, 7, 11]]

        self.puzzles[24].p_pieces = [[1, 5, 8, 11],
                                     [1, 3, 5, 10],
                                     [3, 9, 10, 11],
                                     [3, 5, 9, 11],
                                     [1, 2, 5, 11],
                                     [1, 9, 10, 11]]

        self.puzzles[25].p_pieces = [[4, 7, 8, 11],
                                     [2, 4, 10, 11],
                                     [5, 6, 10, 11],
                                     [0, 7, 8, 10],
                                     [0, 3, 5, 11],
                                     [1, 3, 8, 11]]

        self.puzzles[26].p_pieces = [[4, 7, 8, 11],
                                     [2, 4, 5, 11],
                                     [1, 4, 7, 11],
                                     [0, 1, 7, 10],
                                     [2, 3, 8, 11],
                                     [0, 1, 5, 11]]

        self.puzzles[27].p_pieces = [[2, 5, 8, 10],
                                     [2, 3, 10, 11],
                                     [0, 7, 10, 11],
                                     [1, 5, 7, 8],
                                     [2, 9, 10, 11],
                                     [1, 5, 7, 9]]

        self.puzzles[28].p_pieces = [[1, 2, 8, 10],
                                     [0, 1, 7, 11],
                                     [0, 1, 10, 11],
                                     [3, 4, 10, 11],
                                     [0, 5, 9, 10],
                                     [3, 4, 5, 11]]

        self.puzzles[29].p_pieces = [[0, 8, 9, 10],
                                     [1, 5, 6, 11],
                                     [0, 4, 7, 11],
                                     [3, 6, 7, 10],
                                     [1, 2, 4, 5],
                                     [3, 4, 5, 9]]

        self.puzzles[30].p_pieces = [[8, 9, 10, 11],
                                     [2, 7, 9, 11],
                                     [1, 5, 8, 10],
                                     [2, 8, 10, 11],
                                     [3, 5, 8, 10],
                                     [1, 5, 9, 11]]

        self.puzzles[31].p_pieces = [[4, 5, 9, 10],
                                     [4, 5, 8, 11],
                                     [1, 2, 5, 9],
                                     [4, 8, 10, 11],
                                     [1, 2, 9, 11],
                                     [1, 4, 5, 11]]

        self.puzzles[32].p_pieces = [[2, 5, 9, 11],
                                     [1, 2, 7, 10],
                                     [2, 5, 9, 10],
                                     [0, 7, 10, 11],
                                     [1, 2, 5, 11],
                                     [3, 5, 9, 11]]

        self.puzzles[33].p_pieces = [[0, 4, 5, 10],
                                     [0, 8, 9, 11],
                                     [3, 6, 7, 11],
                                     [0, 1, 2, 10],
                                     [1, 4, 8, 11],
                                     [1, 5, 6, 11]]

        self.puzzles[34].p_pieces = [[3, 6, 10, 11],
                                     [3, 5, 6, 11],
                                     [6, 8, 10, 11],
                                     [2, 4, 8, 11],
                                     [0, 1, 8, 11],
                                     [1, 2, 4, 11]]

        self.puzzles[35].p_pieces = [[0, 1, 5, 11],
                                     [4, 5, 9, 11],
                                     [1, 4, 10, 11],
                                     [3, 4, 10, 11],
                                     [5, 6, 10, 11],
                                     [0, 5, 9, 10]]

    def shufflePuzzles(self):
        np.random.shuffle(self.puzzles)
