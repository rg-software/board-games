class Game:
    def __init__(self):
        self.board = [["." for _ in range(5)] for _ in range(5)]
        self.player_char = "o"

    def _five_in_row(self, r, c, dr, dc, char):
        v = [self.board[r + i * dr][c + i * dc] for i in range(5)]
        return v.count(char) == 5

    def winner_char(self):
        if self._game_over("x"):
            return "x"
        if self._game_over("o"):
            return "o"
        return None

    def _game_over(self, ch):
        return True in (
            [self._five_in_row(k, 0, 0, 1, ch) for k in range(5)]  # horizontal
            + [self._five_in_row(0, k, 1, 0, ch) for k in range(5)]  # vertical
            + [self._five_in_row(0, 0, 1, 1, ch)]  # diagonal 1
            + [self._five_in_row(0, 4, 0, -1, ch)]  # diagonal 2
        )

    def next_player(self):
        self.player_char = "x" if self.player_char == "o" else "o"

    def _is_illegal_move(self, r, c, dir):
        in_board_core = r in range(1, 4) and c in range(1, 4)
        return (
            self.board[r][c] not in (".", self.player_char)
            or in_board_core
            or (r == 0 and dir == "t")
            or (r == 4 and dir == "b")
            or (c == 0 and dir == "l")
            or (c == 4 and dir == "r")
        )

    def push(self, r, c, dir):
        if v := not self._is_illegal_move(r, c, dir):
            self._do_push(r, c, dir)
        return v

    def _do_push(self, r, c, dir):
        dirs = {"t": (-1, 0), "b": (1, 0), "l": (0, -1), "r": (0, 1)}
        dr, dc = dirs[dir]

        while r + dr in range(5) and c + dc in range(5):  # for _ in range(4):
            self.board[r][c] = self.board[r + dr][c + dc]
            r += dr
            c += dc
        self.board[r][c] = self.player_char
