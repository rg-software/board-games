from math import hypot
import pgzrun
from pgzero.builtins import Actor, Rect
from game_kalah import Game

WIDTH = 800
HEIGHT = 300

kalah = Game()


def pit_coords(pit_no):
    board_h = 288
    board_w = 800

    if pit_no == 0:
        return (board_w / 9, board_h / 2)
    elif pit_no == 7:
        return (8 * board_w / 9, board_h / 2)
    elif pit_no < 7:
        return (175 + 90 * (pit_no - 1), 2 * board_h / 3)
    else:
        return (175 + 90 * (14 - pit_no - 1), board_h / 3)


def draw():
    screen.clear()
    gameboard = Actor("gameboard")
    gameboard.draw()

    plbar_y = 0 if kalah.upper_player_move else gameboard.height - 10
    screen.draw.filled_rect(Rect((0, plbar_y), (800, plbar_y + 10)), "green")

    for pit_no in range(14):
        screen.draw.text(
            f"{kalah.board[pit_no]}", center=pit_coords(pit_no), color="black"
        )


def pit_at_location(mx, my):
    for pit_no in range(14):
        is_storage = pit_no in [kalah.my_storage(), kalah.opp_storage()]
        x, y = pit_coords(pit_no)
        if hypot(mx - x, my - y) < 40 and not is_storage:
            return pit_no
    return -1


def on_mouse_down(pos):
    house_no = pit_at_location(pos[0], pos[1])

    if house_no in kalah.my_houses() and kalah.board[house_no] > 0:
        kalah.make_move(house_no)
        if kalah.is_end_game():
            kalah.capture_remaining()


pgzrun.go()
