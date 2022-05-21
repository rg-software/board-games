from enum import Enum

SHAPES = [
    [(0, 0)],
    [(0, 0), (0, 1)],
    [(0, 0), (0, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
    [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)],
    [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)],
]


class Cell(Enum):
    EMPTY = 0
    BLOCK_1 = 1  # player 1
    BLOCK_2 = 2  # player 2


class Block:
    def __init__(self, shape):
        self._shape = shape

    def coord(self):
        return self._shape

    def flip(self):
        self._shape = self._align([(-x, y) for (x, y) in self._shape])

    def rotate(self):
        self._shape = self._align([(y, -x) for (x, y) in self._shape])

    def _align(self, shape):
        minx = min([x for (x, _) in shape])
        miny = min([y for (_, y) in shape])
        return [(x - minx, y - miny) for (x, y) in shape]


class Game:
    BoardWidth = 14
    BoardHeight = 14

    def __init__(self):
        self.board = [
            [Cell.EMPTY for _ in range(Game.BoardWidth)]
            for _ in range(Game.BoardHeight)
        ]

        # player 1 and player 2
        self._blocks = [[Block(s) for s in SHAPES], [Block(s) for s in SHAPES]]
        self._is_current_player_2 = False

    def _cell_on_board(self, r, c):
        return r in range(Game.BoardHeight) and c in range(Game.BoardWidth)

    def _cell_free(self, r, c):
        return self._cell_on_board(r, c) and self.board[r][c] == Cell.EMPTY

    def _cell_neighbor(self, r, c, dlist):
        btype = self._current_player_blocktype()
        coords = [(r + dx, c + dy) for dx, dy in dlist]
        for nr, nc in coords:
            if self._cell_on_board(nr, nc) and self.board[nr][nc] == btype:
                return True
        return False

    def _cell_adjacent(self, r, c):
        return self._cell_neighbor(r, c, [(-1, 0), (1, 0), (0, -1), (0, 1)])

    def _cell_touching_corner(self, r, c):
        return self._cell_neighbor(r, c, [(-1, -1), (1, 1), (1, -1), (-1, 1)])

    def _current_player_blocktype(self):
        return Cell.BLOCK_2 if self._is_current_player_2 else Cell.BLOCK_1

    def _current_player_blocks(self):
        return self._blocks[int(self._is_current_player_2)]

    def get_block(self, idx):
        return self._current_player_blocks()[idx]

    def rotate_block(self, idx):
        self.get_block(idx).rotate()

    def flip_block(self, idx):
        self.get_block(idx).flip()

    def block_shape(self, idx):
        return self.get_block(idx).coord()

    def prev_block(self, idx):
        return max(0, idx - 1)

    def next_block(self, idx):
        return min(idx + 1, len(self._current_player_blocks()) - 1)

    def next_player(self):
        self._is_current_player_2 = not self._is_current_player_2

    def can_place_at(self, r, c, block):
        result = False
        for dr, dc in block.coord():
            row, column = r + dr, c + dc

            if not self._cell_free(row, column) or self._cell_adjacent(row, column):
                return False

            startpos = (9, 9) if self._is_current_player_2 else (4, 4)
            first_move = len(self._current_player_blocks()) == len(SHAPES)
            first_move_ok = first_move and startpos == (row, column)
            corner_rule_ok = not first_move and self._cell_touching_corner(row, column)

            result = result or corner_rule_ok or first_move_ok

        return result

    def player_name(self):
        return "PLAYER 2" if self._is_current_player_2 else "PLAYER 1"

    def player_color(self):
        return "black" if self._is_current_player_2 else "white"

    def place_at(self, r, c, block):
        blocktype = self._current_player_blocktype()

        for dr, dc in block.coord():
            self.board[r + dr][c + dc] = blocktype

        self._current_player_blocks().remove(block)

    def _can_place_on_board(self, block):
        for r in range(Game.BoardHeight):
            for c in range(Game.BoardWidth):
                if self.can_place_at(r, c, block):
                    return True
        return False

    def is_game_over(self):
        for block in self._current_player_blocks():
            for _ in range(2):
                for _ in range(4):
                    if self._can_place_on_board(block):
                        return False
                    block.rotate()
                block.flip()

        return True

    def hints(self, block):
        coord = []
        for r in range(Game.BoardHeight):
            for c in range(Game.BoardWidth):
                if self.can_place_at(r, c, block):
                    coord.append((r, c))
        return coord
