import random
from gui_classes.Variables import Variables


class Field:
    def __init__(self):
        self.ismine = False
        self.isflagged = False
        self.isclicked = False
        self.neighmine = 0


class Board:
    def __init__(self, size_y, size_x, minecount):
        self.gameboard = []
        self.size_y = size_y
        self.size_x = size_x
        self.minecount = minecount
        self.remaining_fields = (size_y*size_x)-minecount
        self.remaining_flags = minecount
        self.firstclick = True

    def create_board(self):
        for y in range(self.size_y):
            self.gameboard.append([])
            for x in range(self.size_x):
                self.gameboard[y].append(Field())

    def plant_on_board(self, guess_y, guess_x):
        planted_minecount = 0
        while planted_minecount < self.minecount:
            random_y = random.randint(0, self.size_y - 1)
            random_x = random.randint(0, self.size_x - 1)
            if not self.gameboard[random_y][random_x].ismine and (random_y != guess_y or random_x != guess_x):
                self.gameboard[random_y][random_x].ismine = True
                planted_minecount += 1

    def print_board(self):
        for y in range(len(self.gameboard)):
            for x in range(len(self.gameboard[y])):
                if self.gameboard[y][x].isclicked and not self.gameboard[y][x].ismine:
                    print(self.gameboard[y][x].neighmine, end=" ")
                elif self.gameboard[y][x].isclicked and self.gameboard[y][x].ismine:
                    print("X", end=" ")
                elif self.gameboard[y][x].isflagged:
                    print("F", end=" ")
                else:
                    print("#", end=" ")
            print("")

    def neigh_mine_count(self, guess_y, guess_x):
        for y in range(-1, 2):
            for x in range(-1, 2):
                if guess_y + y in range(0, self.size_y) and guess_x + x in range(0, self.size_x):
                    if self.gameboard[guess_y + y][guess_x + x].ismine and not self.gameboard[guess_y][guess_x].isclicked:
                        self.gameboard[guess_y][guess_x].neighmine += 1
        if not self.gameboard[guess_y][guess_x].isclicked:
            self.gameboard[guess_y][guess_x].isclicked = True
            self.remaining_fields -= 1

        if self.gameboard[guess_y][guess_x].neighmine == 0:
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if guess_y + y in range(0, self.size_y) and guess_x + x in range(0, self.size_x):
                        if not self.gameboard[guess_y+y][guess_x+x].isclicked:
                            Board.neigh_mine_count(self, guess_y+y, guess_x+x)

    def print_board_test(self):
        for y in range(len(self.gameboard)):
            for x in range(len(self.gameboard[y])):
                print(self.gameboard[y][x].ismine, end=" ")
            print("")

    def flag_uncover(self, guess_y, guess_x):
        if self.gameboard[guess_y][guess_x].isflagged:
            self.gameboard[guess_y][guess_x].isflagged = False
            self.remaining_flags += 1
            return self.remaining_flags
        elif not self.gameboard[guess_y][guess_x].isclicked:
            print("Field flagged")
            self.gameboard[guess_y][guess_x].isflagged = True
            self.remaining_flags -= 1
            return self.remaining_flags
        else:
            self.range_flagcount = 0
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if guess_y + y in range(0, self.size_y) and guess_x + x in range(0, self.size_x):
                        if self.gameboard[guess_y+y][guess_x+x].isflagged:
                            self.range_flagcount += 1

            if self.gameboard[guess_y][guess_x].neighmine != self.range_flagcount:
                print("Flag count and neighbour mine count doesn't match")
            else:
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        if guess_y + y in range(0, self.size_y) and guess_x + x in range(0, self.size_x):
                            if not self.gameboard[guess_y+y][guess_x+x].isflagged and not self.gameboard[guess_y+y][guess_x+x].ismine:
                                Board.neigh_mine_count(self, guess_y+y, guess_x+x)
                            elif not self.gameboard[guess_y+y][guess_x+x].isflagged and self.gameboard[guess_y+y][guess_x+x].ismine:
                                self.gameboard[guess_y+y][guess_x+x].isclicked = True
                                Variables.lost_y = guess_y + y
                                Variables.lost_x = guess_x + x
                                return guess_y + y, guess_x + x

    def guess(self, guess_y, guess_x):
        if self.firstclick:
            self.plant_on_board(guess_y, guess_x)
            self.firstclick = False
        if self.gameboard[guess_y][guess_x].ismine and not self.gameboard[guess_y][guess_x].isflagged:
            self.gameboard[guess_y][guess_x].isclicked = True
            return True
        elif self.gameboard[guess_y][guess_x].isclicked:
            print("Already clicked here")
        elif self.gameboard[guess_y][guess_x].isflagged:
            print("Can't click a flagged field")
        else:
            print("Miss")
            Board.neigh_mine_count(self, guess_y, guess_x)

    def is_over(self):
        if self.remaining_fields == 0:
            isover = True
        else:
            isover = False
        return isover
