import random


class Domino:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.dir_horiz = True

    def flip(self):
        if self.dir_horiz:
            self.dir_horiz = False
            self.v1, self.v2 = self.v2, self.v1
        else:
            self.dir_horiz = True


class Game:
    def __init__(self):
        self.card = [[0 for _ in range(5)] for _ in range(5)]
        self.card[0][0] = self._genrand()
        self.round = 0
        self.dice = None

    def _genrand(self):
        return random.randint(1, 6)

    def roll(self):
        self.round += 1
        self.dice = Domino(self._genrand(), self._genrand())

    def is_game_over(self):  # will be reached in 12 rounds in any case
        for r in range(5):
            for c in range(5):
                vertplace = r < 4 and self.card[r + 1][c] == 0
                horizplace = c < 4 and self.card[r][c + 1] == 0
                if self.card[r][c] == 0 and (vertplace or horizplace):
                    return False
        return True

    def place(self, r, c):
        r2 = r + int(not self.dice.dir_horiz)
        c2 = c + int(self.dice.dir_horiz)

        if r2 < 5 and c2 < 5 and (self.card[r][c], self.card[r2][c2]) == (0, 0):
            self.card[r][c] = self.dice.v1
            self.card[r2][c2] = self.dice.v2
            self.dice = None

    def _line_score(self, r, c, dr, dc, char):
        flag = False
        s = 0
        result = []
        for _ in range(5):
            if self.card[r][c] == char:
                if flag:
                    s += 1
                else:
                    s = 1
                    flag = True
            elif flag:
                flag = False
                result.append(s)

            r += dr
            c += dc

        return result + [s] if flag else result

    def card_score(self):
        s = []
        for char in range(1, 7):
            for r in range(5):
                s.extend(self._line_score(r, 0, 0, 1, char))
                s.extend(self._line_score(0, r, 1, 0, char))
        return s.count(2) * 2 + s.count(3) * 3 + s.count(4) * 8 + s.count(5) * 10
