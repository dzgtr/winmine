import classes
import tkinter.ttk
from tkinter import *
import tkinter.messagebox
from gui_classes.MenuFrame import MenuFrame
from gui_classes.TimeFrame import TimeFrame
from gui_classes.GameFrame import GameFrame


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.menuframe = MenuFrame(self)
        self.timeframe = TimeFrame(self)
        self.gameframe = GameFrame(self)
        self.geometry("350x415")
        self.wm_title("Minesweeper")
        self.mainloop()