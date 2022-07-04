from game_crisscross import Game, Domino


def test_placement():
    cc = Game()
    cc.roll()

    cc.place(0, 0)
    assert cc.dice  # cannot place

    cc.place(4, 4)
    assert cc.dice  # same here

    cc.place(1, 1)
    assert not cc.dice
    assert cc.card[1][1] != 0


def test_flip():
    dice = Domino(1, 2)
    assert dice.v1 == 1 and dice.v2 == 2 and dice.dir_horiz

    dice.flip()
    assert dice.v1 == 2 and dice.v2 == 1 and not dice.dir_horiz

    dice.flip()
    assert dice.v1 == 2 and dice.v2 == 1 and dice.dir_horiz


def test_scoring():
    cc = Game()
    cc.card = [
        [1, 1, 2, 2, 3],
        [1, 4, 2, 2, 5],
        [5, 4, 6, 6, 5],
        [2, 4, 6, 2, 5],
        [1, 5, 6, 3, 5],
    ]

    assert cc.card_score() == 28
