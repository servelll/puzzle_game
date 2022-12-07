class Cell:
    def __init__(self, x, y, chip, board):
        self.x = x
        self.y = y
        self.chip = chip
        self.board = board

    def __repr__(self):
        return "<Cell x:%d y:%d chip:%s>" % (self.x, self.y, self.chip)

    def __str__(self):
        return "Cell: x is %d, y is %d, chip is %s>" % (self.x, self.y, self.chip)

    def set_chip(self, chip):
        chip.cell.chip = None
        self.chip = chip
        chip.cell = self
