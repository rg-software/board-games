from game_othello import Game


def test_gameplay():
    game = Game()
    game.board[0] = [True, False, False, False, False, False, False, None]

    assert game.move_allowed(0, 7)
    assert game._reverse_dirs(0, 7) == [(0, -1, 6)]
    assert not game.move_allowed(6, 6)
