from game_pushfight import Game, Cell


def test_placement():
    game = Game()
    game.place_at(0, 0)

    assert game.board[0][0] == Cell.WHITE_SQUARE
    assert game.board[0][1] == Cell.EMPTY


def test_canplace():
    game = Game()

    assert game.can_move_at(0, 0)
    game.move_at(0, 0)
    assert not game.can_move_at(0, 0)


def test_player_swap():
    game = Game()
    game.move_at(1, 0)
    assert game.can_move_at(0, 0)  
