from game_quixo import Game


def test_game_over():
    game = Game()

    assert not game.winner_char()

    for i in range(5):
        game.board[i][0] = "x"

    assert "x" == game.winner_char()
