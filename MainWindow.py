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
        self.menuframe = MenuFrame(self, self.new_game)
        self.timeframe = TimeFrame(self, self.new_game)
        self.gameframe = GameFrame(self, self.change_smile)
        self.geometry("350x415")
        self.wm_title("Minesweeper")
        self.mainloop()

    def new_game(self):
        self.gameframe.new_game()

    def change_smile(self, img):
        self.timeframe.change_smile_image(img)
