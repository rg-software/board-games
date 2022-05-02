import pgzrun
from pgzero.builtins import Actor
from game_pig import Game

WIDTH = 600
HEIGHT = 300

btn_roll = Actor("btn_roll", (100, 200))
btn_end = Actor("btn_end", (300, 200))
pig = Game()


def draw_player_score(player, coords):
    c = "red" if player == pig.current_player else "black"
    points = pig.score[player]
    screen.draw.text(f"player {player + 1}: {points}", coords, color=c)


def draw():
    screen.fill("white")
    draw_player_score(0, (10, 0))
    draw_player_score(1, (10, 20))
    screen.draw.text(f"table: {pig.table}", (10, 40), color="black")
    screen.draw.text(f"dice: {pig.dice}", (10, 60), color="black")

    if pig.game_over():
        screen.draw.text("Game over!", (10, 80), color="black")
    else:
        btn_roll.draw()
        btn_end.draw()


def on_mouse_down(pos):
    if btn_roll.collidepoint(pos):
        pig.roll_dice()
        if pig.dice == 1:
            pig.pass_turn()

    if btn_end.collidepoint(pos):
        pig.pass_turn()


pgzrun.go()
