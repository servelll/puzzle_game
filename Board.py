from Cell import *
from Chip import *
from random import sample
from tkinter import Canvas
from params import *


class Board:
    def __init__(self, canvas):
        self.cells = [[] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.canvas = canvas
        self.is_victory = 0
        for i in range(BOARD_SIZE):
            row = []
            for j in range(BOARD_SIZE):
                if not (j % 2):
                    row.append(Cell(i, j, None, self))
                elif i % 2:
                    row.append(Cell(i, j, None, self))
                else:
                    row.append(Cell(i, j, None, self))
                    Chip("block", row[j])
            self.cells[i] = row

    def draw(self):
        for row in self.cells:
            for el in row:
                self.canvas.create_rectangle(el.y * BLOCK_SIZE, el.x * BLOCK_SIZE, (el.y + 1) * BLOCK_SIZE,
                                             (el.x + 1) * BLOCK_SIZE, fill='gray25', stipple='gray25')
                if hasattr(el.chip, 'type') and el.chip.type == "block":
                    self.canvas.create_rectangle(el.y * BLOCK_SIZE, el.x * BLOCK_SIZE, (el.y + 1) * BLOCK_SIZE,
                                                 (el.x + 1) * BLOCK_SIZE, fill="#6c7572")
        self.add_chips()

    def get_cell(self, x, y):
        return self.cells[y][x]

    def add_chips(self):
        rand_chips = sample(chips, counts=[5, 5, 5], k=15)
        for i in range(0, BOARD_SIZE, 2):
            for j in range(BOARD_SIZE):
                temp_color = rand_chips.pop()
                chip_canvas = Canvas(self.canvas, width=BLOCK_SIZE, height=BLOCK_SIZE, name=f"a{i}{j}", relief="sunken",
                                     highlightthickness=0)
                chip_id = chip_canvas.create_rectangle(0, 0, BLOCK_SIZE, BLOCK_SIZE, fill=temp_color, width=2)
                chip_canvas.place(x=i * BLOCK_SIZE, y=j * BLOCK_SIZE)
                Chip(temp_color, self.get_cell(i, j))
                chip_canvas.tag_bind(chip_id, '<B1-Motion>', self.get_cell(i, j).chip.drag)
                chip_canvas.tag_bind(chip_id, '<ButtonRelease-1>', self.get_cell(i, j).chip.move_figure)

    def delete_chips(self):
        for child in self.canvas.place_slaves():
            child.destroy()

    def absolute_coordinates(self):
        mx = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        my = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
        if mx < BLOCK_SIZE / 2:
            mx = BLOCK_SIZE / 2
        if mx > board_width - BLOCK_SIZE / 2:
            mx = board_width - BLOCK_SIZE / 2
        if my < BLOCK_SIZE / 2:
            my = BLOCK_SIZE / 2
        if my > board_width - BLOCK_SIZE / 2:
            my = board_width - BLOCK_SIZE / 2
        return mx, my

    def restart(self):
        self.delete_chips()
        self = Board(self.canvas)
        self.add_chips()

    def check_victory(self):
        for row in self.cells:
            if [cell.chip.type for cell in row[::2] if cell.chip] != chips:
                break
        else:
            victory_canvas = Canvas(self.canvas, width=3 * BLOCK_SIZE, height=BLOCK_SIZE, relief="raised", bg="#aacc88",
                                    highlightbackground='#201309', highlightthickness=0)
            victory_canvas.create_text(3 * BLOCK_SIZE // 2, BLOCK_SIZE // 2, text="VICTORY",
                                       font=("Comic Sans MS", 25, 'bold'), fill="#12364a")
            victory_canvas.place(relx=.5, rely=.5, anchor="center")
            self.is_victory = 1
