from tkinter import Tk, messagebox
import pgzrun
from pgzero.builtins import Actor
from game_impact import Game

WIDTH = 600
HEIGHT = 300

btn_roll = Actor("btn_roll", (100, 200))
btn_end = Actor("btn_end", (300, 200))
game = Game()
Tk().wm_withdraw()


def draw_player_score(player, coords):
    c = "red" if player == game.current_player else "black"
    screen.draw.text(f"player {player + 1}: {game.dice[player]}", coords, color=c)


def draw():
    screen.fill("white")
    draw_player_score(0, (10, 0))
    draw_player_score(1, (10, 20))
    screen.draw.text(f"arena: {game.arena}", (10, 40), color="black")
    screen.draw.text(f"last roll: {game.last_roll}", (10, 60), color="black")

    if game.game_over():
        screen.draw.text(f"Game over! Final dice: {game.dice}", (10, 80), color="black")
    else:
        btn_roll.draw()
        btn_end.draw()


def on_mouse_down(pos):
    if not game.game_over() and btn_roll.collidepoint(pos):
        if r := game.roll():
            messagebox.showinfo("Info", f"Obtained dice: {r}, passing turn.")
            game.pass_turn()

    if not game.game_over() and game.last_roll and btn_end.collidepoint(pos):
        game.pass_turn()


pgzrun.go()
