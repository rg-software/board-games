from game_orchard import Game

game = Game()

colors = [".", "b", "r", "g"]


def print_cell(e):  # color_idx, score):
    color = colors[e.top()]
    scorestr = " "
    if e.score() > 0:
        scorestr = str(e.score())
    elif e.score() < 0:
        scorestr = "R"
    print(f"{color}{scorestr}".ljust(3), end="")


def print_board():
    for r in game.board:
        for e in r:
            print_cell(e)
        print()


def print_card(card):
    for r in card:
        for e in r:
            print(f"{colors[e]}".ljust(3), end="")
        print()


def print_all():
    print()
    print_board()
    print(f"Deck size: {len(game.deck)}, Score: {game.score()}")
    dicecolors = ["Rotten", "Blue", "Red", "Green"]
    dice = [f"{dicecolors[idx]}: {cnt}" for idx, cnt in enumerate(game.dicebox.dic)]
    print(f"Dice: {', '.join(dice)}")

    if game.hand[0]:
        print("Active hand:")
        print_card(game.hand[0])

    if game.hand[1]:
        print("Passive hand:")
        print_card(game.hand[1])


while not game.game_over():
    print_all()
    action = input("(s)wap hands, (r)otate card, or place at (row, col)? ")

    if action == "s":
        game.swap_cards()
    elif action == "r":
        game.rotate_card()
    else:
        rc = [int(e) for e in action.split()]
        if game.can_place(rc):
            game.place_card(rc)
        else:
            print("Cannot place this card here!")

print("Game over! Final results:")
print_all()
