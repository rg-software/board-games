from game_paletto import Game


def test_board_generator():
    game = Game()
    sums = [0] * 6

    for r in range(1, 7):
        for c in range(1, 7):
            v = game.board.data[r][c]
            sums[v - 1] += 1
            assert v != game.board.data[r - 1][c]
            assert v != game.board.data[r + 1][c]
            assert v != game.board.data[r][c - 1]
            assert v != game.board.data[r][c + 1]

    assert sums == [6] * 6


def test_can_remove_at():
    game = Game()
    game.board.data = [
        [0] * 8,
        [0, 1, 2, 0, 0, 0, 0, 0],
        [0, 1, 2, 0, 0, 0, 0, 0],
        [0, 3, 2, 1, 1, 1, 0, 0],
        [0] * 8,
        [0] * 8,
        [0] * 8,
        [0] * 8,
    ]

    assert game.can_remove_at(1, 1)  # corner piece
    assert not game.can_remove_at(2, 1)  # non-corner piece

    game.remove_at(1, 1)
    assert game.can_remove_at(2, 1)  # it is corner now
    assert not game.can_remove_at(3, 1)  # corner, but wrong color

    assert game.can_remove_at(3, 5)  # it is corner now
    assert not game.can_remove_at(3, 4)  # will break connectivity
