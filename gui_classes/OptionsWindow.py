from tkinter import *
from gui_classes.Difficulty import Difficulty
from gui_classes.Variables import Variables

class OptionsWindow(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x300")
        self.wm_title("Options")
        
        for diff_number in range(3):
            radio_buttons = Radiobutton(self, text=Variables.difficulties[diff_number].name, value=diff_number, variable=Variables.current_difficulty)
            diff_label = Label(self, text=f"{Variables.difficulties[diff_number].size_y} x {Variables.difficulties[diff_number].size_x}, {Variables.difficulties[diff_number].minecount} mines")
            radio_buttons.grid(row=diff_number, column=0, sticky=W)
            diff_label.grid(row=diff_number, column=1, sticky=W, columnspan=5)
        radio_button = Radiobutton(self, text="Custom", value=3, variable=Variables.current_difficulty)
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
        save_button = Button(self, text="Save", command=lambda: [self.save_options(), self.destroy()])
        save_button.grid(row=5, columnspan=6)
        self.mainloop()

    def save_options(self):
        self.selected_difficulty = Variables.current_difficulty.get()
        Variables.difficulties.append(
            Difficulty("Custom", self.custom_y.get(), self.custom_x.get(), self.custom_minecount.get()))
        print(self.selected_difficulty)
        print("Difficulty selected: " + Variables.difficulties[Variables.current_difficulty.get()].name)
        print(Variables.difficulties[Variables.current_difficulty.get()].size_y)
        print(Variables.difficulties[Variables.current_difficulty.get()].size_x)
        print(Variables.difficulties[Variables.current_difficulty.get()].minecount)