import pgzrun
from pgzero.builtins import Rect, keys, mouse
from game_orchard import Game

WIDTH = 1000
HEIGHT = 750
TITLE = "Orchard"
CELLSIZE = 30
MARGIN = 50
RADIUS = 12

game = Game()
pointer = (0, 0)

# a circle with an optional number or "R" mark inside
def draw_cell(r, c, color_idx, score):
    colors = ["white", "cyan", "red", "green"]
    pos = (MARGIN + c * CELLSIZE + RADIUS, MARGIN + r * CELLSIZE + RADIUS)
    screen.draw.filled_circle(pos, RADIUS, colors[color_idx])
    screen.draw.circle(pos, RADIUS, "black")
    if score != 0:
        s = score if score > 0 else "R"
        screen.draw.text(f"{s}", center=pos, color="black")


def draw_card(card, rc):  # draw a 2x3 or 3x2 array
    row, col = rc
    x, y = MARGIN + col * CELLSIZE, MARGIN + row * CELLSIZE
    w, h = len(card[0]) * CELLSIZE, len(card) * CELLSIZE
    screen.draw.rect(Rect((x, y), (w, h)), "black")
    for r_idx, r in enumerate(card):
        for c_idx, e in enumerate(r):
            draw_cell(row + r_idx, col + c_idx, e, 0)


def draw_board():
    for r_idx, r in enumerate(game.board):
        for c_idx, e in enumerate(r):
            if e.has_data():
                draw_cell(r_idx, c_idx, e.top(), e.score())


def clamp(v, v_min, v_max):
    return max(v_min, min(v, v_max))


def rc_from_pointer(pos):
    r = clamp((pos[1] - MARGIN) // CELLSIZE, 0, Game.BOARDSIZE - 3)
    c = clamp((pos[0] - MARGIN) // CELLSIZE, 0, Game.BOARDSIZE - 3)
    return (r, c)


def draw():
    screen.fill("white")
    draw_board()

    screen.draw.text("Hand:", (800, 50), color="black")
    screen.draw.text(f"Deck: {len(game.deck)}", (800, 300), color="black")

    for r_idx, cnt in enumerate(game.dicebox.dice):
        draw_cell(10, Game.BOARDSIZE + 5 + r_idx, r_idx, cnt)

    screen.draw.text(f"Score: {game.score()}", (800, 400), color="black")

    if game.game_over():
        screen.draw.text("Game over!", (800, 420), color="black")

    if game.hand[0]:
        draw_card(game.hand[0], rc_from_pointer(pointer))

    if game.hand[1]:
        draw_card(game.hand[1], (1, Game.BOARDSIZE + 5))


def on_mouse_move(pos):
    global pointer
    pointer = pos


def on_key_down(key):
    if key == keys.TAB and not game.game_over():
        game.swap_cards()


def on_mouse_down(pos, button):
    if not game.game_over():
        if button == mouse.RIGHT:
            game.rotate_card()
        elif game.can_place(rc_from_pointer(pos)):
            game.place_card(rc_from_pointer(pos))


pgzrun.go()
