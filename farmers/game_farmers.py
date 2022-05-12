import random


class ActionError(BaseException):
    pass


def ensure(condition):
    if not condition:
        raise ActionError()


class Player:
    def __init__(self):
        self.money = 10
        self.wheat = 0
        self.animals = 0
        self.bread = 0

    def make_bread(self, n):
        ensure(self.wheat >= n)
        self.wheat -= n
        self.bread += n

    def _buy(self, price, bonus):
        r_price = min(price + bonus, -1)  # at least one coin
        ensure(self.money + r_price >= 0)
        self.money += r_price

    def _sell(self, have_units, units, price, bonus):
        ensure(have_units >= units)
        self.money += (price + bonus) * units

    def buy_wheat(self, bonus):
        self._buy(-2, bonus)
        self.wheat += 1

    def buy_animals(self, bonus):
        self._buy(-6, bonus)
        self.animals += 1

    def sell_wheat(self, n, bonus):
        self._sell(self.wheat, n, 5, bonus)
        self.wheat -= n

    def sell_animals(self, n, bonus):
        self._sell(self.animals, n, 10, bonus)
        self.animals -= n

    def sell_bread(self, n):
        self._sell(self.bread, n, 7, 0)
        self.bread -= n


class Game:
    def __init__(self):
        self._buy_bonus = random.randint(-2, 2)
        self.players = [Player(), Player()]
        self.current_player_idx = 0
        self.table_wheat = 4
        self.table_animals = 2

    def buy_bonus(self):
        return self._buy_bonus  # _buy_market[self._market_idx]

    def sell_bonus(self):
        return -1 * self.buy_bonus()

    def current_player(self):
        return self.players[self.current_player_idx]

    def make_bread(self, n):
        self.current_player().make_bread(n)

    def buy_wheat(self):
        ensure(self.table_wheat >= 1)
        self.current_player().buy_wheat(self.buy_bonus())
        self.table_wheat -= 1

    def buy_animals(self):
        ensure(self.table_animals >= 1)
        self.current_player().buy_animals(self.buy_bonus())
        self.table_animals -= 1

    def sell_wheat(self, n):
        self.current_player().sell_wheat(n, self.sell_bonus())
        self.table_wheat += n

    def sell_bread(self, n):
        self.current_player().sell_bread(n)
        self.table_wheat += n

    def sell_animals(self, n):
        self.current_player().sell_animals(n, self.sell_bonus())
        self.table_animals += n

    def is_empty_market(self):
        return self.table_animals == 0 and self.table_wheat == 0

    def _sell_cards(self):
        self.sell_wheat(self.current_player().wheat)
        self.sell_bread(self.current_player().bread)
        self.sell_animals(self.current_player().animals)

    def sell_all(self):
        for _ in range(2):
            self._sell_cards()
            self.pass_turn()

    def move_from_edge(self):
        self._buy_bonus = min(1, max(-1, self._buy_bonus))

    def is_market_on_edge(self):
        return self._buy_bonus in [-2, 2]

    def change_market(self, good_buy):
        self._buy_bonus += 1 if good_buy else -1

    def reroll_market(self):
        if (v := random.randint(-2, 3)) < 3:
            self._buy_bonus = v
        return v == 3

    def set_market(self, v):
        self._buy_bonus = v

    def pass_turn(self):
        self.current_player_idx = not self.current_player_idx

    def game_over(self):  # need to check after the second player turn
        scored70 = min(self.players[0].money, self.players[1].money) >= 70
        return self.current_player_idx == 0 and scored70
