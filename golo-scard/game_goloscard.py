import random


class Game:
    def __init__(self, scorecard):
        self.scorecard = scorecard
        self.dice = [
            (3, [1, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 8]),
            (3, [2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7]),
            (5, [3, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 10]),
            (5, [4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9]),
        ] + [(4, [3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8])] * 5

        self.score = 0
        self.rolled = []

    def roll(self):
        self.rolled = [random.choice(die) for _, die in self.dice]

    def can_remove(self, all_indices):  # must remove matching par dice only
        to_remove = []
        indices = list(all_indices)
        while indices:
            hole = 9 - len(self.dice) + len(to_remove)
            par = self.scorecard[hole]
            k = [i for i in indices if self.dice[i][0] == par and not i in to_remove]
            if not k:
                return False
            to_remove.append(k[0])
            indices.remove(k[0])
        return True

    def remove(self, indices):
        self.score += sum([self.rolled[i] for i in indices])
        self.dice = [self.dice[i] for i in range(len(self.dice)) if i not in indices]
