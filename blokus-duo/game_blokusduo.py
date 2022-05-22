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

    def coords(self):
        return self._shape

    def flip(self):
        self._shape = self._align([(-x, y) for (x, y) in self._shape])

    def rotate(self):
        self._shape = self._align([(y, -x) for (x, y) in self._shape])

    def _align(self, shape):
        minx = min([x for (x, _) in shape])
        miny = min([y for (_, y) in shape])
        return [(x - minx, y - miny) for (x, y) in shape]


class PlayerData:
    def __init__(self, blocktype, startpos, name, color):
        self.blocks = [Block(s) for s in SHAPES]
        self.has_moves = True
        self.last_placed_size = 0
        self.blocktype = blocktype
        self.startpos = startpos
        self.name = name
        self.color = color

    def score(self):
        r = -sum([len(block.coords()) for block in self.blocks])
        if r == 0:  # used all blocks
            r = 20 if self.last_placed_size == 1 else 15
        return r


class Game:
    BoardWidth = 14
    BoardHeight = 14

    def __init__(self):
        self.board = [
            [Cell.EMPTY for _ in range(Game.BoardWidth)]
            for _ in range(Game.BoardHeight)
        ]

        # player 1 and player 2
        self._is_current_player_2 = False
        self._player_data = [
            PlayerData(Cell.BLOCK_1, (4, 4), "Player 1", "white"),
            PlayerData(Cell.BLOCK_2, (9, 9), "Player 2", "black"),
        ]

    def _current_player_data(self):
        return self._player_data[int(self._is_current_player_2)]

    def _cell_on_board(self, r, c):
        return r in range(Game.BoardHeight) and c in range(Game.BoardWidth)

    def _cell_free(self, r, c):
        return self._cell_on_board(r, c) and self.board[r][c] == Cell.EMPTY

    def _cell_neighbor(self, r, c, dlist):
        btype = self._current_player_data().blocktype
        coords = [(r + dx, c + dy) for dx, dy in dlist]
        for nr, nc in coords:
            if self._cell_on_board(nr, nc) and self.board[nr][nc] == btype:
                return True
        return False

    def _cell_adjacent(self, r, c):
        return self._cell_neighbor(r, c, [(-1, 0), (1, 0), (0, -1), (0, 1)])

    def _cell_touching_corner(self, r, c):
        return self._cell_neighbor(r, c, [(-1, -1), (1, 1), (1, -1), (-1, 1)])

    def get_block(self, idx):
        return self._current_player_data().blocks[idx]

    def rotate_block(self, idx):
        self.get_block(idx).rotate()

    def flip_block(self, idx):
        self.get_block(idx).flip()

    def block_shape(self, idx):
        return self.get_block(idx).coords()

    def prev_block(self, idx):
        return (idx - 1) % len(self._current_player_data().blocks)

    def next_block(self, idx):
        return (idx + 1) % len(self._current_player_data().blocks)

    def next_player(self):
        self._is_current_player_2 = not self._is_current_player_2
        self._current_player_data().has_moves = self.has_legal_moves()

    def can_place_at(self, r, c, block):
        result = False
        for dr, dc in block.coords():
            row, col = r + dr, c + dc

            if not self._cell_free(row, col) or self._cell_adjacent(row, col):
                return False

            startpos = self._current_player_data().startpos
            first_move = len(self._current_player_data().blocks) == len(SHAPES)
            first_move_ok = first_move and startpos == (row, col)
            corner_rule_ok = not first_move and self._cell_touching_corner(row, col)

            result = result or corner_rule_ok or first_move_ok

        return result

    def player_name(self):
        return self._current_player_data().name

    def player_color(self):
        return self._current_player_data().color

    def place_at(self, r, c, block):
        blocktype = self._current_player_data().blocktype

        for dr, dc in block.coords():
            self.board[r + dr][c + dc] = blocktype

        self._current_player_data().last_placed_size = len(block.coords())
        self._current_player_data().blocks.remove(block)

    def _can_place_on_board(self, block):
        for r in range(Game.BoardHeight):
            for c in range(Game.BoardWidth):
                if self.can_place_at(r, c, block):
                    return True
        return False

    def has_legal_moves(self):
        for block in self._current_player_data().blocks:
            for _ in range(2):
                for _ in range(4):
                    if self._can_place_on_board(block):
                        return True
                    block.rotate()
                block.flip()

        return False

    def is_game_over(self):
        return all((not p.has_moves for p in self._player_data))

    def hints(self, block):
        coord = []
        for r in range(Game.BoardHeight):
            for c in range(Game.BoardWidth):
                if self.can_place_at(r, c, block):
                    coord.append((r, c))
        return coord

    def final_score(self):
        return [p.score() for p in self._player_data]
