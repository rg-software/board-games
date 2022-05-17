import pgzrun
from pgzero.builtins import Actor, Rect
from game_golo import Game

WIDTH = 400
HEIGHT = 300
TITLE = "GOLO"

btn_roll = Actor("btn_roll", (200, 200))
golo = Game()

CELL = 40
MARGIN = 20
indices = set()


def draw():
    screen.fill("white")

    if not golo.dice:
        screen.draw.text(f"Final score: {golo.score}", (10, 100), color="black")

    for i, v in enumerate(golo.rolled):
        rect = Rect((MARGIN + i * CELL, 50), (CELL, CELL))
        c = "red" if i in indices else "black"
        screen.draw.textbox(str(v), rect, color=c)
        screen.draw.rect(rect, color=c)

    btn_roll.draw()


def on_mouse_down(pos):
    global indices

    i = (pos[0] - MARGIN) // CELL
    if pos[1] in range(50, 50 + CELL) and i in range(len(golo.dice)):
        new_indices = indices ^ set([i])
        if not new_indices or golo.can_remove(new_indices):
            indices ^= set([i])

    if golo.dice and indices and btn_roll.collidepoint(pos):
        golo.remove(indices)
        indices = set()
        golo.roll()


golo.roll()
pgzrun.go()
