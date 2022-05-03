from game_stopgate import Game, Cell


def test_placement():
    game = Game()
    game.place_at(0, 0)

    assert game.board[0][0] == Cell.HORIZ
    assert game.board[0][1] == Cell.FULL


def test_canplace():
    game = Game()

    assert game.can_place_at(0, 0)
    game.place_at(0, 0)
    assert not game.can_place_at(0, 0)


def test_player_swap():
    game = Game()
    game.place_at(1, 0)
    assert game.can_place_at(0, 0)  # horizontal still can
    game.next_player()
    assert not game.can_place_at(0, 0)  # vertical cannot
    game.place_at(2, 0)
    assert game.board[2][0] == Cell.VERT
