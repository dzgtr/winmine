import classes
import gui_classes
import tkinter.ttk
from tkinter import *
import tkinter.messagebox

difficulties = {
    "Beginner": [9, 9, 10],
    "Intermediate": [16, 16, 40],
    "Expert": [16, 30, 99],
    "Custom": [0, 0, 0]
}

root = Tk()
app = gui_classes.MainWindow(root)
#board = classes.Board(row_count, col_count, minecount)
#board.create_board()
#board.plant_on_board()


root.wm_title("Minesweeper")
root.mainloop()