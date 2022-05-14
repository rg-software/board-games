from game_mastermind import Game


class GameExt(Game):
    def __init__(self, code):
        self._code = code
        super().__init__()

    def _gencode(self):
        return self._code


def test_pegs():
    mmind = GameExt([0, 1, 5, 4])

    c1 = [0, 1, 5, 3]
    assert not mmind.is_correct(c1)
    assert mmind.black_pegs(c1) == 3
    assert mmind.white_pegs(c1) == 0

    c2 = [1, 0, 5, 4]
    assert not mmind.is_correct(c2)
    assert mmind.black_pegs(c2) == 2
    assert mmind.white_pegs(c2) == 2

    c3 = [0, 1, 5, 4]
    assert mmind.is_correct(c3)
