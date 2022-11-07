import classes

row_count = 5
col_count = 10
minecount = 5

board = classes.Board(row_count, col_count, minecount)
board.create_board()
board.plant_on_board()
# board.print_board_test()
guess_y = 0
guess_x = 0

while True:
    board.print_board()
    print(f"Remaining fields: {board.remaining_fields}")
    print(f"Remaining flags: {board.remaining_flags}")
    func = int(input("0 pro klik, 1 pro flag/uncover:"))
    if func != 0 and func != 1:
        print("Zadej správné číslo funkce")
    else:
        guess_y = int(input("Zadej řádek:"))
        guess_x = int(input("Zadej sloupec:"))
        if guess_y not in range(0, row_count) or guess_x not in range(0, col_count):
            print("Zadané souřadnice jsou mimo herní plochu.")
        else:
            if func == 0:
                if board.guess(guess_y, guess_x):
                    board.print_board()
                    print("You lost")
                    break
                if board.is_over():
                    board.print_board()
                    print("You won!!!")
                    break
            elif func == 1:
                uncover_lost_field = board.flag_uncover(guess_y, guess_x)
                if uncover_lost_field is not None:
                    print("You lost")
                    print(uncover_lost_field)
                    board.print_board()
                    break
                if board.is_over():
                    board.print_board()
                    print("You won!!!")
                    break
