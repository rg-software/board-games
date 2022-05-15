from game_kvalley import Game, Pieces, Player


def test_basic_movements():
    game = Game()

    assert game.move(4, 0, "N")

    assert game.board[4][0] == Pieces.EMPTY
    assert game.board[1][0] == Pieces.W_PAWN

    assert not game.move(4, 0, "N")
    assert not game.move(0, 0, "SE")  # wrong player

    game.pass_turn()
    assert game.move(0, 0, "SE")
    assert game.board[3][3] == Pieces.B_PAWN


def test_captured():
    game = Game()
    game.board[1][1] = Pieces.W_PAWN
    game.board[1][2] = Pieces.W_PAWN
    game.board[1][3] = Pieces.W_PAWN

    assert game.winner() == Player.BLACK


def test_center():
    game = Game()
    game.board[0][2] = Pieces.W_PAWN
    game.board[2][2] = Pieces.W_KING

    assert game.winner() == Player.WHITE
