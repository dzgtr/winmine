from tkinter import *


class AboutWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.wm_title("About")
        info = Label(self, text="Winmine beta by dzgtr\nInspired by winmine.exe for Windows XP.\n\n github.com/dzgtr\n2022")
        info.pack()
        close_button = Button(self, text="Close",
                              command=lambda: self.destroy())
        close_button.pack()
        self.attributes("-topmost", True)
        self.resizable(False, False)
        self.mainloop()
