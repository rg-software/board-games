from enum import Enum
import numpy as np

class GameState(Enum):
    START = 0
    MOVE = 1
    PUSH = 2
    OVER = 3
    
class Cell(Enum):
    EMPTY = 0   
    LAVA = 1

    WHITE_ROUND = 2
    WHITE_SQUARE = 4
    WHITE_ANCHOR = 6

    BROWN_SQUARE = 3
    BROWN_ROUND = 5    
    BROWN_ANCHOR = 7

class Game:
    BoardWidth = 10
    BoardHeight = 4
    in_box = [Cell.WHITE_SQUARE, Cell.BROWN_SQUARE, Cell.WHITE_ROUND, Cell.BROWN_ROUND,
              Cell.WHITE_SQUARE, Cell.BROWN_SQUARE, Cell.WHITE_ROUND, Cell.BROWN_ROUND, 
              Cell.WHITE_SQUARE, Cell.BROWN_SQUARE]

    def __init__(self):
        self.board = [
            [Cell.EMPTY for _ in range(Game.BoardWidth)]
            for _ in range(Game.BoardHeight)
        ]
        for c in range(Game.BoardWidth):
            for r in range(Game.BoardHeight):
                if c == 0 or c == 9: self.board[r][c] = Cell.LAVA
                if r == 0 and (c == 1 or c == 2 or c == 8): self.board[r][c] = Cell.LAVA
                if r == 3 and (c == 1 or c == 7 or c == 8): self.board[r][c] = Cell.LAVA
        
        self.state = GameState.START
        self.white_team = []
        self.brown_team = []
        self.moves = 2
        self.current_team = self.white_team
        self.selected_piece_on = (0,0)

    def _cell_on_board(self, r, c):
        return 0 <= r < Game.BoardHeight and 0 <= c < Game.BoardWidth

    def _cell_free(self, r, c):
        return self._cell_on_board(r, c) and self.board[r][c] == Cell.EMPTY

    def _lava_cell(self, r, c):
        return self._cell_on_board(r, c) and self.board[r][c] == Cell.LAVA   

    def starting_position(self, r, c):
        if (Game.in_box[0] == Cell.WHITE_SQUARE or Game.in_box[0] == Cell.WHITE_ROUND) and c > 4 and self._cell_free(r, c):           
            self.white_team.append(Game.in_box[0])
            self.board[r][c] = Game.in_box[0]
            del Game.in_box[0]
        if (Game.in_box[0] == Cell.BROWN_SQUARE or Game.in_box[0] == Cell.BROWN_ROUND) and c < 5 and self._cell_free(r, c): 
            self.brown_team.append(Game.in_box[0])
            self.board[r][c] = Game.in_box[0]
            del Game.in_box[0]
            
        if len(self.brown_team) == 5: 
            self.state = GameState.MOVE 

    def select_piece(self, r, c):
        if self._cell_on_board(r, c) and self.board[r][c] in self.current_team:
            if self.state == GameState.MOVE:
                self.selected_piece_on = (r, c)
            elif self.board[r][c] in [Cell.WHITE_SQUARE, Cell.BROWN_SQUARE]:
                self.selected_piece_on = (r, c)

    def can_move_at(self, r, c): 
        if self._cell_free(r, c) and self.selected_piece_on != (0,0):
            p_r, p_c = self.selected_piece_on            
            queue = []
            queue.append((p_r, p_c))
            processed = []
            while len(queue) != 0: 
                x, y = queue[0]
                if (x+1,y) not in processed and self._cell_on_board(x+1,y) and self.board[x+1][y] == Cell.EMPTY: queue.append((x+1, y))
                if (x-1,y) not in processed and self._cell_on_board(x-1,y) and self.board[x-1][y] == Cell.EMPTY: queue.append((x-1, y))
                if (x,y+1) not in processed and self._cell_on_board(x,y+1) and self.board[x][y+1] == Cell.EMPTY: queue.append((x, y+1))
                if (x,y-1) not in processed and self._cell_on_board(x,y-1) and self.board[x][y-1] == Cell.EMPTY: queue.append((x, y-1))
                if (r, c) in queue: return True 
                processed.append((x, y))
                queue.remove((x, y))
        return False    

    def move_at(self, r, c):
        p_r, p_c = self.selected_piece_on
        self.board[r][c] = self.board[p_r][p_c]
        self.board[p_r][p_c] = Cell.EMPTY
        self.move_done()        
        
    def move_done(self):   
        self.selected_piece_on = (0,0)
        self.moves = self.moves - 1 
        if self.moves == 0: 
            self.state = GameState.PUSH 

    def can_push_at(self, r, c): 
        if (self._cell_free(r, c) or self._lava_cell(r, c)) and self.selected_piece_on != (0,0):
            p_r, p_c = self.selected_piece_on            
            if p_r == r:                
                for x in range(p_c, c):
                    if self.board[r][x] == Cell.BROWN_ANCHOR or self.board[r][x] == Cell.WHITE_ANCHOR or self._cell_free(r, x):                        
                        return False 
                return True
            if p_c == c:
                for x in range(p_r, r):
                    if self.board[x][c] == Cell.BROWN_ANCHOR or self.board[x][c] == Cell.WHITE_ANCHOR or self._cell_free(x, c): 
                        return False                    
                return True
        return False
    def push_at(self, r, c):   
        p_r, p_c = self.selected_piece_on
        if self._cell_free(r, c):            
            s = abs(p_r - r + p_c - c)            
            for i in range(1, s):    
                self.board[r - np.sign(r-p_r)*(i-1)][c - np.sign(c-p_c)*(i-1)] = self.board[r - np.sign(r-p_r)*i][c - np.sign(c-p_c)*i]    
            self.board[p_r][p_c] = Cell.EMPTY
            for a_c in range(Game.BoardWidth):
                for a_r in range(Game.BoardHeight):
                    if self.board[a_r][a_c] == Cell.BROWN_ANCHOR: self.board[a_r][a_c] = Cell.BROWN_SQUARE
                    if self.board[a_r][a_c] == Cell.WHITE_ANCHOR: self.board[a_r][a_c] = Cell.WHITE_SQUARE
            self.board[p_r+ np.sign(r-p_r)][p_c+ np.sign(c-p_c)] = Cell.BROWN_ANCHOR if self.current_team == self.brown_team else Cell.WHITE_ANCHOR
            self.next_player()
        if self._lava_cell(r, c):
            if self.board[r - np.sign(r-p_r)][c - np.sign(c-p_c)] == (Cell.BROWN_SQUARE or Cell.BROWN_ROUND):
                self.current_team = self.brown_team
            else: self.current_team = self.white_team
            self.state = GameState.OVER

    def next_player(self):
        self.state = GameState.MOVE
        self.selected_piece_on = (0,0)
        self.moves = 2
        self.current_team = self.white_team if self.current_team == self.brown_team else self.brown_team
        
    def is_game_over(self):        
        return True if self.state == GameState.OVER else False

    def player_name(self):
        return "BROWN" if Cell.BROWN_ROUND in self.current_team else "WHITE"

    def hint_text(self):
        return self.moves
    
    def _state_is(self):                
        return self.state

    def _selected_is(self):                
        return self.selected_piece_on