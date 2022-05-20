from game_blokusduo import Game, Cell

game = Game()


def print_game_board():
    charboard = [["." for _ in range(Game.BoardWidth)] for _ in range(Game.BoardHeight)]

    for r in range(Game.BoardHeight):
        for c in range(Game.BoardWidth):
            if game.board[r][c] == Cell.BLOCK_1:
                charboard[r][c] = "="
            if game.board[r][c] == Cell.BLOCK_2:
                charboard[r][c] = "#"

    print()
    for r in range(Game.BoardHeight):
        print("".join(charboard[r]))


while not game.is_game_over():
    print_game_board()
    coords = input(f"{game.player_name()} move: ")
    r, c, b = coords.split()

    if game.can_place_at(int(r), int(c), game.select_block(int(b))):        
        game.place_at(int(r), int(c))
        game.next_player()

print(f"Game over! {game.player_name()} player lost")
