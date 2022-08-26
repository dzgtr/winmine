import classes

col_count = 5
row_count = 5
minecount = 5

board = classes.Board(row_count, col_count, minecount)
board.create_board()
board.plant_on_board()
#board.print_board_test()
guess_x = 0
guess_y = 0

while True:
    board.print_board()
    print(board.remaining)
    func = int(input("0 pro klik, 1 pro flag/uncover:"))
    if func != 0 and func != 1:
        print("Zadej správné číslo funkce")
    else:
        guess_x = int(input("Zadej řádek:"))
        guess_y = int(input("Zadej sloupec:"))
        if guess_x >= col_count or guess_y >= row_count:
            print("Zadané souřadnice jsou mimo herní plochu.")
        else:
            if func == 0:
                if board.guess(guess_x, guess_y):
                    board.print_board()
                    break
                if board.is_over():
                    board.print_board()
                    print("You won!!!")
                    break
            elif func == 1:
                if board.flag_uncover(guess_x, guess_y):
                    board.print_board()
                    break
                if board.is_over():
                    board.print_board()
                    print("You won!!!")
                    break