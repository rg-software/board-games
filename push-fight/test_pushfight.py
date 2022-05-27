from game_pushfight import Game, GameState


class GameExt(Game):
    def __init__(self):
        super().__init__()  # use the same initial setup
        # white team
        self.place_new_piece(0, 5)
        self.place_new_piece(1, 5)
        self.place_new_piece(2, 5)
        self.place_new_piece(3, 5)
        self.place_new_piece(3, 6)

        # brown team
        self.place_new_piece(0, 4)
        self.place_new_piece(1, 4)
        self.place_new_piece(2, 4)
        self.place_new_piece(3, 4)
        self.place_new_piece(3, 3)


def test_basic_gameplay():
    game = GameExt()
    assert not game.current_team_brown and game.moves_left() == 2

    game.select_piece(3, 6)
    assert not game.can_move_at(3, 7)
    assert game.can_move_at(0, 7)
    game.move_at(0, 7)

    game.select_piece(3, 5)
    game.move_at(0, 6)

    assert game.game_state() == GameState.PUSH
    game.select_piece(2, 5)
    game.push_at(2, 4, game.can_push_pieces(2, 4))

    game.move_done(game.moves_left())
    game.select_piece(0, 4)
    game.push_at(0, 5, game.can_push_pieces(0, 5))
    assert game.game_state() == GameState.OVER
    assert not game.current_team_brown  # white team lost
