from tkinter import *
import FieldButton

class GuiBoard:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.gui_board = []

    def create_board(self):
        for y in range(self.size_y):
            self.gui_board.append([])
            for x in range(self.size_x):
                self.gui_board[y].append(FieldButton())

    def print_board(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.gui_board[y][x].pack()