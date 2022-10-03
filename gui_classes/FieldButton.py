from tkinter import *
from classes import Board

class FieldButton:
    def __init__(self, pos_y, pos_x, current_image):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.current_image = current_image
        self.field_button = Label(game_frame, image=self.current_image)
        self.field_button.bind("<Button-1>", Board.guess(pos_x, pos_y))
        self.field_button.bind("<Button-3>", Board.flag_uncover(pos_x, pos_y))
        #self.field_button.pack()