import random


class Player:
    def __init__(self):
        self.hand = [0] * 5
        self.to_roll = set({0, 1, 2, 3, 4})
        self.rolls_left = 3

    def _genrand(self):
        return random.randint(0, 5)

    def roll_dice(self):
        for i in self.to_roll:
            self.hand[i] = self._genrand()
        self.rolls_left -= 1

    def freeze(self, dice_idx):
        if dice_idx in self.to_roll:
            self.to_roll.remove(dice_idx)

    def can_roll(self):
        return self.rolls_left > 0

    def hand_better_than(self, other):
        r1 = self.hand_rank()
        r2 = other.hand_rank()

        if r1 == 7 and r2 == 7:  # check busts
            return sorted(self.hand)[4] > sorted(other.hand)[4]

        return r1 < r2

    def hand_rank(self):
        shand = sorted(self.hand)
        counts = [shand.count(i) for i in set(shand)]

        if shand.count(shand[0]) == 5:
            return 0  # all dice are the same
        if shand.count(shand[2]) == 4:
            return 1  # four dice are the same (take middle as a sample)
        if (shand.count(shand[0]), shand.count(shand[4])) in [(2, 3), (3, 2)]:
            return 2  # 3 same values + 2 same values
        if shand.count(shand[2]) == 3:
            return 3  # 3 same values
        if shand == list(range(shand[0], shand[0] + 5)):
            return 4  # five consecutive numbers
        if counts.count(2) == 2:
            return 5  # two pairs
        if 2 in counts:
            return 6  # one pair
        return 7

    def hand_name(self):
        shand = sorted(self.hand)
        names = [
            "Five of a kind",
            "Four of a kind",
            "Full house",
            "Three of a kind",
            "Straight",
            "Two pair",
            "One pair",
            f"Bust ({shand[4]})",
        ]
        return names[self.hand_rank()]


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.current_player_idx = 0

    def current_player(self):
        return self.players[self.current_player_idx]

    def next_player(self):
        self.current_player_idx += 1

    def is_game_over(self):
        return self.current_player_idx >= len(self.players)
