import pgzrun
from game_stopgate import Game, Cell
from pygame import Rect

CELLSIZE = 50
MARGIN = 10

WIDTH = Game.BoardWidth * CELLSIZE
HEIGHT = Game.BoardHeight * CELLSIZE

game = Game()


def draw_horiz(r, c):
    screen.draw.filled_rect(
        Rect(
            c * CELLSIZE + MARGIN,
            r * CELLSIZE + MARGIN,
            2 * CELLSIZE - 2 * MARGIN,
            CELLSIZE - 2 * MARGIN,
        ),
        "black",
    )


def draw_vert(r, c):
    screen.draw.filled_rect(
        Rect(
            c * CELLSIZE + MARGIN,
            r * CELLSIZE + MARGIN,
            CELLSIZE - 2 * MARGIN,
            2 * CELLSIZE - 2 * MARGIN,
        ),
        "black",
    )


def draw():
    screen.fill("white")

    for i in range(1, 8):
        screen.draw.line((CELLSIZE * i, 0), (CELLSIZE * i, HEIGHT), "black")

    for i in range(1, 8):
        screen.draw.line((0, CELLSIZE * i), (WIDTH, CELLSIZE * i), "black")

    for r in range(8):
        for c in range(8):
            if game.board[r][c] == Cell.HORIZ:
                draw_horiz(r, c)
            elif game.board[r][c] == Cell.VERT:
                draw_vert(r, c)

    if game.is_game_over():
        screen.draw.text(
            f"Game over! {game.player_name()} player lost",
            centery=int(HEIGHT / 2) - 20,
            centerx=int(WIDTH / 2),
            fontsize=32,
            color="red",
        )


def on_mouse_down(pos):
    r = int(pos[1] / CELLSIZE)
    c = int(pos[0] / CELLSIZE)

    if game.can_place_at(r, c):
        game.place_at(r, c)
        game.next_player()


pgzrun.go()
