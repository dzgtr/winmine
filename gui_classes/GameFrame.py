from tkinter import *
import classes
from gui_classes.Variables import Variables
from gui_classes.ImageButton import ImageButton
from gui_classes.ImageLabel import ImageLabel
class GameFrame(Frame):
    def __init__(self, gameframe):
        Frame.__init__(self, gameframe)
        self.gameframe = gameframe
        self.gui_board = []

        self.board = classes.Board(Variables.difficulties[Variables.current_difficulty.get()].size_x,
                              Variables.difficulties[Variables.current_difficulty.get()].size_y,
                              Variables.difficulties[Variables.current_difficulty.get()].minecount)
        self.board.create_board()
        self.board.plant_on_board()
        self.create_gui_board()
        self.print_gui_board()

    def create_gui_board(self):
        for y in range(len(self.board.gameboard)):
            self.gui_board.append([])
            for x in range(len(self.board.gameboard[y])):
                self.gui_board[y].append("")
    def print_gui_board(self):
        for y in range(len(self.board.gameboard)):
            for x in range(len(self.board.gameboard[y])):
                if not self.board.gameboard[y][x].isclicked:
                    self.gui_board[y][x] = ImageButton(self.gameframe, "mine_blank", y, x)
                elif self.board.gameboard[y][x].isclicked and self.board.gameboard[y][x].neighmine == 0:
                    self.gui_board[y][x] = ImageLabel(self.gameframe, "mine_0", y, x)
                else:
                    self.gui_board[y][x] = ImageButton(self.gameframe, f"mine_{self.board.gameboard[y][x].neighmine}")

        print(self.gui_board)

#        #print field buttons now
#        image = PhotoImage(file=f"./_img/mine_2.png")
#        field = Button(self.gameframe, image=image)
#        field.photo = image
#        field.pack()