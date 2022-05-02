class Game:
    def __init__(self):
        self.board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
        self.upper_player_move = False

    def opp_storage(self):
        return 7 if self.upper_player_move else 0

    def my_storage(self):
        return 0 if self.upper_player_move else 7

    def my_houses(self):
        return range(8, 14) if self.upper_player_move else range(1, 7)

    def _opposite_house(self, house_no):
        return 14 - house_no

    def _next_pit(self, house_no):
        r = (house_no + 1) % 14
        return r if r != self.opp_storage() else r + 1

    def _can_capture(self, last_house):
        return (
            last_house in self.my_houses()
            and self.board[last_house] == 1
            and self.board[self._opposite_house(last_house)] > 0
        )

    def _do_capture(self, last_house):
        captured = self.board[self._opposite_house(last_house)] + 1
        self.board[self._opposite_house(last_house)] = 0
        self.board[last_house] = 0
        self.board[self.my_storage()] += captured

    def is_end_game(self):
        for i in self.my_houses():
            if self.board[i] > 0:
                return False
        return True

    def capture_remaining(self):
        for sh in self.my_houses():
            i = self._opposite_house(sh)
            self.board[self.opp_storage()] += self.board[i]
            self.board[i] = 0

    def make_move(self, house_no):
        current_pit = house_no
        seeds = self.board[current_pit]
        self.board[current_pit] = 0

        # sowing
        for _ in range(seeds):
            current_pit = self._next_pit(current_pit)
            self.board[current_pit] += 1

        # ended in my storage: keep my turn
        if current_pit == self.my_storage():
            return

        # capture rule: ended in empty house on my side, opp is not empty
        if self._can_capture(current_pit):
            self._do_capture(current_pit)

        self.upper_player_move = not self.upper_player_move
