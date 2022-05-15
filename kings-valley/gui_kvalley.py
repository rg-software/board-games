import pgzrun
from pgzero.builtins import Rect
from game_kvalley import Game, Pieces, Player

WIDTH = 400
HEIGHT = 400
TITLE = "King's Valley"

MARGIN = 75
STEP = 50
INPUT_Y = 350

DIRECTIONS = [
    ("N", "\u2B06"),
    ("NE", "\u2197"),
    ("E", "\u27A1"),
    ("SE", "\u2198"),
    ("S", "\u2B07"),
    ("SW", "\u2199"),
    ("W", "\u2B05"),
    ("NW", "\u2196"),
]

game = Game()
active_cell = None
active_dir = None


def draw_board():
    pieces = {
        Pieces.B_KING: "\u265A",
        Pieces.B_PAWN: "\u26C3",
        Pieces.W_KING: "\u2654",
        Pieces.W_PAWN: "\u26C1",
        Pieces.EMPTY: "",
    }

    for r in range(5):
        for c in range(5):
            piece = pieces[game.board[r][c]]
            pos = (MARGIN + c * STEP, MARGIN + r * STEP)
            rect = Rect(pos, (STEP, STEP))
            screen.draw.textbox(piece, rect, color="black", fontname="dejavu")
            screen.draw.rect(rect, color="black")


def player_name(p):
    return "White" if p == Player.WHITE else "Black"


def draw_player_info():
    pos = (150, 40)
    if game.winner() == Player.NONE:
        screen.draw.text(f"{player_name(game.player)} move", pos, color="black")
    else:
        screen.draw.text(f"Winner: {player_name(game.winner())}", pos, color="black")


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
    if r in range(5) and c in range(5):
        active_cell = (r, c)

    d = pos[0] // STEP
    if d in range(8) and INPUT_Y < pos[1] < INPUT_Y + STEP:
        active_dir = d

    if active_cell and active_dir is not None and game.winner() == Player.NONE:
        dir, _ = DIRECTIONS[active_dir]
        if game.move(active_cell[0], active_cell[1], dir):
            game.pass_turn()
            active_cell = None
            active_dir = None


pgzrun.go()
