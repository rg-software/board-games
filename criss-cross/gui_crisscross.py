import pgzrun
from pgzero.builtins import Actor
import random

# from game_pig import Game
dice = [random.randint(0, 5), random.randint(0, 5)]
WIDTH = 400
HEIGHT = 300
TITLE = "Criss Cross"

btn_end = Actor("end", (300, 200))


def print_die(pts, pos, color):
    syms = [
        "\U0001F354",
        "\U0001F35E",
        "\U0001F359",
        "\U0001F355",
        "\U0001F34C",
        "\U0001F349",
    ]

    screen.draw.text(syms[pts], pos, color=color, fontname="notoemoji", fontsize=60)


def draw():
    screen.fill("white")
    btn_end.draw()

    print_die(dice[0], (200, 100), "red")
    print_die(dice[1], (100, 100), "red")


def on_mouse_down(pos):
    global dice
    if btn_end.collidepoint(pos):
        dice = [random.randint(0, 5), random.randint(0, 5)]


pgzrun.go()
