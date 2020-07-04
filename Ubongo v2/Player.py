import numpy as np

class Player:
    def __init__(self):
        self.gems = np.zeros(4, dtype=int)
        self.piece_time = np.zeros(4, dtype=int)
        self.sols = np.full((4, 6, 6), -1, dtype=int)
        self.pieces_on = np.array([], dtype=int)
        self.pos = -1
        self.turn_place = -1
        self.game_place = -1
        self.playing = True
        self.solved = False
        self.solving_puzzle = np.full((6, 6), -1, dtype=int)

    def resetGems(self):
        self.gems *= 0
