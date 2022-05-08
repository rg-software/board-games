from random import randint, random


class Game:
    KICK_CHANCE = 0.3  # we can kick dice in the arena

    def __init__(self):
        self.dice = [8, 8]  # for 2 players
        self.arena = [randint(2, 6)]
        self.current_player = 0

    def _genrand(self):
        return randint(1, 6)

    def _kick_dice(self, dice):
        return [self._genrand() if random() < Game.KICK_CHANCE else d for d in dice]

    def _roll(self, count):
        self.dice[self.current_player] -= count
        self.arena += [self._genrand() for _ in range(count)]
        self.arena = self._kick_dice(self.arena)
        self.arena.sort()

    def _remove_all(self, value):
        self.arena = [x for x in self.arena if x != value]

    def resolve(self):
        self._remove_all(1)
        s = 0
        for v in range(2, 7):
            if (c := self.arena.count(v)) > 1:
                self.dice[self.current_player] += c
                s += c
                self._remove_all(v)
        return s

    def roll(self):
        self._roll(1 if self.arena else self.dice[self.current_player])

    def pass_turn(self):
        self.current_player = not self.current_player

    def game_over(self):
        return 0 in self.dice
