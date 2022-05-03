from game_nothanks import Game

game = Game()

while game.deck:
    print()
    for i, player in enumerate(game.players):
        print(f"Player {i + 1}. Tokens: {player.tokens}, Cards: {player.deck}")
    print(f"Active card: {game.deck[0]}")
    print(f"Cards in deck: {len(game.deck) - 1}")
    print(f"Tokens on table: {game.table_tokens}")
    print(f"Current player: {game.current_player + 1}")

    move = input("(P)ass or (T)ake? ")
    if move == "p" and game.can_pass():
        game.move_pass()
    elif move == "t":
        game.move_take()
    else:
        print("Incorrect move!")

print()
print("Game over!")
print("Final scores:")
for i, player in enumerate(game.players):
    print(f"Player {i + 1}. Score: {player.score()}")
