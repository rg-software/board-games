from game_goloscard import Game


class GameExt(Game):
    def __init__(self, card, rndlist):
        super().__init__(card)
        self._rndlist = rndlist

    def roll(self):
        self.rolled = self._rndlist


def test_can_remove():
    dice = [3, 3, 3, 4, 1, 1, 6, 6, 5]  # par 3, 3, 5, 5, then par 4 x 5
    golo = GameExt([5, 4, 3, 4, 4, 3, 4, 4, 5], dice)

    golo.roll()

    # only the matching par dice can be removed
    assert not golo.can_remove([0])  # par 5 needed
    assert not golo.can_remove([1])
    assert golo.can_remove([2])
    assert golo.can_remove([2, 8])  # can remove par 5 then par 4
    assert golo.can_remove([2, 8, 0])  # can remove par 5 then par 4 then par 3
    assert not golo.can_remove([2, 0])  # but can't skip par 4


def test_score():
    inlist = [3, 3, 3, 4, 1, 1, 6, 6, 5]
    golo = GameExt([5, 4, 3, 4, 4, 3, 4, 4, 5], inlist)

    golo.roll()
    golo.remove([5, 2, 4])

    assert golo.score == inlist[2] + inlist[4] + inlist[5]
    assert len(golo.dice) == 9 - 3
