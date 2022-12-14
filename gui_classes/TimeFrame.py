from tkinter import *
from gui_classes.Variables import Variables
from threading import Thread
import time


class TimeFrame(Frame):
    def __init__(self, parentframe, new_game_callback):
        super().__init__()
        self.timeframe = parentframe
        self.new_game_callback = new_game_callback

        self.flagframe = Frame(self.timeframe, width=200, bg="blue")
        self.smileframe = Frame(self.timeframe)
        self.timerframe = Frame(self.timeframe)

    def new_game(self):
        self.flagframe.grid(row=0, columnspan=Variables.difficulties[Variables.current_difficulty].size_x, sticky=W, padx=2)
        self.smileframe.grid(row=0, columnspan=Variables.difficulties[Variables.current_difficulty].size_x)
        self.timerframe.grid(row=0, columnspan=Variables.difficulties[Variables.current_difficulty].size_x, sticky=E, padx=2)
        self.smile()
        self.change_digits(self.timerframe, 0)
        self.timer_control(False)

    def remaining_flags(self, count):
        self.change_digits(self.flagframe, count)
        print(count)

    def smile(self):
        smile = PhotoImage(file="./_img/smile_smile.png")
        self.smile_button = Button(self.smileframe, image=smile, command=self.new_game_callback)
        self.smile_button.photo = smile
        self.smile_button.grid(row=0, columnspan=Variables.difficulties[Variables.current_difficulty].size_x)

    def change_smile_image(self, img):
        smile = PhotoImage(file=f"./_img/smile_{img}.png")
        self.smile_button.photo = smile
        self.smile_button.config(image=smile)

    def timer_control(self, is_running):
        self.thread = Thread(target=self.timer)
        self.thread.daemon = True
        if is_running and not self.thread.is_alive():
            self.timer_is_running = True
            self.thread.start()
        else:
            self.timer_is_running = False

    def timer(self):
        clock = 1
        while clock < 1000:
            if round(clock, 1) % 1 == 0:
                Variables.game_time = int(round(clock))
                self.change_digits(self.timerframe, Variables.game_time)
            if not self.timer_is_running:
                break
            clock += 0.01
            time.sleep(0.01)

    def change_digits(self, frame, number):
        self.digitlist = [Label(frame, bd=0), Label(frame, bd=0), Label(frame, bd=0)]
        if number < -99:
            str_number = "-99"
        elif number in range(-99, 1000):
            str_number = format(number, "03d")
        else:
            str_number = "999"

        for number in range(3):
            img = PhotoImage(file=f"./_img/digit_{str_number[number:number+1]}.png")
            self.digitlist[number].config(image=img)
            self.digitlist[number].photo = img
            self.digitlist[number].grid(row=0, column=number)
