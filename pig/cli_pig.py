from game_pig import Game

pig = Game()

while not pig.game_over():
    pig.roll_die()

    print()
    print(f"score: {pig.score}")
    print(f"current player: {pig.current_player + 1}")
    print(f"table: {pig.table}")
    print(f"dice: {pig.die}")

    if pig.die == 1 or input("continue (y/n)? ") == "n":
        print("passing turn to another player!")
        pig.pass_turn()

print(f"final score: {pig.score}")
