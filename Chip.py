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

        m = self.cell.board.get_cell(self.cell.y - 1 if target.y < self.cell.y else
                                     (self.cell.y + 1 if self.cell.y < 4 else self.cell.y), self.cell.x)
        n = self.cell.board.get_cell(self.cell.y, self.cell.x - 1 if target.x < self.cell.x else
                                     (self.cell.x + 1 if self.cell.x < 4 else self.cell.x))
        c = [i for i in (m, n) if not i.chip]
        if not c:
            if self.cell.x:
                c.append(self.cell.board.get_cell(self.cell.y, self.cell.x - 1))
            if self.cell.y:
                c.append(self.cell.board.get_cell(self.cell.y - 1, self.cell.x))

        for choice in c:
            d_x = target.x - choice.x
            d_y = target.y - choice.y
            sign_x = int(abs(d_x) / d_x) if d_x != 0 else 0
            sign_y = int(abs(d_y) / d_y) if d_y != 0 else 0
            for i in range(1, abs(d_x) + 1):
                if self.cell.board.get_cell(choice.y, choice.x + i * sign_x).chip:
                    break
            else:
                for i in range(1, abs(d_y)):
                    if self.cell.board.get_cell(choice.y + i * sign_y, target.x).chip:
                        break
                else:
                    return True
            for i in range(1, abs(d_y) + 1):
                if self.cell.board.get_cell(choice.y + i * sign_y, choice.x).chip:
                    break
            else:
                for i in range(1, abs(d_x)):
                    if self.cell.board.get_cell(target.y, choice.x + i * sign_x).chip:
                        break
                else:
                    return True
        return False

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
