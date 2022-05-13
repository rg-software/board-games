import random
import copy


# white/rotten 0, blue 1, red 2, green 3
B = 1
R = 2
G = 3
DECK = [
    [[B, R], [R, B], [G, G]],
    [[B, R], [G, G], [R, B]],
    [[R, G], [B, B], [G, R]],
    [[G, R], [G, B], [R, B]],
    [[B, G], [B, R], [G, R]],
    [[B, B], [R, G], [G, R]],
    [[R, B], [R, G], [B, G]],
    [[G, B], [R, R], [B, G]],
    [[R, R], [G, B], [B, G]],
    [[G, R], [B, B], [G, R]],
    [[R, B], [G, G], [R, B]],
    [[R, B], [R, B], [G, G]],
    [[B, B], [R, G], [R, G]],
    [[B, G], [R, B], [G, R]],
    [[B, R], [B, G], [R, B]],
    [[R, R], [G, B], [G, B]],
    [[B, G], [R, R], [B, G]],
    [[R, B], [G, R], [B, G]],
]


class DiceBox:
    def __init__(self):
        self.dice = [2] + [5] * 3  # 2 rotten + 5 dice per each color

    def has_die(self, idx):
        return self.dice[idx] > 0

    def take_die(self, idx):
        self.dice[idx] -= 1

    def put_die(self, idx):
        self.dice[idx] += 1


class Stack:
    def __init__(self, dicebox):
        self._dicebox = dicebox
        self._data = []
        self._has_die = False
        self._die_score = -1

    # Scoring can be improved: we don't track if a die is placed on a large empty pile
    def score(self):
        if not self._has_die:
            return 0
        if self.is_rotten():
            return -3

        return [1, 3, 6, 10][min(self._die_score, 3)]  # stack score

    def has_data(self):
        return bool(self._data)

    def is_rotten(self):
        return self._has_die and min(self._data) != max(self._data)

    def top(self):
        return self._data[-1] if self.has_data() else 0

    # Note: we do not check that rotten card may enable another die on the same step
    def add(self, e):
        die = 0 if self.has_data() and e != self.top() else e

        if die == 0 and self._has_die:
            self._dicebox.put_die(self.top())  # rotten die replaces the existing die

        if not self._has_die and self.has_data() and self._dicebox.has_die(die):
            self._dicebox.take_die(die)
            self._has_die = True

        self._data.append(e)
        if self._has_die:
            self._die_score += 1


class Game:
    BOARDSIZE = 20

    def __init__(self):
        self.dicebox = DiceBox()
        self.deck = copy.deepcopy(DECK)
        random.shuffle(self.deck)
        self.deck = self.deck[:9]  # remove 9 random cards
        self.board = [self._empty_line() for _ in range(Game.BOARDSIZE)]
        self.hand = [self.deck.pop(), self.deck.pop()]
        self.place_card((2, 2))

    def score(self):
        return sum([sum([e.score() for e in r]) for r in self.board])

    def _empty_line(self):
        return [Stack(self.dicebox) for _ in range(Game.BOARDSIZE)]

    def _line_has_items(self, r, c, dr, dc):
        while max(r, c) < Game.BOARDSIZE:
            if self.board[r][c].has_data():
                return True
            r += dr
            c += dc
        return False

    def _move_down(self):
        self.board = [self._empty_line()] + self.board[:-1]

    def _move_right(self):
        for r, _ in enumerate(self.board):
            self.board[r] = [Stack(self.dicebox)] + self.board[r][:-1]

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
        have_rotten = self.dicebox.dice[0]
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
                stack.add(e)

        self.move_board()
        self.take_card()
