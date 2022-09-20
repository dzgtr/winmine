import classes
import tkinter.ttk
from tkinter import *
import tkinter.messagebox
from gui_classes.MainWindow import MainWindow
from gui_classes.Variables import Variables
from gui_classes.Difficulty import Difficulty

root = Tk()
main = MainWindow(root)
#board = classes.Board(row_count, col_count, minecount)
#board.create_board()
#board.plant_on_board()
selected_difficulty = IntVar(None, 5)
difficulties = [
    Difficulty("Beginner", 9, 9, 10),
    Difficulty("Intermediate", 16, 16, 40),
    Difficulty("Expert", 16, 30, 99),
    Difficulty("Custom", 0, 0, 0)
]
for diff_number in range(3):
    radio_buttons = Radiobutton(root, text=difficulties[diff_number].name, value=diff_number, variable=selected_difficulty)
    diff_label = Label(root, text=f"{difficulties[diff_number].size_y} x {difficulties[diff_number].size_x}, {difficulties[diff_number].minecount} mines")
    radio_buttons.grid(row=diff_number, column=0, sticky=W)
    diff_label.grid(row=diff_number, column=1, sticky=W)

save_button = Button(root, text="Save", command=lambda: [save_options(), root.destroy()])
save_button.grid(row=4)

def save_options():
    Variables.current_difficulty = selected_difficulty.get()
    print(difficulties[Variables.current_difficulty].name)


root.wm_title("Minesweeper")
root.mainloop()