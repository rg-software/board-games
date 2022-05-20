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
    def __init__(self, blocktype):
        self.shape = SHAPES[blocktype]

    def coord(self):
        return self.shape

    def flip(self):
        coord = self.shape
        for i in range(len(coord)):
            x, y = coord[i]
            coord[i] = x * (-1), y
        self.alignment()
        self.shape = coord

    def rotate(self):
        coord = self.shape
        for i in range(len(coord)):
            x, y = coord[i]
            coord[i] = y, x * (-1)
        self.alignment()
        self.shape = coord

    def alignment(self):
        coord = self.shape
        while any(e[0] < 0 for e in coord):
            for i in range(len(coord)):
                x, y = coord[i]
                coord[i] = x + 1, y
        while any(e[1] < 0 for e in coord):
            for i in range(len(coord)):
                x, y = coord[i]
                coord[i] = x, y + 1
        self.shape = coord


class Game:
    BoardWidth = 14
    BoardHeight = 14

    def __init__(self):
        self.board = [
            [Cell.EMPTY for _ in range(Game.BoardWidth)]
            for _ in range(Game.BoardHeight)
        ]
        self.blocks_player_1 = [Block(n) for n in range(len(SHAPES))]
        self.blocks_player_2 = [Block(n) for n in range(len(SHAPES))]
        self.current_block = self.blocks_player_1[0]
        self._is_current_player_1 = True

    def _cell_on_board(self, r, c):
        return r < Game.BoardHeight and c < Game.BoardWidth

    def _cell_free(self, r, c):
        return self._cell_on_board(r, c) and self.board[r][c] == Cell.EMPTY

    def _cell_adjacent(self, r, c):
        if self._is_current_player_1:
            if (
                (self._cell_on_board(r + 1, c) and self.board[r + 1][c] == Cell.BLOCK_1)
                or (
                    self._cell_on_board(r - 1, c)
                    and self.board[r - 1][c] == Cell.BLOCK_1
                )
                or (
                    self._cell_on_board(r, c + 1)
                    and self.board[r][c + 1] == Cell.BLOCK_1
                )
                or (
                    self._cell_on_board(r, c - 1)
                    and self.board[r][c - 1] == Cell.BLOCK_1
                )
            ):
                return True
        else:
            if (
                (self._cell_on_board(r + 1, c) and self.board[r + 1][c] == Cell.BLOCK_2)
                or (
                    self._cell_on_board(r - 1, c)
                    and self.board[r - 1][c] == Cell.BLOCK_2
                )
                or (
                    self._cell_on_board(r, c + 1)
                    and self.board[r][c + 1] == Cell.BLOCK_2
                )
                or (
                    self._cell_on_board(r, c - 1)
                    and self.board[r][c - 1] == Cell.BLOCK_2
                )
            ):
                return True
        return False

    def _cell_touching_corner(self, r, c):
        if self._is_current_player_1:
            if (
                (
                    self._cell_on_board(r + 1, c + 1)
                    and self.board[r + 1][c + 1] == Cell.BLOCK_1
                )
                or (
                    self._cell_on_board(r - 1, c + 1)
                    and self.board[r - 1][c + 1] == Cell.BLOCK_1
                )
                or (
                    self._cell_on_board(r + 1, c - 1)
                    and self.board[r + 1][c - 1] == Cell.BLOCK_1
                )
                or (
                    self._cell_on_board(r - 1, c - 1)
                    and self.board[r - 1][c - 1] == Cell.BLOCK_1
                )
            ):
                return True
        else:
            if (
                (
                    self._cell_on_board(r + 1, c + 1)
                    and self.board[r + 1][c + 1] == Cell.BLOCK_2
                )
                or (
                    self._cell_on_board(r - 1, c + 1)
                    and self.board[r - 1][c + 1] == Cell.BLOCK_2
                )
                or (
                    self._cell_on_board(r + 1, c - 1)
                    and self.board[r + 1][c - 1] == Cell.BLOCK_2
                )
                or (
                    self._cell_on_board(r - 1, c - 1)
                    and self.board[r - 1][c - 1] == Cell.BLOCK_2
                )
            ):
                return True
        return False

    def select_block(self, b):
        if self._is_current_player_1 and 0 <= b <= len(self.blocks_player_1):
            self.current_block = self.blocks_player_1[b]
        if not self._is_current_player_1 and 0 <= b <= len(self.blocks_player_2):
            self.current_block = self.blocks_player_2[b]
        return self.current_block

    def rotate_current_block(self):
        self.current_block.rotate()

    def flip_current_block(self):
        self.current_block.flip()

    def current_block_shape(self):
        return self.current_block.coord()

    def next_block(self, m):
        if self._is_current_player_1:
            i = self.blocks_player_1.index(self.current_block)
            i = i + m
            if i < 0:
                i = len(self.blocks_player_1) - 1
            if i >= len(self.blocks_player_1):
                i = 0
            self.current_block = self.blocks_player_1[i]
        else:
            i = self.blocks_player_2.index(self.current_block)
            i = i + m
            if i < 0:
                i = len(self.blocks_player_2) - 1
            if i >= len(self.blocks_player_2):
                i = 0
            self.current_block = self.blocks_player_2[i]

    def can_place_at(self, r, c, b):
        block = b if b != 0 else self.current_block
        coord = block.coord()
        any_corner = False
        for d in coord:
            row = r + d[0]
            column = c + d[1]
            if not self._cell_free(row, column):
                return False
            if self._cell_adjacent(row, column):
                return False
            if len(SHAPES) != len(self.blocks_player_1) and len(SHAPES) != len(
                self.blocks_player_2
            ):
                if self._cell_touching_corner(row, column):
                    any_corner = True
            else:
                any_corner = True
        if not any_corner:
            return False
        return True

    def player_name(self):
        return "PLAYER_1" if self._is_current_player_1 else "PLAYER_2"

    def place_at(self, r, c):
        coord = self.current_block.coord()
        for d in coord:
            row = r + d[0]
            column = c + d[1]
            if self._is_current_player_1:
                self.board[row][column] = Cell.BLOCK_1
            else:
                self.board[row][column] = Cell.BLOCK_2

        if self._is_current_player_1:
            self.blocks_player_1.remove(self.current_block)
            self.current_block = self.blocks_player_2[0]
        else:
            self.blocks_player_2.remove(self.current_block)
            self.current_block = self.blocks_player_1[0]

    def next_player(self):
        self._is_current_player_1 = not self._is_current_player_1

    def is_game_over(self):
        blocks_left = (
            self.blocks_player_1 if self._is_current_player_1 else self.blocks_player_2
        )

        # Да. Я знаю. Но ничего лучше я не придумала.
        # Нам нужно проверить все клетки на все фигуры и их варианты...

        for block in blocks_left:
            for _ in range(2):
                for _ in range(4):
                    for r in range(Game.BoardHeight):
                        for c in range(Game.BoardWidth):
                            if self.can_place_at(r, c, block):
                                return False
                    block.rotate()
                block.flip()

        return True

    # Это подсказка. На поле выводится кружечек куда можно тыкнуть :)
    # Я сделала ее для своего удобства. Ее можно удалить.
    def hints(self):
        coord = []
        for r in range(Game.BoardHeight):
            for c in range(Game.BoardWidth):
                if self.can_place_at(r, c, 0):
                    coord.append((r, c))
        return coord
