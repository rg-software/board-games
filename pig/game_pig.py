import random


class Game:
    def __init__(self):
        self.score = [0, 0]
        self.current_player = 0
        self.table = 0
        self.die = 0

    def _genrand(self):
        return random.randint(1, 6)

    def roll_die(self):
        self.die = self._genrand()
        self.table += self.die

    def pass_turn(self):
        if self.die != 1:
            self.score[self.current_player] += self.table
        self.table = 0
        self.current_player = not self.current_player

    def game_over(self):
        return self.score[0] >= 100 or self.score[1] >= 100
