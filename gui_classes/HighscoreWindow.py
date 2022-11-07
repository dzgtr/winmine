from tkinter import *
import json


class HighscoreWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.wm_title("Fastest Mine Sweepers")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.print_scores()

        reset_button = Button(self, text="Reset Scores", command=self.reset_scores)
        reset_button.grid(row=4, column=0, columnspan=2, pady=10)
        reset_button = Button(self, text="OK", command=self.destroy)
        reset_button.grid(row=4, column=2, pady=10, sticky=W)

    def print_scores(self):
        with open("highscores.json", "r", encoding="utf-8") as json_file:
            highscores = json.load(json_file)

        padding = Label(self)
        padding.grid(row=0)
        row = 1
        for key in highscores:
            difficulty = Label(self, text=f"{key}:")
            difficulty.grid(sticky=W, row=row, column=0, padx=(15, 10))
            score = Label(self, text=f"{highscores[key][0]} seconds")
            score.grid(sticky=W, row=row, column=1, padx=10)
            name = Label(self, text=highscores[key][1])
            name.grid(sticky=W, row=row, column=2, padx=(10, 15))
            row += 1

    def reset_scores(self):
        print("reset")
        reset_scores = {
            "Beginner": [999, "Anonymous"],
            "Intermediate": [999, "Anonymous"],
            "Expert": [999, "Anonymous"]
        }

        with open("highscores.json", "w", encoding="utf-8") as json_file:
            json.dump(reset_scores, json_file, indent=4, ensure_ascii=False)
        self.print_scores()
