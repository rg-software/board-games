from game_paletto import Game


def print_board(board):
    for r in range(1, 7):
        print(board.data[r][1:7])


def print_scorecard(card):
    scores = [f"{i}x{card[i]} " for i in range(1, 7)]
    print("score: " + "".join(scores))


game = Game()

while True:
    print()
    print_board(game.board)
    print(f"current player: {1 if game.p1_turn else 2}")
    print(f"current color: {game.current_color}")

    card = game.scorecards[game.p1_turn]
    print_scorecard(card)
    rc = input("your move (row col) [enter to end]: ")

    if not rc:
        if game.current_color == 0:
            print("at least one move should be made")
        else:
            game.end_turn()
    else:
        r, c = int(rc.split()[0]), int(rc.split()[1])

        if game.can_remove_at(r, c):
            game.remove_at(r, c)
        else:
            print("illegal move!")

    if game.game_over():
        print("Game over! You won.")
        break
