import classes
import tkinter.ttk
from tkinter import *
import tkinter.messagebox
from gui_classes.MenuFrame import MenuFrame
from gui_classes.TimeFrame import TimeFrame
from gui_classes.GameFrame import GameFrame


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.menuframe = MenuFrame(self, self.new_game)
        self.timeframe = TimeFrame(self, self.new_game)
        self.gameframe = GameFrame(self, self.change_smile, self.remaining_flags, self.timer_control)

        self.new_game()
        self.wm_title("Minesweeper")
        self.resizable(False, False)

    def new_game(self):
        self.gameframe.new_game()
        self.timeframe.new_game()


    def change_smile(self, img):
        self.timeframe.change_smile_image(img)

    def remaining_flags(self, count):
        self.timeframe.remaining_flags(count)

    def timer_control(self, is_running):
        self.timeframe.timer_control(is_running)