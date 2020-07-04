from Table import Table
from Player import Player

class PlayerHuman(Player):
    def chooseRow(self, table: Table):
        for i in range(0, 11, 2):
            if table.gems_pos[i, self.pos] > 0:
                self.gems[table.gems_pos[i, self.pos] - 1] += 1
                self.gems[table.gems_pos[i + 1, self.pos] - 1] += 1
                table.gems_pos[i, self.pos] = table.gems_pos[i + 1, self.pos] = 0
                return
