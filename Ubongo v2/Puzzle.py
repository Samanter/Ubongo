import numpy as np


class Puzzle:
    def __init__(self):
        self.form = np.zeros((6, 6), dtype=int)
        self.p_pieces = np.zeros((6, 4), dtype=int)
