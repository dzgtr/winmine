from tkinter import *
from gui_classes.Difficulty import Difficulty

class Variables:
    guess_x = 0
    guess_y = 0
    left_click = True                    # True for left click-guess, False for right click-flag/uncover
    current_difficulty = None
    difficulties = [
            Difficulty("Beginner", 9, 9, 10),
            Difficulty("Intermediate", 16, 16, 40),
            Difficulty("Expert", 16, 30, 99)
        ]