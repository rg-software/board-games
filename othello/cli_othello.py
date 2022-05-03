from game_othello import Game

game = Game()


def print_board():
    for r in range(8):
        for c in range(8):
            if game.board[r][c] is True:
                print("O", end="")
            elif game.board[r][c] is False:
                print("#", end="")
            else:
                print(".", end="")
        print()

    print(f"White = {game.count_pieces(True)}")
    print(f"Black = {game.count_pieces(False)}")
    print(f"Current move: {game.player_name()}")
    print()


while True:
    print_board()
    rclist = input("your move (row, col): ").split()
    r = int(rclist[0])
    c = int(rclist[1])

    if not game.move_allowed(r, c):
        print("Illegal move!")
        continue

    game.move(r, c)
    if not game.has_legal_moves():
        game.pass_move()

        if game.has_legal_moves():
            print("Cannot move. Passing turn to the opponent")
        else:
            print("Game over!")
            break
