from tkinter import *

from gui_classes.Difficulty import Difficulty
from gui_classes.Variables import Variables
from gui_classes.FieldButton import FieldButton

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)
        self.selected_difficulty = IntVar(None, 5)
        self.difficulties = [
            Difficulty("Beginner", 9, 9, 10),
            Difficulty("Intermediate", 16, 16, 40),
            Difficulty("Expert", 16, 30, 99),
            Difficulty("Custom", 0, 0, 0)
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

#        game_frame = gui_classes.GuiBoard()

#        game_frame.pa

    def exitProgram(self):
        exit()

    def about(self):
        about_root = Tk()
        about_root.geometry("400x300")
        about_root.wm_title("About")
        close_button = Button(about_root, text="Close", command=lambda: [print(Variables.current_difficulty), about_root.destroy()])
        close_button.pack()
        about_root.mainloop()

    def options(self):
        options_root = Tk()
        options_root.geometry("400x300")
        options_root.wm_title("Options")

        for diff_number in range(3):
            radio_buttons = Radiobutton(options_root, text=self.difficulties[diff_number].name, value=diff_number, variable=self.selected_difficulty)
            diff_label = Label(options_root, text=f"{self.difficulties[diff_number].size_y} x {self.difficulties[diff_number].size_x}, {self.difficulties[diff_number].minecount} mines")
            radio_buttons.grid(row=diff_number, column=0, sticky=W)
            diff_label.grid(row=diff_number, column=1, sticky=W)

        save_button = Button(options_root, text="Save", command=lambda: [self.save_options(), options_root.destroy()])
        save_button.grid(row=4)
        options_root.mainloop()

    def save_options(self):
        print(self.selected_difficulty.get())
        Variables.current_difficulty = self.selected_difficulty.get()
        #print(self.difficulties[Variables.current_difficulty].name)
