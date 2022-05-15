from enum import Enum


class Pieces(Enum):
    B_PAWN = 1
    W_PAWN = 2
    B_KING = 3
    W_KING = 4
    EMPTY = 5


class Player(Enum):
    WHITE = 1
    BLACK = 2
    NONE = 3


class Game:
    def __init__(self):
        self.board = self._gen_board()
        self.player = Player.WHITE

    def _gen_board(self):
        board = [[Pieces.EMPTY for _ in range(5)] for _ in range(5)]
        for i in range(5):
            board[0][i] = Pieces.B_PAWN
            board[4][i] = Pieces.W_PAWN

        # advanced setup
        board[0][2] = Pieces.W_KING
        board[4][2] = Pieces.B_KING
        return board

    def _get_speeds(self, direction):
        speeds = {
            "N": (-1, 0),
            "S": (1, 0),
            "W": (0, -1),
            "E": (0, 1),
            "NW": (-1, -1),
            "NE": (-1, 1),
            "SW": (1, -1),
            "SE": (1, 1),
        }
        return speeds[direction]

    def _can_go_to(self, r, c):
        return r in range(5) and c in range(5) and self.board[r][c] == Pieces.EMPTY

    def move(self, r, c, direction):
        pieces = {
            Player.WHITE: [Pieces.W_KING, Pieces.W_PAWN],
            Player.BLACK: [Pieces.B_KING, Pieces.B_PAWN],
        }

        if self.board[r][c] not in pieces[self.player]:
            return False

        vr, vc = self._get_speeds(direction)
        nr, nc = r, c
        while self._can_go_to(nr + vr, nc + vc):
            nr += vr
            nc += vc

        self.board[r][c], self.board[nr][nc] = self.board[nr][nc], self.board[r][c]
        return r != nr or c != nc

    def _find_piece(self, piece):
        for r in range(5):
            for c in range(5):
                if self.board[r][c] == piece:
                    return r, c

    def _captured(self, piece):
        r, c = self._find_piece(piece)
        for nr in range(r - 1, r + 2):
            for nc in range(c - 1, c + 2):
                if self._can_go_to(nr, nc):
                    return False
        return True

    def winner(self):
        if self.board[2][2] == Pieces.B_KING or self._captured(Pieces.W_KING):
            return Player.BLACK
        if self.board[2][2] == Pieces.W_KING or self._captured(Pieces.B_KING):
            return Player.WHITE
        return Player.NONE

    def pass_turn(self):
        self.player = Player.BLACK if self.player == Player.WHITE else Player.WHITE
