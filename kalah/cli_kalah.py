from game_kalah import Game

kalah = Game()


def print_board(board):
    def print_row(rowrange, is_top):
        r1 = "   " + " ".join(f"{r:<2}" for r in rowrange)
        r2 = "   " + " ".join(f"{board[r]:02}" for r in rowrange)
        if not is_top:
            r1, r2 = r2, r1
        print(r1)
        print(r2)

    print_row(range(13, 7, -1), True)
    print(f"{board[0]:02}" + "   " * 6 + f" {board[7]:02}")
    print_row(range(1, 7), False)


while not kalah.is_end_game():
    print()
    print_board(kalah.board)
    print(f"your move [{kalah.my_houses()[0]}-{kalah.my_houses()[-1]}]:")

    house_no = int(input())
    if house_no in kalah.my_houses() and kalah.board[house_no] > 0:
        kalah.make_move(house_no)

kalah.capture_remaining()
