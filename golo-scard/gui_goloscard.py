import pgzrun
from pgzero.builtins import Actor, Rect
from game_goloscard import Game

WIDTH = 400
HEIGHT = 300
TITLE = "GOLO (Scorecard)"

btn_roll = Actor("btn_roll", (200, 200))
golo = Game([5, 4, 3, 4, 4, 3, 4, 4, 5])

CELL = 40
MARGIN = 20
Y_INPUT = 100

indices = set()


def draw():
    screen.fill("white")
    hole = min(9, 10 - len(golo.dice))
    screen.draw.text(f"Hole: {hole}", (20, 10), color="black")
    screen.draw.text(f"Target: {sum(golo.scorecard)}", (100, 10), color="black")

    colors = {3: "red", 4: "gray", 5: "blue"}

    for i, par in enumerate(golo.scorecard):
        rect = Rect((20 + i * 20, 30), (20, 20))
        screen.draw.textbox(str(par), rect, color=colors[par])
        screen.draw.rect(rect, color="black")

    for i, v in enumerate(golo.rolled):
        par, _ = golo.dice[i]
        rect = Rect((MARGIN + i * CELL, Y_INPUT), (CELL, CELL))
        c = "green" if i in indices else "black"
        screen.draw.textbox(str(v), rect, color=colors[par])
        screen.draw.rect(rect, color=c)

    if not golo.dice:
        screen.draw.text(f"Final score: {golo.score}", (10, 100), color="black")

    btn_roll.draw()


def on_mouse_down(pos):
    global indices

    i = (pos[0] - MARGIN) // CELL
    if pos[1] in range(50, Y_INPUT + CELL) and i in range(len(golo.dice)):
        new_indices = indices ^ set([i])
        if not new_indices or golo.can_remove(new_indices):
            indices ^= set([i])

    if golo.dice and indices and btn_roll.collidepoint(pos):
        golo.remove(indices)
        indices = set()
        golo.roll()


golo.roll()
pgzrun.go()
