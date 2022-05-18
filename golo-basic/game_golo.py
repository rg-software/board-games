import random


class Game:
    def __init__(self):
        self.dice = [
            [1, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 8],
            [2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7],
            [3, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 10],
            [4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9],
        ] + [[3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8]] * 5

        self.score = 0
        self.rolled = []

    def roll(self):
        self.rolled = [random.choice(die) for die in self.dice]

    def can_remove(self, indices):  # must remove the smallest numbers
        to_remove = [self.rolled[i] for i in indices]
        to_remain = [self.rolled[i] for i in range(len(self.dice)) if i not in indices]
        return not to_remain or max(to_remove) <= min(to_remain)

    def remove(self, indices):
        self.score += sum([self.rolled[i] for i in indices])
        self.dice = [self.dice[i] for i in range(len(self.dice)) if i not in indices]
