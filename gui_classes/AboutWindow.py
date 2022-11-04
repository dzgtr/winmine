from tkinter import *
from gui_classes.Variables import Variables

class AboutWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.wm_title("About")
        close_button = Button(self, text="Close",
                              command=lambda: self.destroy())
        close_button.pack()
        self.attributes("-topmost", True)
        self.mainloop()
