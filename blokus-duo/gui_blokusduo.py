import pgzrun
from pgzero.builtins import Actor, Rect
from game_blokusduo import Game, Cell

CELL = 50
MARGIN = 10
ROW = 14
COLUMN = 14
WIDTH = Game.BoardWidth * CELL + CELL * 7
HEIGHT = Game.BoardHeight * CELL + 1
TITLE = "Blokus Duo"

btn_previous = Actor("btn_previous", (CELL * ROW + CELL + CELL / 2, CELL * 10))
btn_rotate = Actor("btn_rotate", (CELL * ROW + CELL + CELL / 2 + 70, CELL * 10))
btn_flip = Actor("btn_flip", (CELL * ROW + CELL + CELL / 2 + 70 * 2, CELL * 10))
btn_next = Actor("btn_next", (CELL * ROW + CELL + CELL / 2 + 70 * 3, CELL * 10))

game = Game()
block_idx = 0


def draw_cell(r, c, color):
    pos = (c * CELL + MARGIN, r * CELL + MARGIN)
    screen.draw.filled_rect(Rect(pos, (CELL - 2 * MARGIN, CELL - 2 * MARGIN)), color)


def draw_hint(r, c):
    pos = (c * CELL + CELL / 2, r * CELL + CELL / 2)
    screen.draw.filled_circle(pos, MARGIN * 2, "light gray")


def draw_hints(block):
    coord = game.hints(block)
    for r, c in coord:
        draw_hint(r, c)


def draw_block(r, c, block, color):
    for dr, dc in block.coord():
        draw_cell(r + dr, c + dc, color)


def blockcolor(b):
    return "white" if b == Cell.BLOCK_1 else ("black" if b == Cell.BLOCK_2 else "gray")


def draw_info(msg, color):
    textpos = (CELL * ROW + CELL * 3, CELL * 3)  # (CELL * 3, CELL * ROW + CELL * 3)
    screen.draw.text(msg, center=textpos, fontsize=32, color=color)


def draw():
    screen.fill("gray")

    for i in range(1, ROW + 1):
        screen.draw.line((CELL * i, 0), (CELL * i, HEIGHT), "white")
    for i in range(1, COLUMN + 1):
        screen.draw.line((0, CELL * i), (CELL * COLUMN, CELL * i), "white")

    for r in range(ROW):
        for c in range(COLUMN):
            draw_cell(r, c, blockcolor(game.board[r][c]))

    if game.is_game_over():
        draw_info(f"Game over!\n{game.player_name()} lost", "red")
    else:
        draw_info(f"{game.player_name()}", "black")

    draw_block(4, 15, game.get_block(block_idx), game.player_color())
    draw_hints(game.get_block(block_idx))

    btn_previous.draw()
    btn_rotate.draw()
    btn_flip.draw()
    btn_next.draw()


def on_mouse_down(pos):
    global block_idx

    r = pos[1] // CELL
    c = pos[0] // CELL
    block = game.get_block(block_idx)
    if game.can_place_at(r, c, block):
        game.place_at(r, c, block)
        game.next_player()
        block_idx = 0

    if btn_rotate.collidepoint(pos):
        game.rotate_block(block_idx)
    if btn_flip.collidepoint(pos):
        game.flip_block(block_idx)
    if btn_next.collidepoint(pos):
        block_idx = game.next_block(block_idx)
    if btn_previous.collidepoint(pos):
        block_idx = game.prev_block(block_idx)


pgzrun.go()
