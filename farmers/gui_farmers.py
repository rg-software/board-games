from tkinter import Tk, messagebox, simpledialog
import pgzrun
from pgzero.builtins import Actor
from game_farmers import Game, ActionError

WIDTH = 700
HEIGHT = 450
TITLE = "Farmers Finances"

btn_buy_wheat = Actor("btn_buy_wheat", (80, 350))
btn_buy_animal = Actor("btn_buy_animal", (80 + 130, 350))
btn_sell_wheat = Actor("btn_sell_wheat", (80 + 130 * 2, 350))
btn_sell_animal = Actor("btn_sell_animal", (80 + 130 * 3, 350))
btn_make_bread = Actor("btn_make_bread", (80 + 130 * 4, 350))
Tk().wm_withdraw()


# btn_end = Actor("btn_end", (300, 200))
game = Game()


def print_die(pts, pos, color):
    if pts:
        sym = "\U0001F404"  # cow # = chr(ord("\u2680") + pts - 1)
        screen.draw.text(sym, pos, color=color, fontname="notoemoji", fontsize=60)


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
    screen.draw.text(f"Player {n+1}. Money: {p.money}", pos=(x, y), color=c)
    draw_cards(p.wheat, p.animal, p.bread, (x, y + 50), c)


def reroll_market(force):
    if not force and messagebox.askyesno("", "Yes to change market, No to reroll"):
        if game.is_market_on_edge():
            game.move_from_edge()
        else:
            isbuy = messagebox.askyesno("", "Yes for better buy, No for better sell")
            game.change_market(-1 if isbuy else 1)
    elif game.reroll_market():
        v = simpledialog.askinteger("", "Free choice! set buy market value (-2..2)")
        game.set_market(int(v + 2))


def draw():
    screen.fill("white")

    if game.game_over():
        messagebox.showinfo(
            "", f"Game over! P1: {game.players[0].money}, P2: {game.players[1].money}"
        )

    draw_market_info()
    draw_player_info(0, game.players[0], game.current_player_idx == 0, 20, 50)
    draw_player_info(1, game.players[1], game.current_player_idx == 1, 20, 200)

    btn_buy_wheat.draw()
    btn_buy_animal.draw()
    btn_sell_wheat.draw()
    btn_sell_animal.draw()
    btn_make_bread.draw()

    # screen.draw.text(f"table: {pig.table}", (220, 20), color="black")

    # print_die(5, (220, 40), "black")


#     if pig.game_over():
#         screen.draw.text("Game over!", (10, 100), color="black")
#     else:
#         btn_roll.draw()
#         btn_end.draw()


def ask_amount():
    return simpledialog.askinteger("", "How many?")


def on_mouse_down(pos):

    try:
        move_completed = True

        if btn_make_bread.collidepoint(pos):
            game.make_bread(ask_amount())
        elif btn_buy_wheat.collidepoint(pos):
            game.buy_wheat()
        elif btn_buy_animal.collidepoint(pos):
            game.buy_animal()
        elif btn_sell_wheat.collidepoint(pos):
            game.sell_wheat(ask_amount())
        elif btn_sell_animal.collidepoint(pos):
            game.sell_animal(ask_amount())
        else:
            move_completed = False

        if move_completed:
            if game.is_empty_market():
                messagebox.showinfo("", "Market is empty! Will sell goods.")
                game.sell_all()
                reroll_market(True)
            else:
                reroll_market(False)
            game.pass_turn()

    except ActionError:
        pass


pgzrun.go()
