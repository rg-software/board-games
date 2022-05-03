import random


class Player:
    def __init__(self):
        self.tokens = Game.TokensCount
        self.deck = []

    def score(self):
        score = 0
        cards = [0] + self.deck + [100]
        m = cards[0]
        for i in range(1, len(cards)):
            if cards[i] != cards[i - 1] + 1:
                score += m
                m = cards[i]
        return score - self.tokens

    def has_tokens(self):
        return self.tokens > 0

    def move_pass(self):
        self.tokens -= 1

    def move_take(self, tokens, card):
        self.tokens += tokens
        self.deck.append(card)
        self.deck.sort()


class Game:
    PlayersCount = 2
    TokensCount = 11

    def __init__(self):
        self.deck = list(range(3, 36))
        random.shuffle(self.deck)
        self.deck = self.deck[9:]
        self.table_tokens = 0
        self.current_player = 0
        self.players = [Player() for _ in range(Game.PlayersCount)]

    def can_pass(self):
        return self.players[self.current_player].has_tokens()

    def move_pass(self):
        self.players[self.current_player].move_pass()
        self.table_tokens += 1
        self.current_player = (self.current_player + 1) % Game.PlayersCount

    def move_take(self):
        self.players[self.current_player].move_take(self.table_tokens, self.deck[0])
        self.table_tokens = 0
        self.deck = self.deck[1:]
