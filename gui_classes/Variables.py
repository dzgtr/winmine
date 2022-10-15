from tkinter import *
from gui_classes.Difficulty import Difficulty

class Variables:
    guess_x = 0
    guess_y = 0
    flagcount_or_boomcords = None
    remaining = 0
    current_difficulty = None
    difficulties = [
            Difficulty("Beginner", 9, 9, 10),
            Difficulty("Intermediate", 16, 16, 40),
            Difficulty("Expert", 16, 30, 99)
        ]