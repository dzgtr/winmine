from tkinter import *
import classes
from gui_classes.GameFrame import GameFrame

class ImageButton(Button):
    def __init__(self, button_frame, img_name, row, column, board):
#        Frame.__init__(self, button_frame)
        self.button_frame = button_frame
        self.img_name = img_name
        self.board = board
        self.row = row
        self.column = column

        image = PhotoImage(file=f"./_img/{img_name}.png")
        field = Button(self.button_frame, image=image)
        field.photo = image
        field.bind("<Button-1>", self.button_l_click)
        field.bind("<Button-3>", self.button_r_click)
        field.grid(row=row+1, column=column)

    def button_l_click(self, event):
        self.board.guess(self.row, self.column)
        GameFrame.print_gui_board()
    def button_r_click(self, event):
        pass