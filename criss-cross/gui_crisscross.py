import pgzrun
from pgzero.builtins import Actor, Rect, mouse
from game_crisscross import Game

WIDTH = 350
HEIGHT = 500
TITLE = "Criss Cross"

SIZE = 50
CARD_Y = int(150 / 50)
btn_roll = Actor("btn_roll", (100, 60))
cursor_coords = (0, 0)
game = Game()


def drawcell(r, c, value, color):
    syms = [
        "",
        "\U0001F354",  # various food types
        "\U0001F35E",
        "\U0001F359",
        "\U0001F355",
        "\U0001F34C",
        "\U0001F349",
    ]
    x = SIZE * c
    y = SIZE * r

    rect = Rect((x, y), (SIZE, SIZE))
    screen.draw.textbox(syms[value], rect, fontname="notoemoji", color=color)
    screen.draw.rect(rect, color=color)


def draw_domino(r, c, domino):
    drawcell(r, c, domino.v1, "red")
    drawcell(r + int(not domino.dir_horiz), c + int(domino.dir_horiz), domino.v2, "red")


def draw():
    screen.fill("white")
    btn_roll.draw()
    screen.draw.text(f"Round: {game.round}", (70, 120), color="black")
    for r in range(5):
        for c in range(5):
            drawcell(r + CARD_Y, c, game.card[r][c], "black")
    if game.dice:
        cur_r = min(CARD_Y + 4, max(CARD_Y, cursor_coords[0]))  # clamp coords
        cur_c = min(4, max(0, cursor_coords[1]))
        draw_domino(cur_r, cur_c, game.dice)

    screen.draw.text(f"Current score: {game.card_score()}", (10, 430), color="black")
    if game.is_game_over():
        screen.draw.text("Game over!", (10, 470), color="red")


def on_mouse_down(pos, button):
    if btn_roll.collidepoint(pos) and not game.dice and not game.is_game_over():
        game.roll()
        return

    if button == mouse.RIGHT and game.dice:
        game.dice.flip()
    if button == mouse.LEFT and game.dice:
        r, c = cursor_coords
        game.place(max(0, r - CARD_Y), max(0, c))


def on_mouse_move(pos):
    global cursor_coords

    r = (pos[1]) // SIZE
    c = pos[0] // SIZE
    cursor_coords = (r, c)


pgzrun.go()
