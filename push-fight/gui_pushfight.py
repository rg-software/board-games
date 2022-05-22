import pgzrun
from game_pushfight import Game, Cell, GameState
from pygame import Rect

CELLSIZE = 70
MARGIN = 5

WIDTH = Game.BoardWidth * CELLSIZE + CELLSIZE*2
HEIGHT = Game.BoardHeight * CELLSIZE + CELLSIZE*3
TITLE = "Push-Fight"

game = Game()

def draw_skip(r, c, color):
    screen.draw.filled_rect(
        Rect(
            c * CELLSIZE + MARGIN + CELLSIZE,
            r * CELLSIZE + MARGIN + CELLSIZE*2,
            CELLSIZE - MARGIN*2,
            CELLSIZE - MARGIN*5,
        ),
        color,
    )

def draw_cell(r, c, color):
    screen.draw.filled_rect(
        Rect(
            c * CELLSIZE + MARGIN + CELLSIZE,
            r * CELLSIZE + MARGIN + CELLSIZE*2,
            CELLSIZE - MARGIN,
            CELLSIZE - MARGIN,
        ),
        color,
    )
def draw_square(r, c, color_b, color_t, color_a):
    screen.draw.filled_rect(
        Rect(
            c * CELLSIZE + MARGIN*(1.5) + CELLSIZE,
            r * CELLSIZE + MARGIN*(1.5) + CELLSIZE*2,
            CELLSIZE - MARGIN*2,
            CELLSIZE - MARGIN*2,
        ),
        color_a,
    )
    screen.draw.filled_rect(
        Rect(
            c * CELLSIZE + MARGIN*2 + CELLSIZE,
            r * CELLSIZE + MARGIN*2 + CELLSIZE*2,
            CELLSIZE - MARGIN*3,
            CELLSIZE - MARGIN*3,
        ),
        color_b,
    )
    screen.draw.filled_rect(
        Rect(
            c * CELLSIZE + MARGIN*3 + CELLSIZE,
            r * CELLSIZE + MARGIN*3 + CELLSIZE*2,
            CELLSIZE - MARGIN*5,
            CELLSIZE - MARGIN*5,
        ),
        color_t,
    )
def draw_round(r, c, color_b, color_t, color_a):
    screen.draw.filled_rect(
        Rect(
            c * CELLSIZE + MARGIN*(1.5) + CELLSIZE,
            r * CELLSIZE + MARGIN*(1.5) + CELLSIZE*2,
            CELLSIZE - MARGIN*2,
            CELLSIZE - MARGIN*2,
        ),
        color_a,
    )
    screen.draw.filled_rect(
        Rect(
            c * CELLSIZE + MARGIN*2 + CELLSIZE,
            r * CELLSIZE + MARGIN*2 + CELLSIZE*2,
            CELLSIZE - MARGIN*3,
            CELLSIZE - MARGIN*3,
        ),
        color_b,
    )
    screen.draw.filled_circle((
        c * CELLSIZE + MARGIN/2 + CELLSIZE + CELLSIZE/2, 
        r * CELLSIZE + MARGIN/2 + CELLSIZE*2 + CELLSIZE/2
        ), 
        CELLSIZE/3, color_t
        )

def draw_anchor(r, c):
    screen.draw.filled_circle((
        c * CELLSIZE + MARGIN/2 + CELLSIZE + CELLSIZE/2, 
        r * CELLSIZE + MARGIN/2 + CELLSIZE*2 + CELLSIZE/2
        ), 
        CELLSIZE/3, "red"
        )

def what_to_draw(cell, r, c):
    if cell != Cell.LAVA and r >= 0:
        color = "gray"
        if game._state_is() == GameState.START and c > 4: color = "light blue"
        if game._state_is() == GameState.START and c < 5: color = "light salmon"
        if game._selected_is() == (r, c):  color = "light green"
        draw_cell(r, c, color)
    if cell == Cell.LAVA:
        draw_cell(r, c, "orange")
    if cell == Cell.BROWN_ANCHOR:
        draw_square(r, c, "dark red", "tan", "grey 42")
        draw_anchor(r, c)
    if cell == Cell.BROWN_ROUND:                
        draw_round(r, c, "dark red", "tan", "grey 42")
    if cell == Cell.BROWN_SQUARE:                
        draw_square(r, c, "dark red", "tan", "grey 42") 
    if cell == Cell.WHITE_ANCHOR:                
        draw_square(r, c, "gray 85", "white", "gray 42")
        draw_anchor(r, c)
    if cell == Cell.WHITE_ROUND:                
        draw_round(r, c, "gray 85", "white", "gray 42")
    if cell == Cell.WHITE_SQUARE:                
        draw_square(r, c, "gray 85", "white", "gray 42")

def draw():
    screen.fill("grey 23")

    for i in range(1, 12):
        screen.draw.line((CELLSIZE * i, CELLSIZE*2), (CELLSIZE * i, Game.BoardHeight * CELLSIZE + CELLSIZE*2), "light gray")

    for i in range(1, 6):
        screen.draw.line((CELLSIZE, CELLSIZE * i + CELLSIZE), (Game.BoardWidth * CELLSIZE + CELLSIZE, CELLSIZE * i + CELLSIZE), "light gray")

    for r in range(4):
        for c in range(10):
            what_to_draw(game.board[r][c], r, c)
            
    if game._state_is() == GameState.START:
        what_to_draw(Game.in_box[0], -1, 5)
        screen.draw.text(
            f"position the piece:",
            centery=CELLSIZE + MARGIN*4,
            left=CELLSIZE*3 + MARGIN*2,
            fontsize=32,
            color="grey 89",
        )
    if game._state_is() == GameState.MOVE:
        draw_skip(-1, 5, "grey 54")
        screen.draw.text(
            f"skip",
            centery=CELLSIZE + MARGIN*5,
            left=CELLSIZE*6 + MARGIN*3,
            fontsize=24,
            color="black",
        )
        screen.draw.text(
            f"{game.player_name()}\nmoves: {game.hint_text()}",
            centery=CELLSIZE + MARGIN*4,
            left=CELLSIZE*3 + MARGIN*2,
            fontsize=32,
            color="grey 89",
        )
    if game._state_is() == GameState.PUSH:
        screen.draw.text(
            f"{game.player_name()}\npush!",
            centery=CELLSIZE + MARGIN*4,
            left=CELLSIZE*3 + MARGIN*2,
            fontsize=32,
            color="grey 89",
        )
    if game.is_game_over():
        screen.draw.text(
            f"Game over! {game.player_name()} player lost",
            centery=CELLSIZE + MARGIN*4,
            left=CELLSIZE*3 + MARGIN*2,
            fontsize=32,
            color="red",
        )

def on_mouse_down(pos):
    r = pos[1] // CELLSIZE - 2
    c = pos[0] // CELLSIZE - 1
    
    if game._state_is() == GameState.START:
        game.starting_position(r, c)
    if game._state_is() == GameState.MOVE:
        if r == -1 and c == 5: 
            game.move_done()
        elif game.can_move_at(r, c): 
            game.move_at(r, c)            
        else: game.select_piece(r, c)
    if game._state_is() == GameState.PUSH:
        if game.can_push_at(r, c): 
            game.push_at(r, c)
        else: game.select_piece(r, c)

pgzrun.go()