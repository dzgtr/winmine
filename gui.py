import classes
import tkinter.ttk
from tkinter import *
import tkinter.messagebox
from gui_classes.MainWindow import MainWindow
from gui_classes.Variables import Variables
from gui_classes.Difficulty import Difficulty

root = Tk()
main = MainWindow(root)
#board = classes.Board(row_count, col_count, minecount)
#board.create_board()
#board.plant_on_board()

root.wm_title("Minesweeper")
root.mainloop()