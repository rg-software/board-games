class Game:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.board[3][3] = self.board[4][4] = False
        self.board[4][3] = self.board[3][4] = True
        self.whites_move = True

    def player_name(self):
        return "white" if self.whites_move else "black"

    # can reverse so many pieces in the given direction (dr, dc)
    def _reverse_count(self, r, c, dr, dc):
        count = 0
        while True:
            r = r + dr
            c = c + dc
            if r not in range(8) or c not in range(8) or self.board[r][c] is None:
                return 0  # board border reached
            if self.board[r][c] == self.whites_move:  # self color reached
                return count

            count += 1  # opponent color, counting

    def _reverse(self, r, c, dr, dc, cnt):
        for _ in range(cnt):
            r = r + dr
            c = c + dc
            self.board[r][c] = not self.board[r][c]

    def _reverse_dirs(self, r, c):
        result = []
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if (dr or dc) and (cnt := self._reverse_count(r, c, dr, dc)) > 0:
                    result.append((dr, dc, cnt))
        return result

    def _reverse_all(self, r, c, dirs):
        for dr, dc, count in dirs:
            self._reverse(r, c, dr, dc, count)

    def move_allowed(self, r, c):
        if self.board[r][c] is not None:
            return False

        return self._reverse_dirs(r, c)

    def move(self, r, c):
        self.board[r][c] = self.whites_move
        self._reverse_all(r, c, self._reverse_dirs(r, c))
        self.pass_move()

    def pass_move(self):
        self.whites_move = not self.whites_move

    def has_legal_moves(self):
        for r in range(8):
            for c in range(8):
                if self.move_allowed(r, c):
                    return True
        return False

    def count_pieces(self, color):
        return sum(row.count(color) for row in self.board)
