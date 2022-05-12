import pytest
from game_farmers import Game, ActionError


def test_buy_wheat():
    game = Game()
    game.set_market(-2)  # buy bonus
    game.buy_wheat()

    assert game.table_wheat == 3
    assert game.players[0].wheat == 1
    assert game.players[0].money == 6  # purchased for 4 coins

    game.set_market(2)  # buy bonus
    game.buy_wheat()

    assert game.players[0].wheat == 2
    assert game.players[0].money == 5  # purchased for 1 coin


def test_sell_bread():
    game = Game()
    game.set_market(0)  # buy bonus
    game.buy_wheat()

    game.set_market(2)  # buy bonus
    game.make_bread(1)

    assert game.players[0].wheat == 0
    assert game.players[0].bread == 1
    assert game.players[0].money == 8

    game.sell_bread(1)
    assert game.players[0].bread == 0
    assert game.players[0].money == 8 + 7


def test_bad_action():
    game = Game()
    game.set_market(0)

    with pytest.raises(ActionError):
        game.sell_animals(5)  # don't have 5 animals to sell

    game.buy_animals()
    with pytest.raises(ActionError):
        game.buy_animals()  # don't have money
