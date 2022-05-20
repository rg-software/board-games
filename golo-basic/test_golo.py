from game_golo import Game


class GameExt(Game):
    def __init__(self, rndlist):
        super().__init__()
        self._rndlist = rndlist

    def roll(self):
        self.rolled = self._rndlist


def test_can_remove():
    golo = GameExt([3, 3, 3, 4, 1, 1, 6, 6, 5])

    golo.roll()
    assert not golo.can_remove([0])  # only the lowest scores can be removed
    assert not golo.can_remove([0, 1])
    assert golo.can_remove([4])
    assert golo.can_remove([5, 4])
    assert golo.can_remove([5, 2, 4])


def test_score():
    inlist = [3, 3, 3, 4, 1, 1, 6, 6, 5]
    golo = GameExt(inlist)

    golo.roll()
    golo.remove([5, 2, 4])

    assert golo.score == inlist[2] + inlist[4] + inlist[5]
    assert len(golo.dice) == 9 - 3
