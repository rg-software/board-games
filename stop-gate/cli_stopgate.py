from game_stopgate import Game, Cell

game = Game()


def print_game_board():
    charboard = [["." for _ in range(Game.BoardWidth)] for _ in range(Game.BoardHeight)]

    for r in range(Game.BoardHeight):
        for c in range(Game.BoardWidth):
            if game.board[r][c] == Cell.HORIZ:
                charboard[r][c] = "="
                charboard[r][c + 1] = "="
            if game.board[r][c] == Cell.VERT:
                charboard[r][c] = "#"
                charboard[r + 1][c] = "#"

    print()
    for r in range(Game.BoardHeight):
        print("".join(charboard[r]))


while not game.is_game_over():
    print_game_board()
    coords = input(f"{game.player_name()} move: ")
    r, c = coords.split()

    if game.can_place_at(int(r), int(c)):
        game.place_at(int(r), int(c))
        game.next_player()

print(f"Game over! {game.player_name()} player lost")
