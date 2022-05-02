import pgzrun
from pgzero.builtins import Actor
from game_pokerdice import Game

WIDTH = 1000
HEIGHT = 750

game = Game()
btn_roll = Actor("btn_roll", (100, 50))
btn_end = Actor("btn_end", (300, 50))


def draw_hand(player, x, y):
    dice_values = ["9", "10", "j", "q", "k", "a"]

    for k, i in enumerate(player.hand):
        pref = "club" if k in player.to_roll else "diamond"
        a = Actor(f"{pref}_{dice_values[i]}", topleft=(x, y))
        a.draw()
        x += a.width


def draw_player_info(player_idx, y):
    player = game.players[player_idx]
    if player.rolls_left < 3:
        draw_hand(player, 0, y)
        if game.current_player_idx > player_idx:
            screen.draw.text(
                f"final hand: {player.hand_name()}", (600, y - 20), color="black"
            )


def draw():
    screen.fill("white")

    btn_roll.draw()
    btn_end.draw()

    if not game.is_game_over():
        screen.draw.text(
            f"current player: {game.current_player_idx + 1}, "
            f"rolls left: {game.current_player().rolls_left}",
            (500, 20),
            color="black",
        )

    draw_player_info(0, 100)
    draw_player_info(1, 400)

    if game.is_game_over():
        s = "Draw"
        if game.players[0].hand_better_than(game.players[1]):
            s = "Player 1 wins"
        elif game.players[1].hand_better_than(game.players[0]):
            s = "Player 2 wins"
        screen.draw.text(s, (10, 670), color="black")


def player_y():
    return 100 if game.current_player_idx == 0 else 400


def on_mouse_down(pos):
    if btn_end.collidepoint(pos) and game.current_player().rolls_left < 3:
        game.next_player()

    if game.is_game_over():
        return

    if game.current_player().can_roll() and btn_roll.collidepoint(pos):
        game.current_player().roll_dice()

    if game.current_player().rolls_left in range(1, 3):  # can freeze
        x, y = pos
        if y in range(player_y(), player_y() + 250):
            game.current_player().freeze(int(x / 200))


pgzrun.go()
