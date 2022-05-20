import random


class Game:
    def __init__(self):
        self.score = [0, 0]
        self.current_player = 0
        self.dice = [0] * 5
        self.turn = 0

    def _rand(self):
        return random.randint(1, 6)

    def hold_idx(self):
        pref = [6, 5, 4]
        hold_idx = 3
        while pref and self.dice[: len(pref)] != pref:
            hold_idx -= 1
            pref.pop()
        return hold_idx

    def _set_element(self, value, index):  # make sure die value is at the given index
        if value in self.dice:
            pos = self.dice.index(value)
            self.dice[index], self.dice[pos] = self.dice[pos], self.dice[index]

    def roll_dice(self, hold3, hold4):
        # make sure non-held dice are at the end of the list
        if hold4:
            hold3, hold4 = hold4, hold3
            self.dice[3], self.dice[4] = self.dice[4], self.dice[3]

        hold_idx = self.hold_idx() + int(hold3) + int(hold4)
        self.dice = [self.dice[i] if i < hold_idx else self._rand() for i in range(5)]
        self._set_element(6, 0)
        self._set_element(5, 1)
        self._set_element(4, 2)

    def end_turn(self):
        if self.hold_idx() == 3:
            self.score[self.current_player] += self.dice[3] + self.dice[4]
        self.current_player = not self.current_player
        self.turn += 1
        self.dice = [0] * 5

    def game_over(self):
        return self.score[0] >= 100 or self.score[1] >= 100 or self.turn > 19
