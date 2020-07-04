import numpy as np

class Table:
    def __init__(self):
        self.gems_pos = np.zeros([12, 6])
        self.n_players = 4

    def generateTable(self):
        gems = np.array([1, 2, 3, 4])
        gems = np.tile(gems, 18)
        np.random.shuffle(gems)
        gems = gems.reshape(12, 6)
        self.gems_pos = gems.copy()
