import random


class Game:
    def __init__(self):
        self.card = [[0 for _ in range(5)] for _ in range(6)]
        self.cardp = [[0 for _ in range(5)] for _ in range(6)]

        points = [
            (0, 0, 3),
            (2, 0, 2),
            (3, 0, 2),
            (5, 0, 3),
            (1, 1, 1),
            (4, 1, 1),
            (0, 2, 2),
            (2, 2, 1),
            (3, 2, 1),
            (5, 2, 2),
            (1, 3, 1),
            (4, 3, 1),
            (0, 4, 3),
            (2, 4, 2),
            (3, 4, 2),
            (5, 4, 3),
        ]
        for x, y, p in points:
            self.cardp[x][y] = p

        self.round = 0
        self.roll()

    def _genrand(self):
        return random.randint(1, 6)

    def roll(self):
        self.round += 1
        self.dice = [self._genrand(), self._genrand()]

    # def place(self, r, c):
    #     r2 = r + int(not self.dice.dir_horiz)
    #     c2 = c + int(self.dice.dir_horiz)

    #     if r2 < 5 and c2 < 5 and (self.card[r][c], self.card[r2][c2]) == (0, 0):
    #         self.card[r][c] = self.dice.v1
    #         self.card[r2][c2] = self.dice.v2
    #         self.dice = None

    # def _line_score(self, r, c, dr, dc, char):
    #     flag = False
    #     s = 0
    #     result = []
    #     for _ in range(5):
    #         if self.card[r][c] == char:
    #             if flag:
    #                 s += 1
    #             else:
    #                 s = 1
    #                 flag = True
    #         elif flag:
    #             flag = False
    #             result.append(s)

    #         r += dr
    #         c += dc

    #     return result + [s] if flag else result

    # def card_score(self):
    #     s = []
    #     for char in range(1, 7):
    #         for r in range(5):
    #             s.extend(self._line_score(r, 0, 0, 1, char))
    #             s.extend(self._line_score(0, r, 1, 0, char))
    #     return s.count(2) * 2 + s.count(3) * 3 + s.count(4) * 8 + s.count(5) * 10
