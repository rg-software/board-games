from game_golo import Game

golo = Game()


def input_indices():
    indices = input(f"remove values (0-{len(golo.rolled)-1}): ")
    return [int(i) for i in indices.split()]


while golo.dice:
    golo.roll()

    print()
    print(f"dice: {golo.rolled}")
    while (indices := input_indices()) and not golo.can_remove(indices):
        print("Must remove the smallest values!")  # enforce the lowest-scores rule
    golo.remove(indices)


print(f"final score: {golo.score}")
