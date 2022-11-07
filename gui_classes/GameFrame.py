from tkinter import *
from enum import Enum
import classes
import json
from gui_classes.Variables import Variables
from gui_classes.HighscoreWindow import HighscoreWindow


class GameState(Enum):
    inplay = 0
    lost = 1
    won = 2


class GameFrame(Frame):
    def __init__(self, gameframe, smile_image_callback, remaining_flags_callback, timer_callback):
        super().__init__()
        self.gameframe = gameframe
        self.change_smile = smile_image_callback
        self.remaining_flags = remaining_flags_callback
        self.timer = timer_callback
        self.timer_is_running = False
        self.new_game()
        self.highscore()

    def new_game(self):
        if hasattr(self, 'gui_board'):
            self.destroy_gui_board()

        self.board = classes.Board(Variables.difficulties[Variables.current_difficulty].size_y,
                                   Variables.difficulties[Variables.current_difficulty].size_x,
                                   Variables.difficulties[Variables.current_difficulty].minecount)
        Variables.flagcount_or_boomcords = None
        self.board.create_board()
        self.board.plant_on_board()
        self.game_state = GameState.inplay
        self.create_gui_board()
        self.remaining_flags(Variables.difficulties[Variables.current_difficulty].minecount)
        self.print_gui_board()
        self.stop_timer()

    def create_gui_board(self):
        self.gui_board = []
        for y in range(len(self.board.gameboard)):
            self.gui_board.append([])
            for x in range(len(self.board.gameboard[y])):
                self.gui_board[y].append(Button(self.gameframe, name=f"{y},{x}", command=lambda y = y, x = x: self.button_guess(y, x)))
                self.gui_board[y][x].bind("<ButtonPress-1>", lambda x: self.change_smile("click"))
                self.gui_board[y][x].bind("<Button-3>", lambda event, y = y, x = x: self.button_flag(y, x))
                self.gui_board[y][x].grid(row=y + 1, column=x)

    def button_guess(self, guess_y, guess_x):
        self.start_timer()
        Variables.guess_y = guess_y
        Variables.guess_x = guess_x
        self.change_smile("smile")
        if self.board.guess(guess_y, guess_x):
            self.game_state = GameState.lost
            self.game_over()
        if self.board.is_over():
            self.game_state = GameState.won
            self.game_over()

        self.print_gui_board()

    def button_flag(self, flag_y, flag_x):
        self.start_timer()
        Variables.guess_y = flag_y
        Variables.guess_x = flag_x
        Variables.flagcount_or_boomcords = self.board.flag_uncover(flag_y, flag_x)

        if type(Variables.flagcount_or_boomcords) is tuple:
            self.game_state = GameState.lost
            self.game_over()

        if type(Variables.flagcount_or_boomcords) is int:
            self.remaining_flags(Variables.flagcount_or_boomcords)

        if self.board.is_over():
            self.game_state = GameState.won
            self.game_over()

        self.print_gui_board()

    def print_gui_board(self):
        for y in range(len(self.gui_board)):
            for x in range(len(self.gui_board[y])):
                image = PhotoImage(file=f"./_img/{self.change_button_image(y, x)}.png")
                self.gui_board[y][x].photo = image
                self.gui_board[y][x].config(image=image)

    def change_button_image(self, y, x):
        if self.game_state == GameState.won:
            if self.board.gameboard[y][x].ismine:
                return "mine_flag"

        elif self.game_state == GameState.lost:
            if type(Variables.flagcount_or_boomcords) is tuple:
                if y == Variables.flagcount_or_boomcords[0] and x == Variables.flagcount_or_boomcords[1]:
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

    def game_over(self):
        self.stop_timer()
        for y in range(len(self.gui_board)):
            for x in range(len(self.gui_board[y])):
                self.gui_board[y][x].config(state="disabled")
                self.gui_board[y][x].unbind("<ButtonPress-1>")
                self.gui_board[y][x].unbind("<Button-3>")
        if self.game_state == GameState.won:
            print("You won!!!")
            self.change_smile("sunglasses")
            if Variables.difficulties[Variables.current_difficulty].name != "Custom":
                self.highscore()
        elif self.game_state == GameState.lost:
            print("You lost.")
            self.change_smile("dead")

    def start_timer(self):
        if not self.timer_is_running:
            self.timer_is_running = True
            self.timer(True)

    def stop_timer(self):
        self.timer_is_running = False
        self.timer(False)

    def destroy_gui_board(self):
        for y in range(len(self.gui_board)):
            for x in range(len(self.gui_board[y])):
                self.gui_board[y][x].destroy()

    def highscore(self):
        with open("highscores.json", "r", encoding="utf-8") as json_file:
            highscores = json.load(json_file)

        if highscores[Variables.difficulties[Variables.current_difficulty].name][0] > Variables.game_time:
            new_hs_window = Toplevel()
            new_hs_window.resizable(False, False)
            new_hs_window.attributes("-topmost", True)
            new_hs_window.wm_title("New High Score!")
            label = Label(new_hs_window, text=f"You have the fastest time\nfor {Variables.difficulties[Variables.current_difficulty].name} level.\nPlease enter your name.\n")
            label.pack(pady=10, padx=15)
            highscore_name = StringVar()
            highscore_entry = Entry(new_hs_window, bg="white", textvariable=highscore_name)
            highscore_entry.pack()
            highscore_button = Button(new_hs_window, text="OK", command=lambda: [self.savefile(highscores, highscore_name.get()), new_hs_window.destroy()])
            highscore_button.pack()

    def savefile(self, highscores, name):
        highscores[Variables.difficulties[Variables.current_difficulty].name][0] = Variables.game_time - 1  # Idk why it's 1s off
        highscores[Variables.difficulties[Variables.current_difficulty].name][1] = name

        with open("highscores.json", "w", encoding="utf-8") as json_file:
            json.dump(highscores, json_file, indent=4, ensure_ascii=False)

        HighscoreWindow()
