from tkinter import *
from gui_classes.Variables import Variables
import time

class TimeFrame(Frame):
    def __init__(self, parentframe, new_game_callback):
        self.timeframe = parentframe
        self.flagframe = Frame(self.timeframe)
        self.smileframe = Frame(self.timeframe)
        self.timerframe = Frame(self.timeframe)
        self.new_game_callback = new_game_callback
        self.flagframe.grid(row=0, columnspan=Variables.difficulties[Variables.current_difficulty.get()].size_x, sticky=W)
        self.smileframe.grid(row=0, columnspan=Variables.difficulties[Variables.current_difficulty.get()].size_x)
        self.timerframe.grid(row=0, columnspan=Variables.difficulties[Variables.current_difficulty.get()].size_x, sticky=E)


    def new_game(self):
        self.smile()
        self.timer()



    def remaining_flags(self, count):
        self.change_digits(self.flagframe, count)

    def smile(self):
        smile = PhotoImage(file="./_img/smile_smile.png")
        self.smile_button = Button(self.smileframe, image=smile, command=self.new_game_callback)
        self.smile_button.photo = smile
        self.smile_button.grid(row=0, columnspan=Variables.difficulties[Variables.current_difficulty.get()].size_x)

    def change_smile_image(self, img):
        smile = PhotoImage(file=f"./_img/smile_{img}.png")
        self.smile_button.photo = smile
        self.smile_button.config(image=smile)

    def timer(self):
        clock = 0
        self.change_digits(self.timerframe, clock) # 6 for column 6, starting for beginner mines timer
        time.sleep(0)

    def change_digits(self, frame, number):
        digitlist = []
        if number < -99:
            str_number = "-99"
        elif number in range(-99,1000):
            str_number = format(number, "03d")
        else:
            str_number = "999"

        for number in range(3):
            img = PhotoImage(file=f"./_img/scaled/digit_{str_number[number:number+1]}.png")
            digitlist.append(Label(frame, image=img))
            digitlist[number].photo = img
            digitlist[number].grid(row=0, column=number)