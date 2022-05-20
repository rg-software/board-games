import pgzrun
from pgzero.builtins import Actor, Rect
from game_scc import Game

WIDTH = 400
HEIGHT = 300
TITLE = "Ship, Captain, and Crew"
DICE_Y = 90
DSIZE = 40

btn_roll = Actor("btn_roll", (100, 200))
btn_end = Actor("btn_end", (300, 200))
scc = Game()
roll = 0
hold34 = [False] * 5


def print_dice(pos, color):
    for i, pts in enumerate(scc.dice):
        s = chr(ord("\u2680") + pts - 1)
        screen.draw.textbox(s, Rect(pos, (50, 50)), color=color, fontname="dejavu")
        if i < scc.hold_idx() or hold34[i]:
            screen.draw.rect(Rect((pos[0] + 5, pos[1] + 5), (40, 40)), color="green")
        pos = (pos[0] + DSIZE, pos[1])
        # s = [chr(ord("\u2680") + pts - 1) for pts in scc.dice]

        # screen.draw.text("".join(s), pos, color=color, fontname="dejavu", fontsize=60)


def draw_player_score(player, coords):
    c = "red" if player == scc.current_player else "black"
    r = f"({roll})" if (player == scc.current_player and roll > 0) else ""
    pts = scc.score[player]
    screen.draw.circle(coords, 40, color=c)
    screen.draw.text(f"P{player+1} {r}\n{pts}", center=coords, color=c, align="center")


def turn_finished():
    return roll == 3


def turn_started():
    return roll > 0


def draw():
    screen.fill("white")
    draw_player_score(0, (50, 50))
    draw_player_score(1, (150, 50))
    screen.draw.text(f"round: {scc.turn // 2 + 1}", (220, 20), color="black")

    if scc.dice[0]:
        print_dice((0, DICE_Y), "black")

    if scc.game_over():
        screen.draw.text("Game over!", (10, 100), color="black")
    else:
        if not turn_finished():
            btn_roll.draw()
        if turn_started():
            btn_end.draw()


def on_mouse_down(pos):
    global roll

    if not scc.game_over():
        if btn_end.collidepoint(pos) and turn_started():
            roll = 0
            scc.end_turn()
        if btn_roll.collidepoint(pos) and not turn_finished():
            roll += 1
            scc.roll_dice(hold34[3], hold34[4])
            hold34[3] = hold34[4] = False

        if DICE_Y < pos[1] < DICE_Y + DSIZE:
            idx = pos[0] // DSIZE
            if idx in (3, 4) and scc.hold_idx() == 3 and not turn_finished():
                hold34[idx] = not hold34[idx]


pgzrun.go()
