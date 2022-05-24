import pgzrun
from pgzero.builtins import Rect
from game_pushfight import Game, GameState, Piece, PieceColor, PieceShape


def px(col, row, margin=0):
    return (CELLSIZE * col + margin, CELLSIZE * row + margin)


CELLSIZE = 70  # px
MARGIN = 5  # inside cells
WIDTH, HEIGHT = px(Game.BoardWidth + 2, Game.BoardHeight + 3)
TITLE = "Push Fight"

game = Game()
btn_skip_rect = Rect(px(6.2, 1.2), px(1, 0.5))


def draw_skip_button():
    screen.draw.filled_rect(btn_skip_rect, "grey 54")
    screen.draw.textbox("Skip", btn_skip_rect, color="black")


def draw_cell(r, c, color):
    rect = Rect(px(c + 1, r + 2, MARGIN), px(1, 1, -MARGIN))
    screen.draw.filled_rect(rect, color)


def draw_square(r, c, color_b, color_t, color_a):
    rect = Rect(px(c + 1, r + 2, MARGIN * 1.5), px(1, 1, -MARGIN * 2))
    rect2 = Rect(px(c + 1, r + 2, MARGIN * 2), px(1, 1, -MARGIN * 3))
    rect3 = Rect(px(c + 1, r + 2, MARGIN * 3), px(1, 1, -MARGIN * 5))
    screen.draw.filled_rect(rect, color_a)
    screen.draw.filled_rect(rect2, color_b)
    screen.draw.filled_rect(rect3, color_t)


def draw_anchor(r, c, clr):
    screen.draw.filled_circle(px(c + 1.5, r + 2.5, MARGIN / 2), CELLSIZE / 3, clr)


def draw_round(r, c, color_b, color_t, color_a):
    rect = Rect(px(c + 1, r + 2, MARGIN * 1.5), px(1, 1, -MARGIN * 2))
    rect2 = Rect(px(c + 1, r + 2, MARGIN * 2), px(1, 1, -MARGIN * 3))
    screen.draw.filled_rect(rect, color_a)
    screen.draw.filled_rect(rect2, color_b)
    draw_anchor(r, c, color_t)


def draw_piece(r, c, cell):
    colors = {
        PieceColor.WHITE: ("white", "gray 85"),
        PieceColor.BROWN: ("tan", "dark red"),
    }

    color_a = "gray 42"
    color_b, color_t = colors[cell.color]

    if cell.shape == PieceShape.ROUND:
        draw_round(r, c, color_b, color_t, color_a)
    if cell.shape == PieceShape.SQUARE:
        draw_square(r, c, color_b, color_t, color_a)
    if cell.has_anchor:
        draw_anchor(r, c, "red")


def cell_color(cell, state, is_selected, r, c):
    if is_selected:
        return "light green"
    if not cell.is_piece and cell.is_lava:
        return "orange"
    if r < 0 or state != GameState.START:
        return "gray"
    return (
        "light blue"
        if c in Piece(PieceColor.WHITE, PieceShape.SQUARE).start_columns()
        else "light salmon"
    )


def draw_board_cell(cell, r, c):
    sc = cell_color(cell, game.game_state(), game.selected_cell() == (r, c), r, c)
    draw_cell(r, c, sc)

    if cell.is_piece:
        draw_piece(r, c, cell)


def draw_info(text):
    screen.draw.textbox(text, Rect(px(3, 1.2), px(3, 0.5)), color="grey 89")


def draw():
    screen.fill("grey 23")

    for i in range(1, 12):
        screen.draw.line(px(i, 2), px(i, Game.BoardHeight + 2), "light gray")

    for i in range(1, 6):
        screen.draw.line(px(1, i + 1), px(Game.BoardWidth + 1, i + 1), "light gray")

    for r in range(4):
        for c in range(10):
            draw_board_cell(game.board[r][c], r, c)

    if game.game_state() == GameState.START:
        draw_board_cell(game.box_top(), -1, 5)
        draw_info("Position the piece:")

    if game.game_state() == GameState.MOVE:
        draw_skip_button()
        draw_info(f"{game.player_name()}. Moves: {game.moves_left()}")

    if game.game_state() == GameState.PUSH:
        draw_info(f"{game.player_name()}. Push!")

    if game.is_game_over():
        draw_info(f"Game over! {game.player_name()} lost")


def on_mouse_down(pos):
    r = pos[1] // CELLSIZE - 2
    c = pos[0] // CELLSIZE - 1

    if game.game_state() == GameState.START and game.on_board(r, c):
        game.place_new_piece(r, c)

    if game.game_state() == GameState.MOVE:
        if btn_skip_rect.collidepoint(pos):
            game.move_done(game.moves_left())
        elif game.can_move_at(r, c):  # must be selected
            game.move_at(r, c)
        elif game.on_board(r, c):
            game.select_piece(r, c)

    if game.game_state() == GameState.PUSH:
        if (pieces := game.can_push_pieces(r, c)) > 1:  # must be selected
            game.push_at(r, c, pieces)
        else:
            game.select_piece(r, c)


pgzrun.go()
