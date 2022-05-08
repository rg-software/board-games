import random
import copy


# white/rotten 0, blue 1, red 2, green 3
b = 1
r = 2
g = 3
DECK = [
    [[b, r], [r, b], [g, g]],
    [[b, r], [g, g], [r, b]],
    [[r, g], [b, b], [g, r]],
    [[g, r], [g, b], [r, b]],
    [[b, g], [b, r], [g, r]],
    [[b, b], [r, g], [g, r]],
    [[r, b], [r, g], [b, g]],
    [[g, b], [r, r], [b, g]],
    [[r, r], [g, b], [b, g]],
    [[g, r], [b, b], [g, r]],
    [[r, b], [g, g], [r, b]],
    [[r, b], [r, b], [g, g]],
    [[b, b], [r, g], [r, g]],
    [[b, g], [r, b], [g, r]],
    [[b, r], [b, g], [r, b]],
    [[r, r], [g, b], [g, b]],
    [[b, g], [r, r], [b, g]],
    [[r, b], [g, r], [b, g]],
]


class Stack:
    def __init__(self):
        self.data = []
        self.has_die = False

    def score(self):
        if not self.has_die:
            return 0
        elif self.is_rotten():
            return -3

        return [1, 3, 6, 10][min(len(self.data) - 2, 3)]  # stack score

    def is_rotten(self):
        return self.has_die and self.data[0] != self.data[1]

    def is_empty(self):
        return not self.data

    def top(self):
        return 0 if self.is_empty() else self.data[-1]

    def add(self, value, add_die):
        self.data.append(value)
        self.has_die = self.has_die or add_die


class Game:
    BOARDSIZE = 20

    def __init__(self):
        self.dice = [2] + [5] * 3
        self.deck = copy.deepcopy(DECK)
        random.shuffle(self.deck)
        self.deck = self.deck[:9]
        self.board = [self._empty_line() for _ in range(Game.BOARDSIZE)]
        self.hand = [self.deck.pop(), self.deck.pop()]
        self.place_card((2, 2))

    def score(self):
        return sum([sum([e.score() for e in r]) for r in self.board])

    def _empty_line(self):
        return [Stack() for _ in range(Game.BOARDSIZE)]

    def _line_has_items(self, r, c, dr, dc):
        while max(r, c) < Game.BOARDSIZE:
            if not self.board[r][c].is_empty():
                return True
            r += dr
            c += dc
        return False

    def _move_down(self):
        self.board = [self._empty_line()] + self.board[:-1]

    def _move_right(self):
        for r, _ in enumerate(self.board):
            self.board[r] = [Stack()] + self.board[r][:-1]

    def move_board(self):
        while self._line_has_items(0, 0, 0, 1) or self._line_has_items(1, 0, 0, 1):
            self._move_down()

        while self._line_has_items(0, 0, 1, 0) or self._line_has_items(0, 1, 1, 0):
            self._move_right()

    def swap_cards(self):
        if self.hand[1]:
            self.hand = [self.hand[1], self.hand[0]]

    def rotate_card(self):
        card = self.hand[0]
        result = []
        for c in range(len(card[0])):
            row = [card[r][c] for r in range(len(card))]
            result = [row] + result
        self.hand[0] = result

    def take_card(self):
        self.hand[0] = self.hand[1]
        self.hand[1] = None if not self.deck else self.deck.pop(0)

    # ideally we should also check whether it is possible to place the next card
    def game_over(self):
        return not self.hand[0]

    def can_place(self, rc):
        card = self.hand[0]
        overlaps = False
        have_rotten = self.dice[0]
        for r_idx, row in enumerate(card):
            for c_idx, card_e in enumerate(row):
                board_e = self.board[rc[0] + r_idx][rc[1] + c_idx]

                if board_e.is_rotten():  # cannot place on rotten
                    return False

                if board_e.top() != 0:  # has something placed
                    overlaps = True
                    if board_e.top() != card_e:
                        have_rotten -= 1

        return overlaps and have_rotten >= 0

    def place_card(self, rc):
        card = self.hand[0]
        for r_idx, row in enumerate(card):
            for c_idx, e in enumerate(row):
                stack = self.board[rc[0] + r_idx][rc[1] + c_idx]
                die = 0 if not stack.is_empty() and e != stack.top() else e

                use_die = not (stack.has_die or stack.is_empty()) and self.dice[die] > 0
                self.dice[die] -= int(use_die)
                stack.add(e, use_die)

        self.move_board()
        self.take_card()
