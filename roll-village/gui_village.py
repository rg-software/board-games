import pgzrun
from pgzero.builtins import Actor, Rect, mouse
from game_village import Game

WIDTH = 300
HEIGHT = 500
TITLE = "Rolling Village"

SIZE = 50
CARD_Y = int(150 / 50)
btn_roll = Actor("btn_roll", (90, 60))
cursor_coords = (0, 0)
game = Game()
project = 1
# projects = [1, 2, 3]


def draw_dice(x, y, dice):
    d1 = chr(ord("\u2680") + dice[0] - 1)
    d2 = chr(ord("\u2680") + dice[1] - 1)
    screen.draw.text(f"{d1}{d2}", (x, y), color="black", fontname="dejavu", fontsize=60)


def drawproject(c, r, value, color):
    syms = ["", "\U0001F3E0", "\U0001F332", "\u26F5", "\u26F2"]
    x = SIZE * c
    y = SIZE * r

    rect = Rect((x, y), (SIZE, SIZE))
    screen.draw.textbox(syms[value], rect, fontname="notoemoji", color=color)
    screen.draw.rect(rect, color=color)


def drawpoints(c, r, value, color):
    syms = ["", "1", "2", "3"]
    x = SIZE * c
    y = SIZE * r

    rect = Rect((x, y), (SIZE, SIZE))
    screen.draw.text(syms[value], (x + 5, y + 5), color=color)
    screen.draw.rect(rect, color=color)


def draw():
    screen.fill("white")
    btn_roll.draw()
    screen.draw.text(f"Round: {game.round}", (70, 120), color="black")
    for x in range(6):
        for y in range(5):
            drawpoints(x, y + CARD_Y, game.cardp[x][y], "black")
            drawproject(x, y + CARD_Y, game.card[x][y], "black")

    drawproject(cursor_coords[0], cursor_coords[1] + CARD_Y, project, "red")

    if game.dice[0]:
        # cur_r = min(CARD_Y + 4, max(CARD_Y, cursor_coords[0]))  # clamp coords
        # cur_c = min(4, max(0, cursor_coords[1]))
        draw_dice(190, 30, game.dice)

    #screen.draw.text(f"Current score: {game.card_score()}", (10, 430), color="black")
    # if game.is_game_over():
    #    screen.draw.text("Game over!", (10, 470), color="red")


def on_mouse_down(pos, button):
    if btn_roll.collidepoint(pos):  # and not game.dice:  # and not game.is_game_over():
        game.roll()
        return

    global project
    if button == mouse.RIGHT:
        project += 1
        if project == 5:
            project = 1

    if button == mouse.LEFT:
        c, r = cursor_coords
        # r = (pos[1]) // SIZE - CARD_Y
        # c = pos[0] // SIZE
        game.card[c][r] = project

    #    game.dice.flip()
    # if button == mouse.LEFT and game.dice:
    #    r, c = cursor_coords
    #    game.place(max(0, r - CARD_Y), max(0, c))


def on_mouse_move(pos):
    global cursor_coords

    r = (pos[1]) // SIZE - CARD_Y
    c = pos[0] // SIZE

    r = max([0, min([r, 4])])
    cursor_coords = (c, r)


pgzrun.go()
