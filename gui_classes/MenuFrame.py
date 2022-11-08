from tkinter import *

from gui_classes.AboutWindow import AboutWindow
from gui_classes.CustomDifficultyWindow import CustomDifficultyWindow
from gui_classes.HighscoreWindow import HighscoreWindow
from gui_classes.Variables import Variables


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
        game_menu.add_checkbutton(label="Custom...", variable=self.diff_selector, command=self.options)
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

    def options(self):
        CustomDifficultyWindow(self.new_game)

    def change_difficulty(self):
        Variables.current_difficulty = self.diff_selector.get()
        self.new_game()