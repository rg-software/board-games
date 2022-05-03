from game_pokerdice import Player


class TestPlayer(Player):
    def __init__(self, rndlist):
        super().__init__()
        self._rndlist = rndlist

    def _genrand(self):
        return self._rndlist.pop(0)


def test_roll_and_freeze():
    p = TestPlayer([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

    p.roll_dice()
    p.freeze(0)
    p.freeze(2)
    p.freeze(3)
    p.roll_dice()

    assert p.hand == [0, 1, 0, 0, 1]


def test_ranks():
    p = Player()

    p.hand = [1, 1, 1, 1, 1]
    assert p.hand_rank() == 0

    p.hand = [1, 1, 3, 1, 1]
    assert p.hand_rank() == 1

    p.hand = [1, 2, 2, 1, 1]
    assert p.hand_rank() == 2

    p.hand = [1, 2, 3, 1, 1]
    assert p.hand_rank() == 3

    p.hand = [2, 3, 1, 5, 4]
    assert p.hand_rank() == 4

    p.hand = [1, 2, 2, 1, 3]
    assert p.hand_rank() == 5

    p.hand = [1, 2, 2, 3, 4]
    assert p.hand_rank() == 6

    p.hand = [1, 2, 3, 5, 7]
    assert p.hand_rank() == 7


def test_better_than_1():
    p1 = Player()
    p1.hand = [1, 1, 1, 1, 1]

    p2 = Player()
    p2.hand = [1, 2, 1, 1, 1]

    assert p1.hand_better_than(p2)


def test_better_than_2():
    p1 = Player()
    p1.hand = [1, 2, 3, 5, 6]

    p2 = Player()
    p2.hand = [1, 2, 3, 5, 7]

    assert p2.hand_better_than(p1)
