from game_farmers import Game

game = Game()


def print_player_info(n, p, is_current):
    print(f'{">" if is_current else " "}P{n}. ', end="")
    print(f"money: {p.money}, wheat: {p.wheat}, animal: {p.animal}, bread: {p.bread}")


def print_table_info():
    print(f"buy bonus: {game.buy_bonus()}, sell bonus: {game.sell_bonus()}")
    print(f"[market] wheat: {game.table_wheat}, animals: {game.table_animals}")


def reroll_market(force):
    if not force and input("(c)hange or (r)eroll market? ") == "c":
        if game.is_market_on_edge():
            game.move_from_edge()
        else:
            d = -1 if input("good (b)uy or good (s)ell? ") == "b" else 1
            game.change_market(d)
    elif game.reroll_market():
        v = input("Free choice! Set buy market value (-2..2): ")
        game.set_market(int(v + 2))


while not game.game_over():
    print()
    print_table_info()
    print_player_info(1, game.players[0], game.current_player_idx == 0)
    print_player_info(2, game.players[1], game.current_player_idx == 1)

    if (action := input("(b)uy, (s)ell, or (m)ake bread? ")) != "m":
        product = input("(w)heat or (a)nimal? ")
    if action == "m" or action == "s":
        amount = int(input("how many items? "))

    if action == "m":
        game.make_bread(amount)
    elif action == "b" and product == "w":
        game.buy_wheat()
    elif action == "b" and product == "a":
        game.buy_animal()
    elif action == "s" and product == "w":
        game.sell_wheat(amount)
    elif action == "s" and product == "a":
        game.sell_animal(amount)
    else:
        print("Illegal action!")
        continue

    if game.is_empty_market():
        print("Market is empty! Will sell goods.")
        game.sell_all()
        reroll_market(True)
    else:
        reroll_market(False)

    game.pass_turn()

if game.players[0].money != game.players[1].money:
    print("Game over! Final score:")
    print("P1: {game.players[0].money}, P2: {game.players[1].money}")
else:
    print("Tie! Will sell all the goods")
    game.set_market(2)  # middle
    game.sell_all()
    print("Final Score. P1: {game.players[0].money}, P2: {game.players[1].money}")
