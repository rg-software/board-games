import random

# TODO: randomly change placed dice!


class Game:
    def __init__(self):
        self.dice = [8, 8]  # for 2 players
        self.arena = [random.randint(2, 6)]
        self.current_player = 0
        self.last_roll = None

    def _genrand(self):
        return random.randint(1, 6)

    def _roll(self, count):
        self.dice[self.current_player] -= count
        self.last_roll = [self._genrand() for _ in range(count)]
        self.arena += self.last_roll
        self._remove_all(1)
        self.arena.sort()

    def _remove_all(self, value):
        self.arena = [x for x in self.arena if x != value]

    def _resolve(self):
        s = 0
        for v in range(2, 7):
            if (c := self.arena.count(v)) > 1:
                self.dice[self.current_player] += c
                s += c
                self._remove_all(v)
        return s

    def roll(self):
        self._roll(1 if self.arena else self.dice[self.current_player])

        if len(set(self.arena)) == len(self.arena):  # all unique
            return 0

        return self._resolve()

    def pass_turn(self):
        self.current_player = not self.current_player
        self.last_roll = None

    def game_over(self):
        return 0 in self.dice
