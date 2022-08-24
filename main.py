import classes

x_size = 5
y_size = 5
minecount = 5

board = classes.Board(x_size, y_size, minecount)
board.create_board()
board.plant_on_board()
board.print_board_test()
guess_x = 0
guess_y = 0

while True:
    board.print_board()
    print(board.remaining)
    guess_x = int(input("Zadej řádek:"))
    guess_y = int(input("Zadej sloupec:"))
    if guess_x >= x_size or guess_y >= y_size:
        print("Zadané souřadnice jsou mimo herní plochu.")
    else:
        if board.guess(guess_x, guess_y):
            board.print_board()
            break
        if board.is_over():
            board.print_board()
            print("You won!!!")
            break
