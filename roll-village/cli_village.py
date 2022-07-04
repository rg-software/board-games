from game_crisscross import Game


game = Game()


def print_domino(d):
    values = [[str(d.v1), " "], [" ", " "]]
    values[int(not d.dir_horiz)][int(d.dir_horiz)] = str(d.v2)
    print(" ".join(values[0]))
    print(" ".join(values[1]))


def print_card():
    for r in game.card:
        print(" ".join(["." if v == 0 else str(v) for v in r]))


while not game.is_game_over():
    game.roll()
    while game.dice:
        print()
        print(f"Round: {game.round}, score: {game.card_score()}, rolled:")
        print_domino(game.dice)
        print("card:")
        print_card()
        action = input("(F)lip or place at (row, col): ")
        if action == "f":
            game.dice.flip()
        else:
            r, c = action.split()
            game.place(int(r), int(c))
            if game.dice:
                print("Incorrect placement, try again.")
