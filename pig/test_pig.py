from game_pig import Game


class TestGame(Game):
    def __init__(self, rndlist):
        super().__init__()
        self._rndlist = rndlist

    def _genrand(self):
        return self._rndlist.pop(0)


def test_accumulate_ok():
    pig = TestGame([3, 6, 2, 1])

    pig.roll_dice()
    pig.roll_dice()
    pig.roll_dice()
    assert pig.table == 3 + 6 + 2

    pig.pass_turn()

    assert pig.table == 0
    assert pig.current_player == 1
    assert pig.score == [3 + 6 + 2, 0]


def test_accumulate_then_fail():
    pig = TestGame([3, 6, 2, 1])

    pig.roll_dice()
    pig.roll_dice()
    pig.roll_dice()
    pig.roll_dice()
    pig.pass_turn()

    assert pig.table == 0
    assert pig.current_player == 1
    assert pig.score == [0, 0]


def test_game_over():
    pig = TestGame([5] * 20)

    for _ in range(20):
        pig.roll_dice()

    pig.pass_turn()
    assert pig.game_over()
