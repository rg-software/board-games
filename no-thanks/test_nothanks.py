from game_nothanks import Game


def test_gameplay():
    game = Game()

    game.move_take()
    game.move_take()
    game.move_pass()
    game.move_pass()
    game.move_pass()
    game.move_take()

    assert len(game.players[0].deck) == 2
    assert game.players[0].tokens == 11 - 2

    assert len(game.players[1].deck) == 1
    assert game.players[1].tokens == 11 - 1 + 3


def test_scoring():
    player = Game().players[0]

    player.tokens = 1
    player.deck = [3, 5, 6, 7, 8, 12]
    assert player.score() == 3 + 5 + 12 - 1
