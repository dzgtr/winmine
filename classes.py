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
                self.gameboard[x].append(0)

    def plant_on_board(self):
        planted_minecount = 0
        while planted_minecount < self.minecount:
            random_row = random.randint(0, self.size_y - 1)
            random_col = random.randint(0, self.size_x - 1)
            if self.gameboard[random_row][random_col] == 0:
                self.gameboard[random_row][random_col] = 1
                planted_minecount += 1

    def print_board(self):
        for x in range(len(self.gameboard)):
            print(self.gameboard[x])

    def guess(self, guess_x, guess_y):
        if self.gameboard[guess_x][guess_y] == 1:
            print("You Lost!")
            return True
        elif self.gameboard[guess_x][guess_y] == 2:
            print("Already clicked here")
        else:
            print("Miss")
            self.gameboard[guess_x][guess_y] = 2

    def is_over(self):
        isover = True
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.gameboard[x][y] == 0:
                    isover = False
                    break
        return isover
