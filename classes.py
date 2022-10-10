import random
from gui_classes.Variables import Variables

class Field:
    def __init__(self):
        self.ismine = False
        self.isflagged = False
        self.isclicked = False
        self.neighmine = 0

class Board:
    def __init__(self, size_x, size_y, minecount):
        self.gameboard = []
        self.size_x = size_x
        self.size_y = size_y
        self.minecount = minecount
        self.remaining = (size_x*size_y)-minecount

    def create_board(self):
        for y in range(self.size_y):
            self.gameboard.append([])
            for x in range(self.size_x):
                self.gameboard[y].append(Field())

    def plant_on_board(self):
        planted_minecount = 0
        while planted_minecount < self.minecount:
            random_row = random.randint(0, self.size_y - 1)
            random_col = random.randint(0, self.size_x - 1)
            if not self.gameboard[random_row][random_col].ismine:
                self.gameboard[random_row][random_col].ismine = True
                planted_minecount += 1

    def print_board(self):
        for x in range(len(self.gameboard)):
            for y in range(len(self.gameboard[x])):
                if self.gameboard[x][y].isclicked and not self.gameboard[x][y].ismine:
                    print(self.gameboard[x][y].neighmine, end=" ")
                elif self.gameboard[x][y].isclicked and self.gameboard[x][y].ismine:
                    print("X", end=" ")
                elif self.gameboard[x][y].isflagged:
                    print("F", end=" ")
                else:
                    print("#", end=" ")
            print("")

    def neigh_mine_count(self, guess_x, guess_y):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if guess_x + x in range(0, self.size_y) and guess_y + y in range(0, self.size_x):
                    if self.gameboard[guess_x + x][guess_y + y].ismine and not self.gameboard[guess_x][guess_y].isclicked:
                        self.gameboard[guess_x][guess_y].neighmine += 1
        if not self.gameboard[guess_x][guess_y].isclicked:
            self.gameboard[guess_x][guess_y].isclicked = True
            self.remaining -=1

        if self.gameboard[guess_x][guess_y].neighmine == 0:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if guess_x + x in range(0, self.size_y) and guess_y + y in range(0, self.size_x):
                        if not self.gameboard[guess_x+x][guess_y+y].isclicked:
                            Board.neigh_mine_count(self, guess_x+x, guess_y+y)

    def print_board_test(self):
        for x in range(len(self.gameboard)):
            for y in range(len(self.gameboard[x])):
                print(self.gameboard[x][y].ismine, end=" ")
            print("")

# here will be fast uncover function when you click on already clicked but solved field
    def flag_uncover(self, guess_x, guess_y):
        if self.gameboard[guess_x][guess_y].isflagged:
            self.gameboard[guess_x][guess_y].isflagged = False
        elif not self.gameboard[guess_x][guess_y].isclicked:
            print("Field flagged")
            self.gameboard[guess_x][guess_y].isflagged = True
        else:
            self.range_flagcount = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if guess_x + x in range(0, self.size_x) and guess_y + y in range(0, self.size_y):
                        if self.gameboard[guess_x+x][guess_y+y].isflagged:
                            self.range_flagcount +=1
            if self.gameboard[guess_x][guess_y].neighmine != self.range_flagcount:
                print("Flag count and neighbour mine count doesn't match")
            else:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if guess_x + x in range(0, self.size_x) and guess_y + y in range(0, self.size_y):
                            if not self.gameboard[guess_x+x][guess_y+y].isflagged and not self.gameboard[guess_x+x][guess_y+y].ismine:
                                Board.neigh_mine_count(self, guess_x+x, guess_y+y)
                            elif not self.gameboard[guess_x+x][guess_y+y].isflagged and self.gameboard[guess_x+x][guess_y+y].ismine:
                                self.gameboard[guess_x+x][guess_y+y].isclicked = True
                                print("You Lost!")
                                Variables.lost_x = guess_y + y
                                Variables.lost_y = guess_x + x
                                return True

    def guess(self, guess_x, guess_y):
        if self.gameboard[guess_x][guess_y].ismine and not self.gameboard[guess_x][guess_y].isflagged:
            self.gameboard[guess_x][guess_y].isclicked = True
            print("You Lost!")
            return True
        elif self.gameboard[guess_x][guess_y].isclicked:
            print("Already clicked here")
        elif self.gameboard[guess_x][guess_y].isflagged:
            print("Can't click a flagged field")
        else:
            print("Miss")
            Board.neigh_mine_count(self, guess_x, guess_y)

    def is_over(self):
        if self.remaining == 0:
            isover = True
        else:
            isover = False
        return isover
