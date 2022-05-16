from tkinter import Tk, messagebox
import pgzrun
from pgzero.builtins import Actor
from game_gfever import Game, Stone

WIDTH = 400
HEIGHT = 400
TITLE = "Gold Fever"

btn_take = Actor("btn_take", (100, 350))
btn_end = Actor("btn_end", (300, 350))
can_take_stone = True
last_taken_stone = None
game = Game()


def msg_box(title, text):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, text)
    root.destroy()


def game_over():
    return 5 in [game.player().score, game.opponent().score]


def draw_player_score(player, coords):
    c = "red" if player == game.current_player else "black"
    pts = game.players[player].score
    screen.draw.circle(coords, 40, color=c)
    screen.draw.text(f"P {player + 1}\n{pts}", center=coords, color=c, align="center")


def draw_table_stones():
    for i, s in enumerate(game.table_stones):
        fname = f"stone_{s.name.lower()}_s"
        pos = (50 + i * 50, 150)
        Actor(fname, pos).draw()


def can_end_turn():
    return game.table_stones or not can_take_stone


def draw():
    screen.fill("white")
    draw_player_score(0, (50, 50))
    draw_player_score(1, (150, 50))
    draw_table_stones()

    if game_over():
        screen.draw.text("Game over!", (10, 100), color="black")
        return

    if can_take_stone:
        btn_take.draw()
    if can_end_turn():
        btn_end.draw()


def on_mouse_down(pos):
    global can_take_stone, last_taken_stone

    if game_over():
        return

    if can_take_stone and btn_take.collidepoint(pos):
        last_taken_stone, can_take_stone = game.draw_stone()

    if can_end_turn() and btn_end.collidepoint(pos):
        if can_take_stone:
            game.end_turn()  # ended voluntarily
        else:
            opp_stone = game.resolve(last_taken_stone)
            if last_taken_stone == Stone.BLACK and opp_stone:
                msg_box("Got a stone!", f"Got from opponent: {opp_stone.name}")
        can_take_stone = True


pgzrun.go()
