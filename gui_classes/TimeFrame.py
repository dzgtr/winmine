import tkinter
from tkinter import *

class TimeFrame(Frame):
    def __init__(self, timeframe, new_game_callback):
        Frame.__init__(self, timeframe)
        self.timeframe = timeframe
        self.new_game_callback = new_game_callback

        smile = PhotoImage(file="./_img/smile_smile.png")
        self.smile_button = Button(timeframe, image=smile, command=self.new_game_callback)
        self.smile_button.photo = smile
        self.smile_button.grid(columnspan=9)
        timeframe.grid()
        
    def change_smile_image(self, img):
        self.img = img
        smile = PhotoImage(file=f"./_img/smile_{self.img}.png")
        self.smile_button.photo = smile
        self.smile_button.config(image=smile)