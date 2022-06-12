from game_quixo import Game

game = Game()


def print_board(board):
    for r in range(5):
        print("".join([board[r][c] for c in range(5)]))


while not game.winner_char():  # game_over():
    print(f"player: {game.player_char}")
    print_board(game.board)
    v = input("Your move (r, c, dir): ").split()
    if game.push(int(v[0]), int(v[1]), v[2]):
        game.next_player()
    else:
        print("Illegal move!")

print_board(game.board)
print(f"Game over! Player '{game.winner_char()}' wins.")
