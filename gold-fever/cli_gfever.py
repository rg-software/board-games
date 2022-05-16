from game_gfever import Game, Stone

game = Game()

while 5 not in [game.player().score, game.opponent().score]:
    print()
    for i, player in enumerate(game.players):
        print(f"Player {i + 1}. Score: {player.score}")
    print(f"Table: {', '.join([s.name for s in game.table_stones])}")
    print(f"Current player: {game.current_player + 1}")

    move = input("(D)raw or (E)nd? ")
    if move == "d":
        stone, r = game.draw_stone()
        print(f"Got: {stone.name}")
        if not r:
            print("Passing turn!")
            opp_stone = game.resolve(stone)
            if stone == Stone.BLACK and opp_stone:
                print(f"Got from opponent: {opp_stone.name}")

    elif move == "e" and game.table_stones:
        game.end_turn()
    else:
        print("Incorrect move!")

print()
print("Game over!")
print("Final scores:")
for i, player in enumerate(game.players):
    print(f"Player {i + 1}. Score: {player.score}")
