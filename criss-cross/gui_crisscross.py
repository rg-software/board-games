import pgzrun
from pgzero.builtins import Actor
import random

# from game_pig import Game
# dice = [random.randint(0, 5), random.randint(0, 5)]
WIDTH = 800
HEIGHT = 600
TITLE = "Criss Cross"

SIZE = 50
btn_end = Actor("end", (300, 500))

syms = [
    "",
    "\U0001F354",
    "\U0001F35E",
    "\U0001F359",
    "\U0001F355",
    "\U0001F34C",
    "\U0001F349",
]


# def print_die(pts, pos, color):
#     screen.draw.text(syms[pts], pos, color=color, fontname="notoemoji", fontsize=40)


class Domino:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.dir_horiz = True

    def draw(self, r, c):
        x = SIZE * c
        y = SIZE * r
        screen.draw.textbox(
            syms[self.v1],
            Rect((x, y), (SIZE, SIZE)),
            fontname="notoemoji",
            color="black",
        )

        dx = SIZE * int(self.dir_horiz)
        dy = SIZE * int(not self.dir_horiz)

        screen.draw.textbox(
            syms[self.v2],
            Rect((x + dx, y + dy), (SIZE, SIZE)),
            fontname="notoemoji",
            color="black",
        )

    def flip(self):
        if self.dir_horiz:
            self.dir_horiz = False
            self.v1, self.v2 = self.v2, self.v1
        else:
            self.dir_horiz = True


dice_coords = (0, 0)
dice = Domino(random.randint(1, 6), random.randint(1, 6))

card = [[0 for _ in range(5)] for _ in range(5)]


def draw():
    screen.fill("white")
    btn_end.draw()

    dice.draw(dice_coords[0], dice_coords[1])

    # print_die(dice[1], (100, 100), "red")
    # print_die(dice[0], (150, 100), "red")


def on_mouse_down(pos, button):
    global dice
    if btn_end.collidepoint(pos):
        dice = Domino(random.randint(1, 6), random.randint(1, 6))

    if button == mouse.RIGHT:
        dice.flip()
    if button == mouse.LEFT:
        r, c = dice_coords
        card[r][c] = dice.v1
        card[r + int(not dice.dir_horiz)][c + int(dice.dir_horiz)] = dice.v2


def on_mouse_move(pos, buttons):
    global dice_coords

    r = int(pos[1] / SIZE)
    c = int(pos[0] / SIZE)
    # print(r, c)
    dice_coords = (r, c)
    # (SIZE * int(pos[0] / SIZE), SIZE * int(pos[1] / SIZE))


pgzrun.go()
