import random


class ActionError(BaseException):
    pass


def assert_product(product, count):
    if product < count:
        raise ActionError()


def assert_money(money, price):
    if money + price < 0:
        raise ActionError()


class Player:
    def __init__(self):
        self.money = 10
        self.wheat = 0
        self.animal = 0
        self.bread = 0

    def make_bread(self, n):
        self.wheat -= n
        self.bread += n

    def _buy(self, price, bonus):
        assert_money(self.money, price + bonus)
        self.money += price + bonus

    def _sell(self, units, price, bonus):
        self.money += (price + bonus) * units

    def buy_wheat(self, bonus):
        self._buy(-2, bonus)
        self.wheat += 1

    def buy_animal(self, bonus):
        self._buy(-6, bonus)
        self.animal += 1

    def sell_wheat(self, n, bonus):
        assert_product(self.wheat, n)
        self._sell(n, 5, bonus)
        self.wheat -= n

    def sell_animal(self, n, bonus):
        assert_product(self.animal, n)
        self._sell(n, 10, bonus)
        self.animal -= n

    def sell_bread(self, n):
        assert_product(self.bread, n)
        self._sell(n, 7, 0)
        self.bread -= n


class Game:
    def __init__(self):
        self._market_idx = random.randint(0, 4)
        self._buy_market = [2, 1, 0, -1, -2]
        self.players = [Player(), Player()]
        self.current_player_idx = 0
        self.table_wheat = 4
        self.table_animals = 2

    def buy_bonus(self):
        return self._buy_market[self._market_idx]

    def sell_bonus(self):
        return -1 * self.buy_bonus()

    def current_player(self):
        return self.players[self.current_player_idx]

    def make_bread(self, n):
        self.current_player().make_bread(n)

    def buy_wheat(self):
        assert_product(self.table_wheat, 1)
        self.current_player().buy_wheat(self.buy_bonus())
        self.table_wheat -= 1

    def buy_animal(self):
        assert_product(self.table_animals, 1)
        self.current_player().buy_animal(self.buy_bonus())
        self.table_animals -= 1

    def sell_wheat(self, n):
        self.current_player().sell_wheat(n, self.sell_bonus())
        self.table_wheat += n

    def sell_bread(self, n):
        self.current_player().sell_bread(n)
        self.table_wheat += n

    def sell_animal(self, n):
        self.current_player().sell_animal(n, self.sell_bonus())
        self.table_animals += n

    # def _genrand(self):
    #     return random.randint(1, 6)

    def is_empty_market(self):
        return self.table_animals == 0 and self.table_wheat == 0

    def _sell_cards(self):
        self.sell_wheat(self.current_player().wheat)
        self.sell_bread(self.current_player().bread)
        self.sell_animal(self.current_player().animal)

    def sell_all(self):
        for _ in range(2):
            self._sell_cards()
            self.pass_turn()

    def is_market_on_edge(self):
        return self._market_idx in [0, 4]

    def move_from_edge(self):
        self._market_idx = 1 if self._market_idx == 0 else 3

    def change_market(self, d):
        self._market_idx += d

    def reroll_market(self):
        if (v := random.randint(1, 6)) < 6:
            self._market_idx = v
        return v == 6

    def set_market(self, v):
        self._market_idx = v

    def pass_turn(self):
        self.current_player_idx = not self.current_player_idx

    def game_over(self):  # need to check after the second player turn
        return self.current_player_idx == 0 and (
            self.players[0].money > 70 or self.players[1].money > 70
        )
