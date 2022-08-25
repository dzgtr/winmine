import random


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
        for x in range(self.size_y):
            self.gameboard.append([])
            for y in range(self.size_x):
                self.gameboard[x].append(Field())

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
                else:
                    print("#", end=" ")
            print("")

    def neigh_mine_count(self, guess_x, guess_y):
        self.gameboard[guess_x][guess_y].isclicked = True
        self.remaining -= 1
        for x in range(-1, 2):
            for y in range(-1, 2):
                if guess_x + x in range(0, self.size_x) and guess_y + y in range(0, self.size_y):
                    if self.gameboard[guess_x + x][guess_y + y].ismine:
                        self.gameboard[guess_x][guess_y].neighmine += 1

        if self.gameboard[guess_x][guess_y].neighmine == 0:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if guess_x + x in range(0, self.size_x) and guess_y + y in range(0, self.size_y):
                        if not self.gameboard[guess_x+x][guess_y+y].isclicked:
                            Board.neigh_mine_count(self, guess_x+x, guess_y+y)

    def print_board_test(self):
        for x in range(len(self.gameboard)):
            for y in range(len(self.gameboard[x])):
                print(self.gameboard[x][y].ismine, end=" ")
            print("")

# here will be fast uncover function when you click on already clicked but solved field
    def fast_uncover(self, guess_x, guess_y):
        print("Already clicked here")

    def guess(self, guess_x, guess_y):
        if self.gameboard[guess_x][guess_y].ismine:
            self.gameboard[guess_x][guess_y].isclicked = True
            print("You Lost!")
            return True
        elif self.gameboard[guess_x][guess_y].isclicked:
            Board.fast_uncover(self, guess_x, guess_y)
        else:
            print("Miss")
            Board.neigh_mine_count(self, guess_x, guess_y)

    def is_over(self):
        if self.remaining == 0:
            isover = True
        else:
            isover = False
        return isover
