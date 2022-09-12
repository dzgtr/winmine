from tkinter import *
import tkinter.messagebox

class MainWindow(Frame):
    def __init__(self, master=None):
        self.selected_difficulty = tkinter.StringVar()
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        game_menu = Menu(menu, tearoff=0)
        game_menu.add_command(label="New Game")
        game_menu.add_command(label="Options", command=self.options)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=game_menu)

        about_menu = Menu(menu, tearoff=0)
        about_menu.add_command(label="About", command=self.about)
        menu.add_cascade(label="About", menu=about_menu)

    def exitProgram(self):
        exit()

    def about(self):
        about_root = Tk()
        about_root.geometry("400x300")
        about_root.wm_title("About")
        close_button = Button(about_root, text="Close", command=lambda: [print(self.selected_difficulty), about_root.destroy])
        close_button.pack()
        about_root.mainloop()

    def options(self):
        options_root = Tk()
        options_root.geometry("400x300")
        options_root.wm_title("Options")
        difficulties = [
            Difficulty("Beginner", 9, 9, 10),
            Difficulty("Intermediate", 16, 16, 40),
            Difficulty("Expert", 16, 30, 99),
            Difficulty("Custom",1,1,1)
        ]

        for diff_number in range(len(difficulties)):
            radio_buttons = Radiobutton(options_root, text=difficulties[diff_number].name, value=difficulties[diff_number].name, variable=self.selected_difficulty)
            diff_label = Label(options_root, text=f"{difficulties[diff_number].size_y} x {difficulties[diff_number].size_x}, {difficulties[diff_number].minecount} mines")
            radio_buttons.grid(row=diff_number, column=0, sticky=W)
            diff_label.grid(row=diff_number, column=1, sticky=W)

        save_button = Button(options_root, text="Save", command=lambda: [self.save_options(), options_root.destroy()])
        save_button.grid(row=4)
        options_root.mainloop()

    def save_options(self):
        difficul = self.selected_difficulty.get()
        print(difficul)

class Difficulty:
    def __init__(self, name, size_y, size_x, minecount):
        self.name = name
        self.size_y = size_y
        self.size_x = size_x
        self.minecount = minecount

class FieldButton:
    def __init__(self, current_image):
        self.current_image = current_image
        self.field_button = Label(gamefield, image=self.current_image)
        self.field_button.bind("<Button-1>", click) #left click dodelat
        self.field_button.bind("<Button-3>", rclick)  # right click dodelat
        self.field_button.pack()

class GuiBoard:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.gui_board = []

    def create_board(self):
        for y in range(self.size_y):
            self.gui_board.append([])
            for x in range(self.size_x):
                self.gui_board[y].append(FieldButton())

    def print_board(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.gui_board[y][x]