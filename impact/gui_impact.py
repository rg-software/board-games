import pgzrun
from pgzero.builtins import Actor
from game_impact import Game

WIDTH = 450
HEIGHT = 300
TITLE = "Impact"

btn_roll = Actor("btn_roll", (100, 200))
btn_end = Actor("btn_end", (300, 200))
btn_resolve = Actor("btn_resolve", (200, 200))
resolve_phase = False
game = Game()


def die(pts):
    return chr(ord("\u2680") + pts - 1)


def draw_player_score(player, coords):
    c = "red" if player == game.current_player else "black"
    screen.draw.circle(coords, 40, color=c)
    screen.draw.text(f"P {player + 1}\n{game.dice[player]}", center=coords, color=c)


def draw_dice(dice, pos, color):
    dice = "".join([die(v) for v in dice])
    screen.draw.text(dice, center=pos, color=color, fontname="dejavu", fontsize=40)


def draw():
    screen.fill("white")
    draw_player_score(0, (50, 40))
    draw_player_score(1, (350, 40))
    screen.draw.text("ARENA", center=(200, 70), color="black")

    draw_dice(game.arena, (200, 100), "black")

    if resolve_phase:
        btn_resolve.draw()
    elif game.game_over():
        screen.draw.text("Game over!", (10, 100), color="black")
    else:
        btn_roll.draw()
        btn_end.draw()


def on_mouse_down(pos):
    global resolve_phase

    if btn_resolve.collidepoint(pos) and resolve_phase:
        resolve_phase = not resolve_phase
        if game.resolve():
            game.pass_turn()
    elif not game.game_over() and btn_roll.collidepoint(pos):
        game.roll()
        resolve_phase = not resolve_phase
    elif not game.game_over() and btn_end.collidepoint(pos):
        game.pass_turn()


pgzrun.go()
