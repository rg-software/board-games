from game_blackbox import Game, ExitType


class GameExt(Game):
    def __init__(self, coordlist):
        self._balls = coordlist
        super().__init__()

    def _generate_balls(self):
        return self._balls


def test_basic_trajectories():
    game = GameExt([(4, 3), (1, 5), (4, 5), (8, 8)])

    assert game.trace(1, 0, 0, 1).exit_type == ExitType.HIT
    assert game.trace(0, 5, 1, 0).exit_type == ExitType.HIT

    assert game.trace(0, 6, 0, 1).exit_type == ExitType.REFLECT
    assert game.trace(9, 4, -1, 0).exit_type == ExitType.REFLECT
    assert game.trace(2, 0, 1, 0).exit_type == ExitType.REFLECT

    r1 = game.trace(2, 9, 0, -1)
    assert r1.exit_type == ExitType.DETOUR and (r1.r, r1.c) == (3, 9)

    r2 = game.trace(6, 0, 0, 1)
    assert r1.exit_type == ExitType.DETOUR and (r2.r, r2.c) == (6, 9)

    r3 = game.trace(5, 0, 0, 1)
    assert r3.exit_type == ExitType.DETOUR and (r3.r, r3.c) == (9, 2)
