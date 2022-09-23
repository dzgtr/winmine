import classes
import tkinter.ttk
from tkinter import *
import tkinter.messagebox
from gui_classes.MenuFrame import MenuFrame
from gui_classes.TimeFrame import TimeFrame
from gui_classes.GameFrame import GameFrame
from gui_classes.Variables import Variables
from gui_classes.Difficulty import Difficulty

root = Tk()

menuframe = MenuFrame(root)
#board = classes.Board(row_count, col_count, minecount)
#board.create_board()
#board.plant_on_board()
timeframe = TimeFrame(root)
timeframe.pack()
gameframe = GameFrame(root)
gameframe.pack()
root.geometry("400x300")
root.wm_title("Minesweeper")
root.mainloop()