from tkinter import Tk, messagebox
import pgzrun
from pgzero.builtins import Actor, Rect
from game_othello import Game

CELLWIDTH = 100
WIDTH = 8 * CELLWIDTH + 200
HEIGHT = 8 * CELLWIDTH
TITLE = "Othello"

game = Game()


def draw_piece(r, c, name):
    piece = Actor(name, pos=(c * CELLWIDTH + 50, r * CELLWIDTH + 50))
    piece.draw()


def draw_infostring(s, ycoord):
    screen.draw.text(s, (HEIGHT + 10, ycoord), color="black")


def draw():
    screen.clear()
    screen.draw.filled_rect(Rect((HEIGHT, 0), (WIDTH, HEIGHT)), "yellow")

    Actor("board").draw()

    for r in range(8):
        for c in range(8):
            if game.board[r][c] is True:
                draw_piece(r, c, "white-piece.png")
            elif game.board[r][c] is False:
                draw_piece(r, c, "black-piece.png")

    draw_infostring(f"White = {game.count_pieces(True)}", 50)
    draw_infostring(f"Black = {game.count_pieces(False)}", 150)
    draw_infostring(f"Current move: {game.player_name()}", 250)


def msg_box(title, text):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, text)
    root.destroy()


def on_mouse_down(pos):
    r, c = pos[1] // 100, pos[0] // 100

    if r < 8 and c < 8 and game.move_allowed(r, c):
        game.move(r, c)

        if not game.has_legal_moves():
            game.pass_move()

            if game.has_legal_moves():
                msg_box("Info", "Cannot move. Passing turn to the opponent")
            else:
                msg_box("Info", "Game over!")


pgzrun.go()
