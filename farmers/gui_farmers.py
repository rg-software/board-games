from tkinter import Tk, messagebox, simpledialog
import pgzrun
from pgzero.builtins import Actor
from game_farmers import Game, ActionError

WIDTH = 700
HEIGHT = 450
TITLE = "Farmers Finances"

btn_buy_wheat = Actor("btn_buy_wheat", (80, 350))
btn_buy_animals = Actor("btn_buy_animal", (80 + 130, 350))
btn_sell_wheat = Actor("btn_sell_wheat", (80 + 130 * 2, 350))
btn_sell_animals = Actor("btn_sell_animal", (80 + 130 * 3, 350))
btn_make_bread = Actor("btn_make_bread", (80 + 130 * 4, 350))

game = Game()


def msg_box(title, text):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, text)
    root.destroy()


def ask_amount(text):
    root = Tk()
    root.withdraw()
    r = simpledialog.askinteger("", text)
    root.destroy()
    return r


def ask_yesno(text):
    root = Tk()
    root.withdraw()
    r = messagebox.askyesno("", text)
    root.destroy()
    return r


def draw_cards(wheat, animal, bread, pos, c):
    cards = ["\U0001F404"] * animal
    cards += ["\U0001F33E"] * wheat
    cards += ["\U0001F35E"] * bread
    screen.draw.text("".join(cards), pos, fontname="notoemoji", color=c, fontsize=40)


def draw_market_info():
    screen.draw.text(
        f"Market. Buy bonus: {game.buy_bonus()}, sell bonus: {game.sell_bonus()}",
        (350, 50),
        color="black",
    )
    draw_cards(game.table_wheat, game.table_animals, 0, (350, 80), "black")


def draw_player_info(n, p, is_current, x, y):
    c = "red" if is_current else "black"
    screen.draw.text(f"Player {n + 1}. Money: {p.money}", pos=(x, y), color=c)
    draw_cards(p.wheat, p.animals, p.bread, (x, y + 50), c)


def reroll_market(force):
    if not force and ask_yesno("Yes to change market, No to reroll"):
        if game.is_market_on_edge():
            game.move_from_edge()
        else:
            game.change_market(ask_yesno("Yes for better buy, No for better sell"))
    elif game.reroll_market():
        game.set_market(ask_amount("Free choice! set buy market value (-2..2)"))


def message_game_over():
    players = game.players
    if players[0].money != players[1].money:
        msg_box("", f"Game over! P1: {players[0].money}, P2: {players[1].money}")
    else:
        msg_box("", "Tie! Will sell all the goods.")
        game.set_market(0)
        game.sell_all()
        msg_box("", f"Final Score. P1: {players[0].money}, P2: {players[1].money}")


def draw():
    screen.fill("white")

    if game.game_over():
        message_game_over()

    draw_market_info()
    draw_player_info(0, game.players[0], game.current_player_idx == 0, 20, 50)
    draw_player_info(1, game.players[1], game.current_player_idx == 1, 20, 200)

    btn_buy_wheat.draw()
    btn_buy_animals.draw()
    btn_sell_wheat.draw()
    btn_sell_animals.draw()
    btn_make_bread.draw()


def on_mouse_down(pos):

    try:
        move_completed = True

        if btn_make_bread.collidepoint(pos):
            game.make_bread(ask_amount("How many?"))
        elif btn_buy_wheat.collidepoint(pos):
            game.buy_wheat()
        elif btn_buy_animals.collidepoint(pos):
            game.buy_animals()
        elif btn_sell_wheat.collidepoint(pos):
            game.sell_wheat(ask_amount("How many?"))
        elif btn_sell_animals.collidepoint(pos):
            game.sell_animals(ask_amount("How many?"))
        else:
            move_completed = False

        if move_completed:
            if game.is_empty_market():
                msg_box("", "Market is empty! Will sell all the goods.")
                game.sell_all()
                reroll_market(True)
            else:
                reroll_market(False)
            game.pass_turn()

    except ActionError:
        msg_box("", "Illegal action!")


pgzrun.go()
