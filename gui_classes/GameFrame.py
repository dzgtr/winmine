from tkinter import *
from enum import Enum
import classes
from gui_classes.Variables import Variables
from gui_classes.ImageButton import ImageButton
from gui_classes.ImageLabel import ImageLabel

class GameState(Enum):
    inplay = 0
    lost = 1
    won = 2

class GameFrame(Frame):
    def __init__(self, gameframe):
        Frame.__init__(self, gameframe)
        self.gameframe = gameframe
        self.board = classes.Board(Variables.difficulties[Variables.current_difficulty.get()].size_x,
                              Variables.difficulties[Variables.current_difficulty.get()].size_y,
                              Variables.difficulties[Variables.current_difficulty.get()].minecount)
        self.board.create_board()
        self.board.plant_on_board()
        self.game_state = GameState.inplay
        self.create_gui_board()
        self.print_gui_board(None, None)
#        self.update_gui_board()

    def create_gui_board(self):
        self.gui_board = []
        for y in range(len(self.board.gameboard)):
            self.gui_board.append([])
            for x in range(len(self.board.gameboard[y])):
                self.gui_board[y].append(Button(self.gameframe, name=f"{y},{x}", command=lambda x = x, y = y: self.button_guess(y,x)))
                self.gui_board[y][x].bind("<Button-3>", lambda x = x, y = y: self.button_flag(y,x))
                self.gui_board[y][x].grid(row=y + 1, column=x)


    def print_gui_board(self, y, x):
        for y in range(len(self.gui_board)):
            for x in range(len(self.gui_board[y])):
                image = PhotoImage(file=f"./_img/{self.change_button_image(y, x)}.png")
                self.gui_board[y][x].photo = image
                self.gui_board[y][x].config(image=image)

    def button_guess(self, guess_y, guess_x):
        if self.board.guess(guess_y, guess_x):
            self.game_state = GameState.lost
            self.print_gui_board(guess_y, guess_x)
            image = PhotoImage(file=f"./_img/mine_boom.png")
            self.gui_board[guess_y][guess_x].photo = image
            self.gui_board[guess_y][guess_x].config(image=image)
            return
        if self.board.is_over():
            self.game_state = GameState.won
            print("You won!!!")
            self.print_gui_board(guess_y, guess_x)
            return
        self.print_gui_board(guess_y, guess_x)

    def button_flag(self, y, x):
        self.board.flag_uncover(y, x)
        self.print_gui_board()

    def change_button_image(self, y, x):
        if self.game_state == GameState.won:
            if self.board.gameboard[y][x].ismine:
                return "mine_flag"
        if self.game_state == GameState.lost:
            if self.board.gameboard[y][x].isflagged and self.board.gameboard[y][x].ismine:
                return "mine_falseflag"
            elif self.board.gameboard[y][x].isflagged and not self.board.gameboard[y][x].ismine:
                return "mine_8"
        if self.board.gameboard[y][x].isflagged:
            return "mine_flag"
        elif self.board.gameboard[y][x].isclicked:
            return f"mine_{self.board.gameboard[y][x].neighmine}"
        else:
            return "mine_blank"
            """
            if not self.board.gameboard[y][x].isclicked and self.board.gameboard[y][x].neighmine == 0:
                self.gui_board[y][x].image = PhotoImage(file=f"./_img/mine_blank.png")
                self.gui_board[y][x].field.config(image=self.gui_board[y][x].image)
            elif self.board.gameboard[y][x].isclicked and self.board.gameboard[y][x].neighmine == 0:
                self.gui_board[y][x].image = PhotoImage(file=f"./_img/mine_0.png")
                self.gui_board[y][x].field.config(image=self.gui_board[y][x].image)
            elif self.board.gameboard[y][x].isclicked and not self.board.gameboard[y][x].ismine:
                self.gui_board[y][x].img_name = f"mine_{self.board.gameboard[y][x].neighmine}"
                self.gui_board[y][x].image = PhotoImage(file=f"./_img/{self.gui_board[y][x].img_name}.png")
                self.gui_board[y][x].field.config(image=self.gui_board[y][x].image)
            else:
                pass
            """
    def print_gui_board_end(self):
        pass

