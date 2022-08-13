import tkinter.ttk
from tkinter import *
import random

board_width = 2
board_height = 2
minecount = 2
brake = 0
board = []

for x in range(board_height):
    board.append([])
    for y in range(board_width):
        board[x].append(0)

for x in range(len(board)):
    print(board[x])

planted_minecount = 0

while planted_minecount < minecount:
    random_row = random.randint(0, board_height-1)
    random_col = random.randint(0, board_width-1)
    if board[random_row][random_col] == 0:
        board[random_row][random_col] = 1
        planted_minecount += 1

print(planted_minecount)

def printboard(hraci_plocha):
    for x in range(len(hraci_plocha)):
        print(hraci_plocha[x])


def guess(board,x,y,brake):
    if board[x][y] == 1:
        print("You Lost!")
        brake = 1
        return brake
    elif board[x][y] == 2:
        print("Already clicked here")
    else:
        #zmenit tlacitko na prokliknuty
        print("Miss")
        board[x][y] = 2

def is_over(board):
    isover = True
    for y in range(board_height):
        for x in range(board_width):
            if board[x][y] == 0:
                isover = False
    return isover


while True:
    printboard(board)
    if guess(board, int(input("Zadej řádek:")), int(input("Zadej sloupec:")), brake) == True:
        break
    if is_over(board) == True:
        print("You won!!!")
        break

"""
class field:
    def _init_(self, row, col):
        self.row = row
        self.col = col

    def isFlagged(self):

    def isClicked(self):

    def isMine(self):


field(0, 0)
"""