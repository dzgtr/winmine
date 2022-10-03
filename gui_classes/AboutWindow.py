from tkinter import *
from gui_classes.Variables import Variables

class AboutWindow(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("400x300")
        self.wm_title("About")
        close_button = Button(self, text="Close",
                              command=lambda: [print(Variables.current_difficulty.get()), self.destroy()])
        close_button.pack()
        self.mainloop()
