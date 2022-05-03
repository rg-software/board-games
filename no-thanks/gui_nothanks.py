import pgzrun
from pgzero.builtins import Actor, Rect
from game_nothanks import Game

WIDTH = 800
HEIGHT = 600

btn_pass = Actor("btn_pass", (100, 40))
btn_take = Actor("btn_take", (300, 40))
game = Game()


def draw_card(value, x, y, w, h):
    screen.draw.rect(Rect(x, y, w, h), color="black")
    screen.draw.textbox(str(value), (x, y, w, h), color="black")


def draw_hand(player, x, y, w, h, is_active):
    deck = player.deck
    color = "red" if is_active else "black"

    screen.draw.circle((x + w / 2, y + h / 2), w, color=color)
    screen.draw.textbox(str(player.tokens), (x, y, w, h), color=color)
    x += 2 * w
    for v in deck:
        screen.draw.rect(Rect(x, y, w, h), color=color)
        screen.draw.textbox(str(v), (x, y, w, h), color=color)
        x += w + 2


def draw():
    screen.fill("white")

    if not game.deck:  # game over
        screen.draw.text("Final scores:", pos=(50, 200), color="black")
        y = 250
        for i, player in enumerate(game.players):
            screen.draw.text(
                f"Player {i + 1}. Score: {player.score()}", pos=(50, y), color="black"
            )
            y += 50
        return

    btn_pass.draw()
    btn_take.draw()

    draw_card(game.deck[0], 50, 100, 80, 40)
    screen.draw.text(
        f"Deck: {len(game.deck) - 1}, tokens: {game.table_tokens}",
        pos=(150, 120),
        color="black",
    )

    draw_hand(game.players[0], 50, 200, 30, 20, game.current_player == 0)
    draw_hand(game.players[1], 50, 300, 30, 20, game.current_player == 1)


def on_mouse_down(pos):
    if btn_pass.collidepoint(pos) and game.deck and game.can_pass():
        game.move_pass()
    if btn_take.collidepoint(pos) and game.deck:
        game.move_take()


pgzrun.go()
