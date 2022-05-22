from game_blokusduo import Game, Block, SHAPES


def test_game_start():
    game = Game()
    assert not game.can_place_at(0, 0, game.get_block(0))
    assert game.can_place_at(4, 4, game.get_block(0))


def test_flip():
    block = Block(list(SHAPES[6]))  # L-shaped
    block.flip()
    assert block.coords() == [(1, 0), (1, 1), (1, 2), (0, 2)]


def test_rotate():
    block = Block(list(SHAPES[6]))  # L-shaped
    block.rotate()
    assert block.coords() == [(0, 1), (1, 1), (2, 1), (2, 0)]


def test_canplace():
    game = Game()

    assert game.can_place_at(4, 2, game.get_block(2))
    game.place_at(4, 2, game.get_block(2))

    assert not game.can_place_at(0, 13, game.get_block(4))
    assert not game.can_place_at(4, 2, game.get_block(4))
    assert game.can_place_at(2, 4, game.get_block(4))
