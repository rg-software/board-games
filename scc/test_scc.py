from game_scc import Game


class GameExt(Game):
    def __init__(self, rndlist):
        super().__init__()
        self._rndlist = rndlist

    def _rand(self):
        return self._rndlist.pop(0)


def test_sequential_obtain():
    scc = GameExt([1, 1, 1, 1, 1, 2, 6, 2, 2, 2, 3, 5, 3, 3, 5, 5, 4])

    scc.roll_dice(False, False)
    assert scc.dice == [1, 1, 1, 1, 1]

    scc.roll_dice(False, False)
    assert scc.dice == [6, 2, 2, 2, 2]

    scc.roll_dice(False, False)
    assert scc.dice == [6, 5, 3, 3, 3]

    scc.roll_dice(False, False)
    assert scc.dice == [6, 5, 4, 5, 5]


def test_quick_obtain():
    scc = GameExt([1, 6, 5, 4, 1, 2, 2])

    scc.roll_dice(False, False)
    assert scc.dice == [6, 5, 4, 1, 1]

    scc.roll_dice(False, False)
    assert scc.dice == [6, 5, 4, 2, 2]


def test_roll_with_hold():
    scc = GameExt([6, 6, 5, 4, 1, 4])

    scc.roll_dice(False, False)
    assert scc.dice == [6, 5, 4, 6, 1]
    assert scc.hold_idx() == 3
    scc.roll_dice(True, False)
    assert scc.dice == [6, 5, 4, 6, 4]

    scc = GameExt([6, 6, 5, 4, 1, 4])

    scc.roll_dice(False, False)
    assert scc.dice == [6, 5, 4, 6, 1]
    assert scc.hold_idx() == 3
    scc.roll_dice(False, True)
    assert scc.dice == [6, 5, 4, 1, 4]
