import random
from enum import Enum

Stone = Enum("Stone", ["GOLD", "WHITE", "GRAY", "BLACK"])


class Player:
    def __init__(self):
        self.stones = [Stone.GOLD] * 5 + [Stone.BLACK, Stone.GRAY, Stone.WHITE] * 4
        self.score = 0

    def draw_stone(self):
        random.shuffle(self.stones)
        return self.stones.pop()

    def put_stones(self, stones):
        self.stones.extend(stones)


class Game:
    def __init__(self):
        self.table_stones = []
        self.current_player = 0
        self.players = [Player(), Player()]

    def player(self):
        return self.players[self.current_player]

    def opponent(self):
        return self.players[(self.current_player + 1) % 2]

    def pass_turn(self):
        self.current_player = (self.current_player + 1) % 2

    def resolve(self, stone):
        self.player().put_stones(self.table_stones)  # second stone

        got_from_opp = None
        if stone == Stone.BLACK:
            opp_stone = self.opponent().draw_stone()
            if opp_stone != Stone.GOLD:
                got_from_opp = opp_stone
                self.player().put_stones([opp_stone])
            else:
                self.opponent().put_stones([opp_stone])

        self.table_stones = []
        self.pass_turn()
        return got_from_opp

    def draw_stone(self):
        stone = self.player().draw_stone()
        self.table_stones.append(stone)

        return stone, stone == Stone.GOLD or stone not in self.table_stones[:-1]

    def end_turn(self):
        score = len([s for s in self.table_stones if s == Stone.GOLD])
        gravel = [s for s in self.table_stones if s != Stone.GOLD]

        self.player().score += score
        self.opponent().put_stones(gravel)
        self.table_stones = []
        self.pass_turn()
