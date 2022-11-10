from tkinter import Tk, Canvas, Label, Button, Frame, messagebox
from PIL import Image, ImageTk
from params import *
from Board import *
from Cell import *
from Chip import *


def close_game():
    if messagebox.askokcancel("Quit the game", "Are you sure to leave the game?"):
        tk.destroy()


# Graphic
tk = Tk()
tk.resizable(width=False, height=False)
tk.title("Sliding puzzle mini-game")
tk.protocol("WM_DELETE_WINDOW", close_game)
# tk.wm_attributes('-transparentcolor', '#AD999E')
image = Image.open("board_bg.PNG")
width = int(2.3 * BOARD_SIZE * BLOCK_SIZE)
ratio = (width / float(image.size[0]))
height = int((float(image.size[1]) * float(ratio)))
image = image.resize((width, height), Image.Resampling.LANCZOS)
image = ImageTk.PhotoImage(image)
panel = Label(tk, image=image)
panel.pack(side="top", fill="both", expand=0)
tk.update_idletasks()
top_panel = Canvas(tk, width=BOARD_SIZE * BLOCK_SIZE, height=BLOCK_SIZE / 1.4, bg="#d19020", relief="sunken",
                   highlightthickness=0)
top_panel.create_oval(20, 10, 60, 50, fill="#e62413", width=2, outline="#76553d")
top_panel.create_oval(180, 10, 220, 50, fill="#d7c817", width=2, outline="#76553d")
top_panel.create_oval(340, 10, 380, 50, fill="#3334b6", width=2, outline="#76553d")
top_panel.place(relx=.5, rely=.1, anchor="center")
board_frame = Frame(tk, width=BOARD_SIZE * BLOCK_SIZE, height=BOARD_SIZE * BLOCK_SIZE)
canvas = Canvas(board_frame, width=BOARD_SIZE * BLOCK_SIZE, height=BOARD_SIZE * BLOCK_SIZE, relief="raised",
                highlightbackground='#201309', highlightthickness=2)
canvas.pack(side="left")
board_frame.place(relx=.5, rely=.5, anchor="center")


# Main
def main():
    board = Board(canvas)
    board.draw()
    restart_btn = Button(tk, text="Skip puzzle and restart", bg="black", fg="#d19020",
                         font=("Comic Sans MS", 16, 'bold'), command=board.restart)
    restart_btn.place(relx=.5, rely=0.97, anchor='s')
    tk.mainloop()


if __name__ == "__main__":
    main()
