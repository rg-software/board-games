from game_quixo import Game


def test_not_game_over():
    game = Game()
    assert not game.winner_char()

    game.board[0][0] = "x"
    game.board[0][1] = "x"
    assert not game.winner_char()


def test_game_over():
    game = Game()

    for i in range(5):
        game.board[i][0] = "x"

    assert "x" == game.winner_char()

    for i in range(5):
        game.board[i][i] = "o"

    assert "o" == game.winner_char()


def test_push_allowed():
    game = Game()
    game.board[0][0] = "x"

    assert not game.push(0, 4, "t")
    assert not game.push(3, 3, "t")
    assert game.player_char == "o"  # start with 'o'
    assert not game.push(0, 0, "b")
    assert game.push(0, 1, "b")


def test_push():
    game = Game()
    for i in range(4):
        game.board[i][0] = "o"

    assert game.player_char == "o"  # start with 'o'
    assert game.push(4, 0, "t")
    assert game.winner_char() == "o"
