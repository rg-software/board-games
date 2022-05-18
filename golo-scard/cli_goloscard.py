from game_goloscard import Game

golo = Game([5, 4, 3, 4, 4, 3, 4, 4, 5])


def input_indices():
    indices = input(f"remove values (0-{len(golo.rolled)-1}): ")
    return [int(i) for i in indices.split()]


def print_dice():
    for (v, dice) in zip(golo.rolled, golo.dice):
        print(f"{dice[0]}:{v} ", end="")
    print()


while golo.dice:
    golo.roll()

    print()
    hole = 10 - len(golo.dice)
    print(f"Hole: {hole}, scorecard: {golo.scorecard}, target: {sum(golo.scorecard)}")
    print_dice()
    while (indices := input_indices()) and not golo.can_remove(indices):
        print("Must remove allowed dice only!")
    golo.remove(indices)


print(f"final score: {golo.score}")
