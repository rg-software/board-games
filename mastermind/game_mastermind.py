import random


class Game:
    def __init__(self):
        self.code = self._gencode()

    # playing the base game: all pegs are distinct, no empty spaces
    def _gencode(self):
        r = list(range(6))  # 6 colors
        random.shuffle(r)
        return r[:4]

    def is_correct(self, s):
        return self.black_pegs(s) == 4

    def white_pegs(self, s):  # correct value but not position
        return sum([1 for i in range(4) if s[i] in self.code and s[i] != self.code[i]])

    def black_pegs(self, s):  # correct value and position
        return sum([1 for i in range(4) if s[i] == self.code[i]])
