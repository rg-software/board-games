import pgzrun
from pgzero.builtins import Actor
from game_pig import Game

WIDTH = 400
HEIGHT = 300
TITLE = "Pig"

btn_roll = Actor("btn_roll", (100, 200))
btn_end = Actor("btn_end", (300, 200))
pig = Game()


def print_die(pts, pos, color):
    if pts:
        sym = chr(ord("\u2680") + pts - 1)
        screen.draw.text(sym, pos, color=color, fontname="dejavu", fontsize=60)


def draw_player_score(player, coords):
    c = "red" if player == pig.current_player else "black"
    pts = pig.score[player]
    screen.draw.circle(coords, 40, color=c)
    screen.draw.text(f"P {player + 1}\n {pts}", center=coords, color=c, align="center")


def draw():
    screen.fill("white")
    draw_player_score(0, (50, 50))
    draw_player_score(1, (150, 50))
    screen.draw.text(f"table: {pig.table}", (220, 20), color="black")

    print_die(pig.die, (220, 40), "black")

    if pig.game_over():
        screen.draw.text("Game over!", (10, 100), color="black")
    else:
        btn_roll.draw()
        btn_end.draw()


def on_mouse_down(pos):
    if not pig.game_over() and btn_roll.collidepoint(pos):
        pig.roll_die()
        if pig.die == 1:
            pig.pass_turn()

    if not pig.game_over() and btn_end.collidepoint(pos):
        pig.pass_turn()


pgzrun.go()
