import pgzrun
from game_blokusduo import Game, Cell
from pygame import Rect

CELLSIZE = 50
MARGIN = 10
ROW = 14
COLUMN = 14
WIDTH = Game.BoardWidth * CELLSIZE + CELLSIZE*7
HEIGHT = Game.BoardHeight * CELLSIZE 
TITLE = "Blokus DUO"

btn_previous = Actor("btn_previous", (CELLSIZE *ROW + CELLSIZE + CELLSIZE/2, CELLSIZE*10))
btn_rotate = Actor("btn_rotate", (CELLSIZE *ROW + CELLSIZE + CELLSIZE/2 + 70, CELLSIZE*10))
btn_flip = Actor("btn_flip", (CELLSIZE *ROW + CELLSIZE + CELLSIZE/2 + 70 * 2, CELLSIZE*10))
btn_next = Actor("btn_next", (CELLSIZE *ROW + CELLSIZE + CELLSIZE/2 + 70 * 3, CELLSIZE*10))

game = Game()

def draw_blocks_on_bord(r, c, color):
    screen.draw.filled_rect(
        Rect(
            c * CELLSIZE + MARGIN,
            r * CELLSIZE + MARGIN,
            CELLSIZE - 2 * MARGIN,
            CELLSIZE - 2 * MARGIN,
        ),
        color,
    )
def draw_hints():
    coord = game.hints()
    for r in range(0, ROW):
        for c in range(0, ROW):
            if (r,c) in coord:
                screen.draw.circle((c*CELLSIZE + CELLSIZE/2, r*CELLSIZE +CELLSIZE/2), MARGIN*2, "light gray")

def draw_current_block():    
    x = CELLSIZE *ROW + CELLSIZE
    y = CELLSIZE*4
    color = "white" if game.player_name() == "PLAYER_1" else "black"
    for i in range(0, 6):
        screen.draw.line((CELLSIZE*i + x, y), (CELLSIZE*i + x, y + CELLSIZE*5), "dark gray")
        screen.draw.line((x, CELLSIZE*i + y), (x + CELLSIZE*5, CELLSIZE * i + y), "dark gray")
    shape = game.current_block_shape()
    for r in range(0, 5):
        for c in range(0, 5):
            if (r,c) in shape:
                screen.draw.filled_rect(
                    Rect(
                        c * CELLSIZE + MARGIN + x,
                        r * CELLSIZE + MARGIN + y,
                        CELLSIZE - 2 * MARGIN,
                        CELLSIZE - 2 * MARGIN,
                    ),
                    color,
                )    
    screen.draw.circle((x + CELLSIZE/2, y + CELLSIZE/2), MARGIN*2, "white")

def draw():
    screen.fill("gray")
    for i in range(1, ROW + 1):
        screen.draw.line((CELLSIZE * i, 0), (CELLSIZE * i, HEIGHT), "white")
    for i in range(1, COLUMN + 1):
        screen.draw.line((0, CELLSIZE * i), (CELLSIZE *COLUMN, CELLSIZE * i), "white")

    for r in range(ROW):
        for c in range(COLUMN):
            if game.board[r][c] == Cell.BLOCK_1:
                draw_blocks_on_bord(r, c, "white")
            elif game.board[r][c] == Cell.BLOCK_2:
                draw_blocks_on_bord(r, c, "black")

    draw_current_block()
    draw_hints()

    btn_previous.draw()
    btn_rotate.draw()
    btn_flip.draw()
    btn_next.draw()
   
    if game.is_game_over():
        screen.draw.text(
            f"Game over!\n{game.player_name()} lost",
            centery=CELLSIZE*3,
            centerx=CELLSIZE*ROW + CELLSIZE*3,
            fontsize=32,
            color="red",
        )
    else:
        screen.draw.text(
            f"{game.player_name()}",
            centery=CELLSIZE*3,
            centerx=CELLSIZE*ROW + CELLSIZE*3,
            fontsize=32,
            color="black",
        )

def on_mouse_down(pos):
    r = pos[1] // CELLSIZE
    c = pos[0] // CELLSIZE
    if game.can_place_at(r, c, 0):
        game.place_at(r, c)
        game.next_player()

    if btn_rotate.collidepoint(pos):
        game.rotate_current_block()
    if btn_flip.collidepoint(pos):
        game.flip_current_block()
    if btn_next.collidepoint(pos):
        game.next_block(1)
    if btn_previous.collidepoint(pos):
        game.next_block(-1)

pgzrun.go()