from enum import Enum


class Cell(Enum):
    EMPTY = 0
    FULL = 1
    HORIZ = 2  # : left side of a horizontal bar
    VERT = 3  # top side of a vertical bar


class Game:
    BoardWidth = 8
    BoardHeight = 8

    def __init__(self):
        self.board = [
            [Cell.EMPTY for _ in range(Game.BoardWidth)]
            for _ in range(Game.BoardHeight)
        ]
        self._is_current_horiz = True

    def _cell_on_board(self, r, c):
        return r < Game.BoardHeight and c < Game.BoardWidth

    def _cell_free(self, r, c):
        return self._cell_on_board(r, c) and self.board[r][c] == Cell.EMPTY

    def can_place_at(self, r, c):
        if self._is_current_horiz:
            return self._cell_free(r, c) and self._cell_free(r, c + 1)
        return self._cell_free(r, c) and self._cell_free(r + 1, c)

    def player_name(self):
        return "Horizontal" if self._is_current_horiz else "Vertical"

    def place_at(self, r, c):
        if self._is_current_horiz:
            self.board[r][c] = Cell.HORIZ
            self.board[r][c + 1] = Cell.FULL
        else:
            self.board[r][c] = Cell.VERT
            self.board[r + 1][c] = Cell.FULL

    def next_player(self):
        self._is_current_horiz = not self._is_current_horiz

    def is_game_over(self):
        for r in range(8):
            for c in range(8):
                if self.can_place_at(r, c):
                    return False
        return True
