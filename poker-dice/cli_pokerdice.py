from game_pokerdice import Game

game = Game()


def hand_string(hand):
    dice_values = ["9", "10", "J", "Q", "K", "A"]
    items = [f"({i}: {dice_values[hand[i]]})" for i in range(5)]
    return ", ".join(items)


def player_roll():
    print()
    print(f"current player: {game.current_player_idx + 1}")
    print(f"rolls left: {game.current_player().rolls_left}")

    game.current_player().roll_dice()
    game.current_player().unfreeze_all()
    print("hand: " + hand_string(game.current_player().hand))

    if not game.current_player().can_roll() or input("roll again (y/n)? ") == "n":
        return False

    to_freeze = input("will freeze: ")
    for i in to_freeze.split():
        game.current_player().freeze(int(i))

    return True


while not game.is_game_over():
    while player_roll():
        pass

    print(f"final hand: {game.current_player().hand_name()}")
    game.next_player()

if game.players[0].hand_better_than(game.players[1]):
    print("Player 1 wins")
elif game.players[1].hand_better_than(game.players[0]):
    print("Player 2 wins")
else:
    print("Draw")
