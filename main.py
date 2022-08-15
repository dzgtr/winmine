import classes

x_size = 3
y_size = 3
minecount = 3

board = classes.Board(x_size, y_size, minecount)
board.create_board()
board.plant_on_board()
board.print_board()
guess_x = 0
guess_y = 0

while True:
    guess_x = int(input("Zadej řádek:"))
    guess_y = int(input("Zadej sloupec:"))
    if guess_x >= x_size or guess_y >= y_size:
        print("Zadané souřadnice jsou mimo herní plochu.")
    else:
        if board.guess(guess_x, guess_y):
            break
        if board.is_over():
            print("You won!!!")
            break
