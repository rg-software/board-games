from game_impact import Game

game = Game()

while not game.game_over():
    print()
    print(f"arena: {game.arena}")
    print(f"players' dice: {game.dice}")
    print(f"current player: {game.current_player + 1}")

    game.roll()
    print(f"rolling! new arena: {game.arena}")

    if (r := game.resolve()) or input("no matches! continue (y/n)? ") == "n":
        print(f"obtained dice: {r},  passing turn")
        game.pass_turn()

print(f"Game over! Final dice: {game.dice}")
