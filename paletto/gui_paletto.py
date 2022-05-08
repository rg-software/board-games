import pgzrun
from pgzero.builtins import Actor
from game_paletto import Game

WIDTH = 700
HEIGHT = 500
TITLE = "Paletto"

game = Game()
end_button = Actor("end", (400, 400))
gameover_box = Actor("gameover", center=(WIDTH / 2, HEIGHT / 2))
color_names = ["white", "blue", "cyan", "gray", "green", "red", "gold"]


def print_player_info(player_no, pos, is_active):
    c = "red" if is_active else "black"
    screen.draw.text(f"Player {player_no}", midleft=pos, color=c)

    if is_active:
        cc = color_names[game.current_color]
        screen.draw.filled_circle((pos[0] + 100, pos[1]), 20, color=cc)

    dx = 0
    for c_idx, c in enumerate(color_names[1:]):
        screen.draw.filled_circle((pos[0] + dx, pos[1] + 50), 20, color=c)
        is_first = player_no == 1
        card = game.scorecards[is_first]
        score = card[c_idx + 1]
        screen.draw.text(str(score), center=(pos[0] + dx, pos[1] + 50))
        dx += 50


def draw():
    screen.fill("white")
    end_button.draw()

    print_player_info(1, (400, 50), game.p1_turn)
    print_player_info(2, (400, 250), not game.p1_turn)

    for r in range(1, 7):
        for c in range(1, 7):
            color = game.board.data[r][c]
            cname = color_names[color]
            screen.draw.filled_circle((c * 50, r * 50), 20, color=cname)

    if game.game_over():
        gameover_box.draw()
        screen.draw.text(
            f"Winner: Player {2 - game.p1_turn}",
            center=(WIDTH / 2, 3 * HEIGHT / 4),
            color="black",
        )


def on_mouse_down(pos):
    r = (pos[1] + 25) // 50
    c = (pos[0] + 25) // 50

    if r in range(1, 7) and c in range(1, 7) and game.can_remove_at(r, c):
        game.remove_at(r, c)

    if end_button.collidepoint(pos) and game.current_color:
        game.end_turn()


pgzrun.go()
