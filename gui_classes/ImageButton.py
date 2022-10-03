from tkinter import *
import os

class ImageButton(Button):
    def __init__(self, button_frame, img_name, row, column):
        Frame.__init__(self, button_frame)
        self.button_frame = button_frame
        self.img_name = img_name

        image = PhotoImage(file=f"./_img/{img_name}.png")
        field = Button(self.button_frame, image=image)
        field.photo = image
        field.grid(row=row+1, column=column)