import tkinter
from tkinter import *

class TimeFrame(Frame):
    def __init__(self, timeframe):
        Frame.__init__(self, timeframe)
        self.timeframe = timeframe

        smile = PhotoImage(file="./_img/smile_smile.png")
        newgame_button = Button(timeframe, image=smile)
        newgame_button.photo = smile
        newgame_button.grid(columnspan=9)
        timeframe.grid()