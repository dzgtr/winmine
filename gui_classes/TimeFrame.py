from tkinter import *
import time

class TimeFrame(Frame):
    def __init__(self, timeframe, new_game_callback):
        Frame.__init__(self, timeframe)
        self.timeframe = timeframe
        self.tmrlblb = Label(timeframe)
        self.new_game_callback = new_game_callback
        self.smile()
        timeframe.grid()
        self.timer()

    def remaining_flags(self, count):
        self.change_digits(0, count)

    def smile(self):
        smile = PhotoImage(file="./_img/smile_smile.png")
        self.smile_button = Button(self.timeframe, image=smile, command=self.new_game_callback)
        self.smile_button.photo = smile
        self.smile_button.grid(row=0, columnspan=9)

    def change_smile_image(self, img):
        smile = PhotoImage(file=f"./_img/smile_{img}.png")
        self.smile_button.photo = smile
        self.smile_button.config(image=smile)

    def timer(self):
        clock = 0
        self.change_digits(6, clock) # 6 for column 6, starting for beginner mines timer
        time.sleep(0)

    def change_digits(self, column_count, number):
        digits = []
        if number < -99:
            str_number = "-99"
        elif number in range(-99,1000):
            str_number = format(number, "03d")
        else:
            str_number = "999"

        for number in range(3):
            img = PhotoImage(file=f"./_img/scaled/digit_{str_number[number:number+1]}.png")
            digits.append(Label(self.timeframe, image=img))
            digits[number].photo = img
            digits[number].grid(row=0, column=column_count+number)