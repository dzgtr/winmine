from tkinter import *
import classes


class ImageButton():
    def __init__(self, button_frame, img_name, row, column, board):
#        Frame.__init__(self, button_frame)
        self.button_frame = button_frame
        self.img_name = img_name
        self.board = board
        self.row = row
        self.column = column

        self.image = PhotoImage(file=f"./_img/{self.img_name}.png")
        self.field = Button(self.button_frame, image=self.image)
        self.field.photo = self.image
        self.field.bind("<Button-1>", self.button_l_click)
        self.field.bind("<Button-3>", self.button_r_click)
        self.field.grid(row=row+1, column=column)

    def button_l_click(self, event):
        self.board.guess(self.row, self.column)
#        self.change_images()
    def button_r_click(self, event):
        self.board.flag_uncover(self.row, self.column)
#        self.change_images()

    def change_images(self):
        for y in range(len(self.board.gameboard)):
            for x in range(len(self.board.gameboard[y])):
                if not self.board.gameboard[y][x].isclicked and self.board.gameboard[y][x].neighmine == 0:
                    self.img_name = "mine_blank"
                elif self.board.gameboard[y][x].isclicked and self.board.gameboard[y][x].neighmine == 0:
                    self.img_name = "mine_0"
                elif self.board.gameboard[y][x].isclicked and not self.board.gameboard[y][x].ismine:
                    self.img_name = f"mine_{self.board.gameboard[y][x].neighmine}"
                elif self.board.gameboard[y][x].isflagged:
                    self.img_name = "mine_blank"  # HERE WILL BE FLAG IMGAE
                elif self.board.gameboard[y][x].ismine:
                    self.img_name = "mine_boom"

                self.image = PhotoImage(file=f"./_img/{self.img_name}.png")
                self.field.config(image=self.image)