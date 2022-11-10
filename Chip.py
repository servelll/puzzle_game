from tkinter import Misc
from params import *


class Chip:
    def __init__(self, color, cell):
        self.type = color
        self.cell = cell
        self.cell.chip = self

    def __repr__(self):
        return "<Chip type:%s, cell x:%d, y:%d>" % (self.type, self.cell.x, self.cell.y)

    def __str__(self):
        return "Chip: type is %s, cell: x is %d, y is %d>" % (self.type, self.cell.x, self.cell.y)

    def drag(self, e):
        Misc.lift(e.widget)
        mx, my = self.cell.board.absolute_coordinates()
        e.widget.place(x=mx, y=my, anchor='center')

    def can_move(self, target):
        if target.chip or self.cell.board.is_victory:
            return False
        if self.cell.x - target.x == 0:
            i = abs(target.y - self.cell.y) // (target.y - self.cell.y)
            for cell in self.cell.board.cells[target.x][self.cell.y + i: target.y: i]:
                if cell.chip:
                    return False
            return True
        if self.cell.y - target.y == 0:
            d = target.x - self.cell.x
            sign = int(abs(d) / d)
            for i in range(1, abs(d)):
                if self.cell.board.get_cell(target.y, self.cell.x + i * sign).chip:
                    return False
            return True

    def move_figure(self, e):
        mx, my = self.cell.board.absolute_coordinates()
        target = self.cell.board.get_cell(int(mx // BLOCK_SIZE), int(my // BLOCK_SIZE))
        if self.type and self.can_move(target):
            target.set_chip(self)
            e.widget.place(x=BLOCK_SIZE / 2 + mx // BLOCK_SIZE * BLOCK_SIZE,
                           y=BLOCK_SIZE / 2 + my // BLOCK_SIZE * BLOCK_SIZE, anchor='center')
            self.cell.board.check_victory()
        else:
            e.widget.place(x=BLOCK_SIZE / 2 + self.cell.y * BLOCK_SIZE,
                           y=BLOCK_SIZE / 2 + self.cell.x * BLOCK_SIZE, anchor='center')
