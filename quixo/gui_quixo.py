import pgzrun
from pgzero.builtins import Rect
from game_quixo import Game

WIDTH = 400
HEIGHT = 400
TITLE = "Quixo"

MARGIN = 75
STEP = 50
INPUT_Y = 350

DIRECTIONS = [
    ("b", "\u2B06"),
    ("l", "\u27A1"),
    ("t", "\u2B07"),
    ("r", "\u2B05"),
]

game = Game()
active_cell = None
active_dir = None


def draw_board():
    for r in range(5):
        for c in range(5):
            ch = " " if game.board[r][c] == "." else game.board[r][c]
            pos = (MARGIN + c * STEP, MARGIN + r * STEP)
            rect = Rect(pos, (STEP, STEP))
            screen.draw.textbox(ch, rect, color="black")
            screen.draw.rect(rect, color="black")


# def player_name(p):
#     return "White" if p == Player.WHITE else "Black"


def draw_player_info():
    pos = (150, 40)
    if not game.winner_char():
        screen.draw.text(f"{game.player_char} move", pos, color="black")
    else:
        screen.draw.text(f"Winner: {game.winner_char()}", pos, color="black")


def draw_active_cell():
    r, c = active_cell
    pos = (MARGIN + 2 + c * STEP, MARGIN + 2 + r * STEP)
    rect = Rect(pos, (STEP - 4, STEP - 4))
    screen.draw.rect(rect, color="red")


def draw_active_direction():
    pos = (2 + active_dir * STEP, INPUT_Y)
    rect = Rect(pos, (STEP - 4, STEP - 4))

    screen.draw.rect(rect, color="red")


def draw():
    screen.fill("white")

    draw_board()
    draw_player_info()

    if active_cell:
        draw_active_cell()

    if active_dir is not None:
        draw_active_direction()

    for i, (_, sym) in enumerate(DIRECTIONS):
        pos = (i * STEP, INPUT_Y)
        rect = Rect(pos, (STEP, STEP))
        screen.draw.textbox(sym, rect, color="black", fontname="dejavu")


def on_mouse_down(pos):
    global active_cell, active_dir

    r = (pos[1] - MARGIN) // STEP
    c = (pos[0] - MARGIN) // STEP

    in_board = r in range(5) and c in range(5)
    # in_board_core = r in range(1, 4) and c in range(1, 4)
    if in_board:  # and not in_board_core:
        active_cell = (r, c)

    d = pos[0] // STEP
    if d in range(8) and INPUT_Y < pos[1] < INPUT_Y + STEP:
        active_dir = d

    if active_cell and active_dir is not None and not game.winner_char():
        dir, _ = DIRECTIONS[active_dir]

        if game.push(active_cell[0], active_cell[1], dir):
            game.next_player()
        active_cell = None
        active_dir = None


pgzrun.go()
