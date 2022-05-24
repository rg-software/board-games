from enum import Enum

GameState = Enum("GameState", ["START", "MOVE", "PUSH", "OVER"])
PieceColor = Enum("PieceColor", ["WHITE", "BROWN"])
PieceShape = Enum("PieceShape", ["ROUND", "SQUARE"])


class Piece:
    def __init__(self, color, shape, has_anchor=False):
        self.color = color
        self.shape = shape
        self.has_anchor = has_anchor
        self.is_piece = True

    def start_columns(self):
        return range(5, 10) if self.color == PieceColor.WHITE else range(0, 5)

    def is_free(self):
        return False


class Empty:
    def __init__(self, is_lava=False):
        self.is_lava = is_lava
        self.is_piece = False

    def is_free(self):
        return not self.is_lava


class Game:
    BoardWidth = 10
    BoardHeight = 4

    def __init__(self):
        lava1 = [[(r, 0), (r, 9)] for r in range(4)]
        lava2 = [[(0, c + 1), (0, c + 8), (3, c), (3, c + 7)] for c in range(2)]
        lava = set(sum(lava1 + lava2, []))

        self.board = [
            [Empty((r, c) in lava) for c in range(Game.BoardWidth)]
            for r in range(Game.BoardHeight)
        ]

        self._in_box = (
            [Piece(PieceColor.WHITE, PieceShape.SQUARE) for _ in range(3)]
            + [Piece(PieceColor.WHITE, PieceShape.ROUND) for _ in range(2)]
            + [Piece(PieceColor.BROWN, PieceShape.SQUARE) for _ in range(3)]
            + [Piece(PieceColor.BROWN, PieceShape.ROUND) for _ in range(2)]
        )

        self.state = GameState.START
        self.moves = 2
        self.current_team_brown = False
        self.selected_piece_on = (-1, -1)

    def box_top(self):
        return self._in_box[0]

    def _current_color(self):
        return PieceColor.BROWN if self.current_team_brown else PieceColor.WHITE

    def on_board(self, r, c):
        return r in range(Game.BoardHeight) and c in range(Game.BoardWidth)

    def place_new_piece(self, r, c):
        if self.board[r][c].is_free() and c in self._in_box[0].start_columns():
            self.board[r][c] = self._in_box.pop(0)
            if not self._in_box:
                self.state = GameState.MOVE

    def _is_selectable(self, r, c):
        piece = self.board[r][c]
        result = False
        if piece.is_piece and piece.color == self._current_color():
            state_move = self.state == GameState.MOVE
            state_push = self.state == GameState.PUSH
            push_ok = not piece.has_anchor and piece.shape == PieceShape.SQUARE
            result = state_move or (state_push and push_ok)
        return result

    def select_piece(self, r, c):
        if self._is_selectable(r, c):
            self.selected_piece_on = (r, c)

    def can_move_at(self, r, c):
        if self.board[r][c].is_free() and self.selected_piece_on != (-1, -1):
            queue = [self.selected_piece_on]
            processed = set()
            while len(queue) != 0:
                cr, cc = queue[0]
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = cr + dr
                    nc = cc + dc
                    is_free = self.on_board(nr, nc) and self.board[nr][nc].is_free()
                    if (nr, nc) not in processed and is_free:
                        queue.append((nr, nc))

                if (r, c) in queue:
                    return True

                processed.add((cr, cc))
                queue.remove((cr, cc))
        return False

    def move_at(self, r, c):
        p_r, p_c = self.selected_piece_on
        self.board[r][c] = self.board[p_r][p_c]
        self.board[p_r][p_c] = Empty()
        self.move_done()

    def move_done(self, count=1):
        self.moves -= count
        if self.moves == 0:
            self.state = GameState.PUSH
            if not self._can_push():
                self.state = GameState.OVER
        self.selected_piece_on = (-1, -1)

    def _can_push_from_loc(self, r, c):
        if self._is_selectable(r, c):
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                self.selected_piece_on = (r, c)
                nr = r + dr
                nc = c + dc
                if self.can_push_pieces(nr, nc) > 1:
                    return True
        return False

    def _can_push(self):
        for r in range(Game.BoardHeight):
            for c in range(Game.BoardWidth):
                if self._can_push_from_loc(r, c):
                    return True
        return False

    def can_push_pieces(self, r, c):
        dr = r - self.selected_piece_on[0]
        dc = c - self.selected_piece_on[1]
        r, c = self.selected_piece_on

        if abs(dr) + abs(dc) != 1:
            return False

        push_distance = 0

        while self.on_board(r, c):
            if not self.board[r][c].is_piece:
                return push_distance
            if self.board[r][c].has_anchor:
                return 0
            r += dr
            c += dc
            push_distance += 1
        return 0

    def _remove_anchor(self):
        for r in self.board:
            for cell in r:
                if cell.is_piece and cell.has_anchor:
                    cell.has_anchor = False
                    return

    def push_at(self, r, c, pieces):
        self._remove_anchor()

        dr = r - self.selected_piece_on[0]
        dc = c - self.selected_piece_on[1]
        r, c = self.selected_piece_on
        self.board[r][c].has_anchor = True

        prev_piece = Empty()
        for _ in range(pieces + 1):  # including empty piece
            piece = self.board[r][c]
            self.board[r][c] = prev_piece
            prev_piece = piece
            r += dr
            c += dc

        self._next_player()
        if prev_piece.is_lava:
            if self.board[r - dr][c - dc].color != self._current_color():
                self._next_player()  # make sure the right is the winner
            self.state = GameState.OVER

    def _next_player(self):
        self.state = GameState.MOVE
        self.selected_piece_on = (-1, -1)
        self.moves = 2
        self.current_team_brown = not self.current_team_brown

    def is_game_over(self):
        return self.state == GameState.OVER

    def player_name(self):
        return "Brown" if self.current_team_brown else "White"

    def moves_left(self):
        return self.moves

    def game_state(self):
        return self.state

    def selected_cell(self):
        return self.selected_piece_on
