from game_impact import Game


class GameExt(Game):
    def __init__(self, rndlist):
        super().__init__()
        self.arena = [2]
        self._rndlist = rndlist

    def _genrand(self):
        return self._rndlist.pop(0)


def test_gameplay():
    game = GameExt([3, 2, 1, 3])
    assert not game.roll()  # no pairs
    assert game.roll()  # pair 2-2
    assert game.arena == [3]
    assert game.dice == [8, 8]
    game.pass_turn()
    assert not game.roll()
    assert game.arena == [3]  # rolled 1 is removed


def test_empty_arena():
    game = GameExt([2, 3, 3, 3, 4, 4, 1, 5, 1])
    assert game.roll()  # pair 2-2
    assert not game.arena  # empty
    game.pass_turn()
    assert game.roll()  # rolling all the dice, pairs 3-3-3, 4-4
    assert game.dice == [9, 5]
    assert game.arena == [5]
