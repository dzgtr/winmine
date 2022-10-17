from tkinter import *

from gui_classes.Difficulty import Difficulty
from gui_classes.Variables import Variables
from gui_classes.AboutWindow import AboutWindow
from gui_classes.OptionsWindow import OptionsWindow


class MenuFrame(Frame):
    def __init__(self, menuframe, new_game_callback):
        self.menuframe = menuframe
        menu = Menu(self.menuframe)
        self.menuframe.config(menu=menu)
        self.new_game = new_game_callback

        game_menu = Menu(menu, tearoff=0)
        game_menu.add_command(label="New Game", command=self.new_game)
        game_menu.add_command(label="Options", command=self.options)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=game_menu)

        about_menu = Menu(menu, tearoff=0)
        about_menu.add_command(label="About", command=self.about)
        menu.add_cascade(label="About", menu=about_menu)

    def exitProgram(self):
        exit()

    def about(self):
        AboutWindow()

    def options(self):
        OptionsWindow(self.new_game)
