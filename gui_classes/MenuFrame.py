from tkinter import *

from gui_classes.Difficulty import Difficulty
from gui_classes.Variables import Variables
from gui_classes.FieldButton import FieldButton
from gui_classes.GuiBoard import GuiBoard

class MenuFrame(Frame):
    def __init__(self, menuframe):
        Frame.__init__(self, menuframe)
        self.menuframe = menuframe
        menu = Menu(self.menuframe)
        self.menuframe.config(menu=menu)
        self.difficulties = [
            Difficulty("Beginner", 9, 9, 10),
            Difficulty("Intermediate", 16, 16, 40),
            Difficulty("Expert", 16, 30, 99)
        ]

        game_menu = Menu(menu, tearoff=0)
        game_menu.add_command(label="New Game")
        game_menu.add_command(label="Options", command=self.options)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=game_menu)

        about_menu = Menu(menu, tearoff=0)
        about_menu.add_command(label="About", command=self.about)
        menu.add_cascade(label="About", menu=about_menu)
        Variables.current_difficulty = IntVar(None, 2) # sets current difficulty to expert
        game_frame = GuiBoard(self.difficulties[Variables.current_difficulty.get()].size_y, self.difficulties[Variables.current_difficulty.get()].size_x)

    def exitProgram(self):
        exit()

    def about(self):
        about_root = Toplevel()
        about_root.geometry("400x300")
        about_root.wm_title("About")
        close_button = Button(about_root, text="Close", command=lambda: [print(Variables.current_difficulty.get()), about_root.destroy()])
        close_button.pack()
        about_root.mainloop()

    def options(self):
        options_root = Toplevel()
        options_root.geometry("400x300")
        options_root.wm_title("Options")

        for diff_number in range(3):
            radio_buttons = Radiobutton(options_root, text=self.difficulties[diff_number].name, value=diff_number, variable=Variables.current_difficulty)
            diff_label = Label(options_root, text=f"{self.difficulties[diff_number].size_y} x {self.difficulties[diff_number].size_x}, {self.difficulties[diff_number].minecount} mines")
            radio_buttons.grid(row=diff_number, column=0, sticky=W)
            diff_label.grid(row=diff_number, column=1, sticky=W, columnspan=5)
        radio_button = Radiobutton(options_root, text="Custom", value=3, variable=Variables.current_difficulty)
        radio_button.grid(row=4, column=0, sticky=W)
        custom_text1 = Label(options_root, text="Height: ")
        custom_text1.grid(row=4, column=1, sticky=W)
        self.custom_y = Entry(options_root, width=3)
        self.custom_y.grid(row=4, column=2, sticky=W)
        custom_text2 = Label(options_root, text="Width: ")
        custom_text2.grid(row=4, column=3, sticky=W)
        self.custom_x = Entry(options_root, width=3)
        self.custom_x.grid(row=4, column=4, sticky=W)
        custom_text3 = Label(options_root, text="Mines: ")
        custom_text3.grid(row=4, column=5, sticky=W)
        self.custom_minecount = Entry(options_root, width=3)
        self.custom_minecount.grid(row=4, column=6)
        custom = Label(options_root)
        custom.grid(row=5)
        save_button = Button(options_root, text="Save", command=lambda: [self.save_options(), options_root.destroy()])
        save_button.grid(row=5, columnspan=6)
        options_root.mainloop()

    def save_options(self):
        self.selected_difficulty = Variables.current_difficulty.get()
        self.difficulties.append(Difficulty("Custom", self.custom_y.get(), self.custom_x.get(), self.custom_minecount.get()))
        print(self.selected_difficulty)
        print("Difficulty selected: " + self.difficulties[Variables.current_difficulty.get()].name)
        print(self.difficulties[Variables.current_difficulty.get()].size_y)
        print(self.difficulties[Variables.current_difficulty.get()].size_x)
        print(self.difficulties[Variables.current_difficulty.get()].minecount)