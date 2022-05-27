from game_pushfight import Game, GameState, Piece, PieceColor, PieceShape

game = Game()


def empty_char(cell, r, c):
    if cell.is_lava:
        return "+"
    if r < 0 or game.state != GameState.START:
        return "."
    return (
        "/" if c in Piece(PieceColor.WHITE, PieceShape.SQUARE).start_columns() else "\\"
    )


def piece_char(cell):
    chars = {
        (PieceColor.WHITE, PieceShape.ROUND): "O",
        (PieceColor.BROWN, PieceShape.ROUND): "o",
        (PieceColor.WHITE, PieceShape.SQUARE): "U",
        (PieceColor.BROWN, PieceShape.SQUARE): "u",
        PieceColor.WHITE: "A",
        PieceColor.BROWN: "a",
    }

    return chars[cell.color] if cell.has_anchor else chars[(cell.color, cell.shape)]


def print_board_cell(cell, r, c):
    c = piece_char(cell) if cell.is_piece else empty_char(cell, r, c)
    print(c, end=" ")


def print_game_board():
    print("  " + " ".join([str(c) for c in range(10)]))

    for r in range(4):
        print(r, end=" ")
        for c in range(10):
            print_board_cell(game.board[r][c], r, c)
        print()


while not game.is_game_over():
    print()
    print_game_board()

    if game.game_state() == GameState.START:
        coords = input(f"Position the piece {piece_char(game.box_top())} (r, c): ")
        r, c = coords.split()
        game.place_new_piece(int(r), int(c))

    elif game.game_state() == GameState.MOVE:
        print(f"{game.player_name()}. Moves: {game.moves_left()}")
        if (action := input("Move from (r1, c1) to (r2, c2) or (S)kip: ")) == "s":
            game.move_done(game.moves_left())
        else:
            r1, c1, r2, c2 = [int(x) for x in action.split()]
            game.select_piece(r1, c1)
            if game.can_move_at(r2, c2):
                game.move_at(r2, c2)

    elif game.game_state() == GameState.PUSH:
        print(f"{game.player_name()}. Push!")
        action = input("From (r1, c1) to (r2, c2): ")
        r1, c1, r2, c2 = [int(x) for x in action.split()]
        game.select_piece(r1, c1)
        if (pieces := game.can_push_pieces(r2, c2)) > 1:
            game.push_at(r2, c2, pieces)

print(f"Game over! {game.player_name()} player lost")
