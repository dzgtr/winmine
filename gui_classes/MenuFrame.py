from tkinter import *

from gui_classes.AboutWindow import AboutWindow
from gui_classes.CustomDifficultyWindow import CustomDifficultyWindow
from gui_classes.HighscoreWindow import HighscoreWindow
from gui_classes.Variables import Variables
from gui_classes.Difficulty import Difficulty


class MenuFrame(Frame):
    def __init__(self, menuframe, new_game_callback):
        super().__init__()
        self.menuframe = menuframe
        menu = Menu(self.menuframe)
        self.menuframe.config(menu=menu)
        self.new_game = new_game_callback
        self.diff_selector = IntVar(None, 0)

        game_menu = Menu(menu, tearoff=0)
        game_menu.add_command(label="New", command=self.new_game)
        game_menu.add_separator()
        for diff_number in range(3):
            game_menu.add_radiobutton(label=Variables.difficulties[diff_number].name, value=diff_number, variable=self.diff_selector, command=self.change_difficulty)
        game_menu.add_radiobutton(label="Custom...", value=3, variable=self.diff_selector, command=self.custom)
        game_menu.add_separator()
        game_menu.add_command(label="Best Times...", command=HighscoreWindow)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.exit_program)
        menu.add_cascade(label="File", menu=game_menu)

        about_menu = Menu(menu, tearoff=0)
        about_menu.add_command(label="About", command=self.about)
        menu.add_cascade(label="About", menu=about_menu)

    def exit_program(self):
        exit()

    def about(self):
        AboutWindow()

    def custom(self):
        Variables.difficulties.append(Difficulty("Custom", Variables.difficulties[Variables.current_difficulty].size_y,
                                                 Variables.difficulties[Variables.current_difficulty].size_x,
                                                 Variables.difficulties[Variables.current_difficulty].minecount))
        previous_difficulty = Variables.current_difficulty
        Variables.current_difficulty = self.diff_selector.get()
        CustomDifficultyWindow(self.new_game, previous_difficulty)

    def change_difficulty(self):
        Variables.current_difficulty = self.diff_selector.get()
        self.new_game()