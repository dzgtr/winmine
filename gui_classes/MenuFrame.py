from tkinter import *

from gui_classes.Difficulty import Difficulty
from gui_classes.Variables import Variables
from gui_classes.FieldButton import FieldButton
from gui_classes.GuiBoard import GuiBoard
from gui_classes.AboutWindow import AboutWindow
from gui_classes.OptionsWindow import OptionsWindow

class MenuFrame(Frame):
    def __init__(self, menuframe):
        Frame.__init__(self, menuframe)
        self.menuframe = menuframe
        menu = Menu(self.menuframe)
        self.menuframe.config(menu=menu)

        game_menu = Menu(menu, tearoff=0)
        game_menu.add_command(label="New Game")
        game_menu.add_command(label="Options", command=self.options)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=game_menu)

        about_menu = Menu(menu, tearoff=0)
        about_menu.add_command(label="About", command=self.about)
        menu.add_cascade(label="About", menu=about_menu)
        Variables.current_difficulty = IntVar(None, 0) # sets current difficulty to beginner
        game_frame = GuiBoard(Variables.difficulties[Variables.current_difficulty.get()].size_y, Variables.difficulties[Variables.current_difficulty.get()].size_x)

    def exitProgram(self):
        exit()

    def about(self):
        AboutWindow()

    def options(self):
        OptionsWindow()
