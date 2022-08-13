import tkinter.ttk
from tkinter import *
import random

class field:
    def __init__(self):
        self.isMine = False
        self.isFlagged = False
        self.isClicked = False

class board:
    def __init__(self, size_x, size_y, minecount):
        self.size_x = size_x
        self.size_y = size_y
        self.minecount = minecount

    def create_board(self):
        for x in range(self.size_y):
            self.append([])
            for y in range(self.size_x):
                self[x].append(field)

    def plant_on_board(self):
        planted_minecount = 0
        while planted_minecount < self.minecount:
            random_row = random.randint(0, self.size_y - 1)
            random_col = random.randint(0, self.size_x - 1)
            if self[random_row][random_col] == 0:
               self[random_row][random_col] = 1
               planted_minecount += 1

    def print_board(self):
        for x in range(len(self)):
            print(self[x])

    def guess(self, guess_x, guess_y):
        if self[guess_x][guess_y] == 1:
            print("You Lost!")
            return False
        elif self[guess_x][guess_y] == 2:
            print("Already clicked here")
        else:
            # zmenit tlacitko na prokliknuty
            print("Miss")
            self[guess_x][guess_y] = 2

    def is_over(self):
        isover = True
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self[x][y] == 0:
                    isover = False
        return isover

while True:
    print_board(board)
    if guess(board, int(input("Zadej řádek:")), int(input("Zadej sloupec:"))) == True:
        break
    if is_over(board) == True:
        print("You won!!!")
        break