import pgzrun
from pgzero.builtins import Actor
import random

# from game_pig import Game
dice = [random.randint(0, 5), random.randint(0, 5)]
WIDTH = 800
HEIGHT = 600
TITLE = "Criss Cross"

btn_end = Actor("end", (300, 500))

syms = [
    "\U0001F354",
    "\U0001F35E",
    "\U0001F359",
    "\U0001F355",
    "\U0001F34C",
    "\U0001F349",
]


def print_die(pts, pos, color):

    screen.draw.text(syms[pts], pos, color=color, fontname="notoemoji", fontsize=40)


class Domino:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.dir_horiz = True

    def draw(self, x, y):

        screen.draw.textbox(
            syms[self.v1], Rect((x, y), (50, 50)), fontname="notoemoji", color="black"
        )

        dx = 50 * int(self.dir_horiz)
        dy = 50 * int(not self.dir_horiz)

        screen.draw.textbox(
            syms[self.v2],
            Rect((x + dx, y + dy), (50, 50)),
            fontname="notoemoji",
            color="black",
        )

    def flip(self):
        pass


dom_coords = (300, 50)
mydom = Domino(1, 4)


def draw():
    screen.fill("white")
    btn_end.draw()

    mydom.draw(dom_coords[0], dom_coords[1])

    print_die(dice[1], (100, 100), "red")
    print_die(dice[0], (150, 100), "red")


def on_mouse_down(pos, button):
    global dice
    if btn_end.collidepoint(pos):
        dice = [random.randint(0, 5), random.randint(0, 5)]

    if button == mouse.RIGHT:
        mydom.flip()


def on_mouse_move(pos, buttons):
    global dom_coords
    dom_coords = pos


pgzrun.go()
