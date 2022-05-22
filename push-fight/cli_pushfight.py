from game_pushfight import Game, Cell, GameState

game = Game()


def print_game_board():
    charboard = [["." for _ in range(Game.BoardWidth)] for _ in range(Game.BoardHeight)]

    for r in range(Game.BoardHeight):
        for c in range(Game.BoardWidth):
            if game.board[r][c] == Cell.LAVA:
                charboard[r][c] = " "
            if game.board[r][c] == Cell.EMPTY:                
                charboard[r][c] = "."
            if game.board[r][c] == Cell.WHITE_ROUND:                
                charboard[r][c] = "o"
            if game.board[r][c] == Cell.WHITE_SQUARE:            
                charboard[r][c] = "-"
            if game.board[r][c] == Cell.BROWN_ROUND:      
                charboard[r][c] = "*"
            if game.board[r][c] == Cell.BROWN_SQUARE:  
                charboard[r][c] = "="
            if game.board[r][c] == Cell.BROWN_ANCHOR:
                charboard[r][c] = "a"
            if game.board[r][c] == Cell.WHITE_ANCHOR:
                charboard[r][c] = "a"

    print()
    for r in range(Game.BoardHeight):
        print("".join(charboard[r]))


while not game.is_game_over():
    print_game_board()
    if game._state_is() == GameState.START:
        coords = input(f"Arrange piece: ")
        r, c = coords.split()
        game.starting_position(int(r), int(c))

    if game._state_is() == GameState.MOVE:
        coords = input(f"{game.player_name()} move: ")
        r, c = coords.split()
        if game.can_move_at(r, c): 
            game.move_at(r, c)            
        else: game.select_piece(r, c)
    if game._state_is() == GameState.PUSH:
        coords = input(f"{game.player_name()} push: ")
        r, c = coords.split()
        if game.can_push_at(r, c): 
            game.push_at(r, c)
        else: game.select_piece(r, c)


print(f"Game over! {game.player_name()} player lost")
