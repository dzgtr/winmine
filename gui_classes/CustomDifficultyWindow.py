from tkinter import *
from gui_classes.Variables import Variables
from gui_classes.Difficulty import Difficulty

class CustomDifficultyWindow(Toplevel):
    def __init__(self, new_game_callback, previous_difficult):
        super().__init__()

        self.wm_title("Custom Field")
        self.new_game = new_game_callback
        self.resizable(False, False)

        custom_text1 = Label(self, text="Height: ")
        custom_text1.grid(sticky=W, row=0, column=0, pady=(20, 0), padx=10)
        self.custom_y = Entry(self, width=5, background="white")
        self.custom_y.insert(0, Variables.difficulties[previous_difficult].size_y)
        self.custom_y.bind('<FocusIn>', lambda x: self.custom_y.selection_range(0, END))
        self.custom_y.grid(sticky=W, row=0, column=1, padx=10, pady=(20, 0))
        custom_text2 = Label(self, text="Width: ")
        custom_text2.grid(sticky=W, row=1, column=0, padx=10)
        self.custom_x = Entry(self, width=5, background="white")
        self.custom_x.insert(0, Variables.difficulties[previous_difficult].size_x)
        self.custom_x.bind('<FocusIn>', lambda x: self.custom_x.selection_range(0, END))
        self.custom_x.grid(sticky=W, row=1, column=1, padx=10)
        custom_text3 = Label(self, text="Mines: ")
        custom_text3.grid(sticky=W, row=2, column=0, padx=10, pady=(0, 20))
        self.custom_minecount = Entry(self, width=5, background="white")
        self.custom_minecount.insert(0, Variables.difficulties[previous_difficult].minecount)
        self.custom_minecount.bind('<FocusIn>', lambda x: self.custom_minecount.selection_range(0, END))
        self.custom_minecount.grid(row=2, column=1, padx=10, pady=(0, 20))

        save_button = Button(self, text="OK", command=self.save_options, width=6)
        save_button.grid(row=0, column=2, rowspan=2, padx=10)
        cancel_button = Button(self, text="Cancel", command=self.destroy, width=6)
        cancel_button.grid(row=1, column=2, rowspan=3, padx=10)
        self.attributes("-topmost", True)
        self.mainloop()

    def save_options(self):
        if int(self.custom_y.get()) <= 9:
            Variables.difficulties[3].size_y = Variables.difficulties[0].size_y
        elif int(self.custom_y.get()) >= 24:
            Variables.difficulties[3].size_y = 24
        else:
            Variables.difficulties[3].size_y = int(self.custom_y.get())

        if int(self.custom_x.get()) <= 9:
            Variables.difficulties[3].size_x = Variables.difficulties[0].size_x
        elif int(self.custom_x.get()) >= 30:
            Variables.difficulties[3].size_x = 30
        else:
            Variables.difficulties[3].size_x = int(self.custom_x.get())
        print((Variables.difficulties[3].size_y - 1) * (Variables.difficulties[3].size_x - 1))
        if int(self.custom_minecount.get()) <= 10:
            Variables.difficulties[3].minecount = Variables.difficulties[0].minecount
        elif int(self.custom_minecount.get()) >= (Variables.difficulties[3].size_y - 1) * (Variables.difficulties[3].size_x - 1):
            Variables.difficulties[3].minecount = (Variables.difficulties[3].size_y - 1) * (Variables.difficulties[3].size_x - 1)
        else:
            Variables.difficulties[3].minecount = int(self.custom_minecount.get())

        self.new_game()
        self.destroy()

        print(Variables.current_difficulty)
        print("Difficulty selected: " + Variables.difficulties[Variables.current_difficulty].name)
        print(Variables.difficulties[Variables.current_difficulty].size_y)
        print(Variables.difficulties[Variables.current_difficulty].minecount)


