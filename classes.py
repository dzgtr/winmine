import random


class Field:
    def __init__(self):
        self.isMine = False
        self.isFlagged = False
        self.isClicked = False

class Board:
    def __init__(self, size_x, size_y, minecount):
        self.gameboard = []
        self.size_x = size_x
        self.size_y = size_y
        self.minecount = minecount

    def create_board(self):
        for x in range(self.size_y):
            self.gameboard.append([])
            for y in range(self.size_x):
                self.gameboard[x].append(Field())

    def plant_on_board(self):
        planted_minecount = 0
        while planted_minecount < self.minecount:
            random_row = random.randint(0, self.size_y - 1)
            random_col = random.randint(0, self.size_x - 1)
            if self.gameboard[random_row][random_col].isMine == False:
                self.gameboard[random_row][random_col].isMine = True
                planted_minecount += 1

    def print_board(self):
        for x in range(len(self.gameboard)):
            for y in range(len(self.gameboard[x])):
                print(self.gameboard[x][y].isMine, end=" ")
            print("")

    def guess(self, guess_x, guess_y):
        if self.gameboard[guess_x][guess_y].isMine == True:
            print("You Lost!")
            return True
        elif self.gameboard[guess_x][guess_y].isClicked == True:
            print("Already clicked here")
        else:
            print("Miss")
            self.gameboard[guess_x][guess_y].isClicked = True

    def is_over(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.gameboard[x][y].isMine or self.gameboard[x][y].isClicked:
                    isover = True
                else:
                    isover = False
                    break
        return isover
