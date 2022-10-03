import classes
import tkinter.ttk
from tkinter import *
import tkinter.messagebox
from gui_classes.MenuFrame import MenuFrame
from gui_classes.TimeFrame import TimeFrame
from gui_classes.GameFrame import GameFrame
from gui_classes.Variables import Variables
from gui_classes.Difficulty import Difficulty
from gui_classes.ImageButton import ImageButton

root = Tk()

menuframe = MenuFrame(root)
timeframe = TimeFrame(root)
gameframe = GameFrame(root)
root.geometry("600x500")
root.wm_title("Minesweeper")
root.mainloop()