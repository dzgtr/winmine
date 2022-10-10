from tkinter import *
from enum import Enum
import classes
from gui_classes.Variables import Variables

class GameState(Enum):
    inplay = 0
    lost = 1
    won = 2

class GameFrame(Frame):
    def __init__(self, gameframe):
        Frame.__init__(self, gameframe)
        self.gameframe = gameframe
        self.new_game()

    def new_game(self):
        self.board = classes.Board(Variables.difficulties[Variables.current_difficulty.get()].size_x,
                              Variables.difficulties[Variables.current_difficulty.get()].size_y,
                              Variables.difficulties[Variables.current_difficulty.get()].minecount)
        Variables.lost_x, Variables.lost_y = None, None
        self.board.create_board()
        self.board.plant_on_board()
        self.game_state = GameState.inplay
        self.create_gui_board()
        self.print_gui_board()
    def create_gui_board(self):
        self.gui_board = []
        for y in range(len(self.board.gameboard)):
            self.gui_board.append([])
            for x in range(len(self.board.gameboard[y])):
                self.gui_board[y].append(Button(self.gameframe, name=f"{y},{x}", command=lambda y = y, x = x: self.button_guess(y,x)))
                self.gui_board[y][x].bind("<Button-3>", lambda event, x = x, y = y: self.button_flag(event, y,x))
                self.gui_board[y][x].grid(row=y + 1, column=x)


    def print_gui_board(self):
        for y in range(len(self.gui_board)):
            for x in range(len(self.gui_board[y])):
                image = PhotoImage(file=f"./_img/{self.change_button_image(y, x)}.png")
                self.gui_board[y][x].photo = image
                self.gui_board[y][x].config(image=image)


    def button_guess(self, guess_y, guess_x):
        Variables.guess_y = guess_y
        Variables.guess_x = guess_x
        if self.board.guess(guess_y, guess_x):
            self.game_state = GameState.lost
            print("you lossdsguess")
            self.test_new_game()
        if self.board.is_over():
            self.game_state = GameState.won
            print("You won!!!")
            self.test_new_game()
        self.print_gui_board()

    def button_flag(self, event, flag_y, flag_x):
        Variables.guess_y = flag_y
        Variables.guess_x = flag_x
        if self.board.flag_uncover(flag_y, flag_x):
            self.game_state = GameState.lost
            print("you lossdsuncover")
            self.test_new_game()
        if self.board.is_over():
            self.game_state = GameState.won
            print("You won!!!")
            self.test_new_game()
        self.print_gui_board()

    def change_button_image(self, y, x):
        if self.game_state == GameState.won:
            if self.board.gameboard[y][x].ismine:
                return "mine_flag"

        elif self.game_state == GameState.lost:
            if y == Variables.lost_y and x == Variables.lost_x:
                return "mine_boom"
            if y == Variables.guess_y and x == Variables.guess_x:
                if self.board.gameboard[y][x].neighmine > 0:
                    return f"mine_{self.board.gameboard[y][x].neighmine}"
                else:
                    return "mine_boom"
            if self.board.gameboard[y][x].isflagged and not self.board.gameboard[y][x].ismine:
                    return "mine_falseflag"
            if self.board.gameboard[y][x].ismine:
                return "mine_revealed"

        if self.board.gameboard[y][x].isflagged:
            return "mine_flag"
        elif self.board.gameboard[y][x].isclicked:
            return f"mine_{self.board.gameboard[y][x].neighmine}"
        else:
            return "mine_blank"

    def test_new_game(self):
        ng = Toplevel()
        close_button = Button(ng, text="New game",
                              command=lambda: [self.new_game(), ng.destroy()])
        close_button.pack()