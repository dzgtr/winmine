from tkinter import *
import tkinter.messagebox
from gui_classes.Difficulty import Difficulty
from gui_classes.Variables import Variables


class OptionsWindow(Toplevel):
    def __init__(self, new_game_callback):
        super().__init__()

        self.wm_title("Options")
        self.new_game = new_game_callback
        self.diff_selector = IntVar(None, 0)

        for diff_number in range(3):
            radio_buttons = Radiobutton(self, text=Variables.difficulties[diff_number].name, value=diff_number, variable=self.diff_selector)
            diff_label = Label(self, text=f"{Variables.difficulties[diff_number].size_y} x {Variables.difficulties[diff_number].size_x}, {Variables.difficulties[diff_number].minecount} mines")
            radio_buttons.grid(row=diff_number, column=0, sticky=W)
            diff_label.grid(row=diff_number, column=1, sticky=W, columnspan=5)
        radio_button = Radiobutton(self, text="Custom (7x7 - 30x58)", value=3, variable=self.diff_selector)
        radio_button.grid(row=4, column=0, sticky=W)
        custom_text1 = Label(self, text="Height: ")
        custom_text1.grid(row=4, column=1, sticky=W)
        self.custom_y = Entry(self, width=3)
        self.custom_y.grid(row=4, column=2, sticky=W)
        custom_text2 = Label(self, text="Width: ")
        custom_text2.grid(row=4, column=3, sticky=W)
        self.custom_x = Entry(self, width=3)
        self.custom_x.grid(row=4, column=4, sticky=W)
        custom_text3 = Label(self, text="Mines: ")
        custom_text3.grid(row=4, column=5, sticky=W)
        self.custom_minecount = Entry(self, width=3)
        self.custom_minecount.grid(row=4, column=6)
        custom = Label(self)
        custom.grid(row=5)
        save_button = Button(self, text="Save", command=self.save_options)
        save_button.grid(row=5, columnspan=6)
        self.attributes("-topmost", True)
        self.mainloop()

    def save_options(self):
        if self.diff_selector.get() in range(0, 3):
            Variables.current_difficulty = self.diff_selector.get()
            self.destroy()
            self.new_game()
        elif self.diff_selector.get() == 3 and self.custom_y.get() != "" and self.custom_x.get() != "":
            if int(self.custom_y.get()) in range(7, 31) and int(self.custom_x.get()) in range(7, 58):
                if self.custom_minecount.get() == "" or int(self.custom_minecount.get()) == 0:
                    tkinter.messagebox.showwarning(title="Do you even sweep?", message="You want to play Minesweeper without mines?", parent=self)
                else:
                    try:
                        Variables.difficulties[3].size_y = int(self.custom_y.get())
                        Variables.difficulties[3].size_x = int(self.custom_x.get())
                        Variables.difficulties[3].minecount = int(self.custom_minecount.get())
                    except:
                        Variables.difficulties.append(Difficulty("Custom", int(self.custom_y.get()), int(self.custom_x.get()), int(self.custom_minecount.get())))
                    Variables.current_difficulty = self.diff_selector.get()
                    self.destroy()
                    self.new_game()
            else:
                tkinter.messagebox.showwarning(title="Incorrect field size",
                                               message="Enter valid field size(7x7 - 30x58)", parent=self)

        else:
            tkinter.messagebox.showerror(title="What are you doing?",
                                         message="Enter at least something when you chose Custom difficulty, preferably valid field size(7x7 - 30x58)", parent=self)

        print(Variables.current_difficulty)
        print("Difficulty selected: " + Variables.difficulties[Variables.current_difficulty].name)
        print(Variables.difficulties[Variables.current_difficulty].size_y)
        print(Variables.difficulties[Variables.current_difficulty].minecount)
