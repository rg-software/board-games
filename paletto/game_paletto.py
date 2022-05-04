import random
from collections import defaultdict

SIZE = 6
ATTEMPTS = 5


class Board:
    def __init__(self):
        self.data = [[0 for _ in range(SIZE + 2)] for _ in range(SIZE + 2)]

    def generate(self):
        while not self._fill_board():
            pass  # generation failed, retrying

    def _random_pick(self, pieces, bad_color1, bad_color2):
        for _ in range(ATTEMPTS):
            s = random.choice(pieces)
            if s not in (bad_color1, bad_color2):
                return s
        return 0

    def _fill_board(self):
        bag = list(range(1, 7)) * 6  # six pieces of colors 1-6

        for r in range(1, SIZE + 1):
            for c in range(1, SIZE + 1):
                color1, color2 = self.data[r][c - 1], self.data[r - 1][c]
                if (s := self._random_pick(bag, color1, color2)) == 0:
                    return False
                self.data[r][c] = s
                bag.remove(s)
        return True

    def pieces_count(self):
        # nonzero pieces = total pieces - zero pieces
        return (SIZE + 2) * (SIZE + 2) - sum(row.count(0) for row in self.data)

    def can_remove_color(self, r, c, current_color):
        return current_color in (0, self.data[r][c])  # 0 is ok and (r, c) is ok

    def no_adjacent_pieces(self, r, c):
        s = 0
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            s += int(self.data[r + dx][c + dy] == 0)  # sum zeroes
        return s >= 2

    def no_path_break(self, r, c):
        return self.pieces_count() == 1 or PathChecker(self).no_path_break(r, c)

    def choose_piece(self):
        for x in range(1, SIZE + 1):
            for y in range(1, SIZE + 1):
                if self.data[x][y]:
                    return (x, y)
        return None  # should not happen


class PathChecker:
    def __init__(self, board):
        self.board = board

    def no_path_break(self, x, y):
        c = self.board.data[x][y]
        self.board.data[x][y] = 0
        p_x, p_y = self.board.choose_piece()

        spillboard = Board()
        spillboard.data[p_x][p_y] = 1

        while self.spill(spillboard):
            pass

        self.board.data[x][y] = c

        return spillboard.pieces_count() + 1 == self.board.pieces_count()

    def spill(self, spboard):
        # if could advance liquid, return True
        p = spboard.pieces_count()
        for r in range(1, SIZE + 1):
            for c in range(1, SIZE + 1):
                if spboard.data[r][c]:
                    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if self.board.data[r + dy][c + dx] != 0:
                            spboard.data[r + dy][c + dx] = 1
        return p < spboard.pieces_count()


class Game:
    def __init__(self):
        self.board = Board()
        self.board.generate()
        self.p1_turn = True
        self.current_color = 0
        self.scorecards = {True: defaultdict(int), False: defaultdict(int)}

    def game_over(self):
        return self.collected_six() or self.board.pieces_count() == 0

    def collected_six(self):
        return 6 in self.scorecards[self.p1_turn].values()

    def can_remove_at(self, r, c):
        return (
            self.board.can_remove_color(r, c, self.current_color)
            and self.board.no_adjacent_pieces(r, c)
            and self.board.no_path_break(r, c)
        )

    def remove_at(self, r, c):
        self.current_color = self.board.data[r][c]
        self.board.data[r][c] = 0
        c = self.scorecards[self.p1_turn]
        c[self.current_color] += 1

    def end_turn(self):
        self.current_color = 0
        self.p1_turn = not self.p1_turn
