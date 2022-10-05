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

class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.menuframe = MenuFrame(self)
        self.timeframe = TimeFrame(self)
        self.gameframe = GameFrame(self)
        self.geometry("600x500")
        self.wm_title("Minesweeper")
        self.mainloop()