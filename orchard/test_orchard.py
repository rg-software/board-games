from game_orchard import Game, Stack, DiceBox, DECK


def test_rotate_card():
    game = Game()
    game.hand[0] = [[1, 2], [2, 1], [3, 3]]

    game.rotate_card()  # rotates left
    assert game.hand[0] == [[2, 1, 3], [1, 2, 3]]

    game.rotate_card()
    assert game.hand[0] == [[3, 3], [1, 2], [2, 1]]


def test_stack_ops_1():
    db = DiceBox()
    s = Stack(db)
    assert s.score() == 0

    s.add(1)
    assert s.score() == 0

    s.add(1)
    assert s.score() == 1

    s.add(1)
    assert s.score() == 3

    s.add(1)
    assert s.score() == 6

    s.add(1)
    assert s.score() == 10

    s.add(2)  # rotten
    assert s.score() == -3


def test_stack_ops_2():
    db = DiceBox()
    db.dice[1] = 0  # don't have "1" dice anymore
    s = Stack(db)

    s.add(1)
    s.add(1)
    s.add(1)

    assert s.score() == 0


def test_stack_ops_3():
    db = DiceBox()
    db.dice[1] = 1  # one "1" die
    s1 = Stack(db)
    s2 = Stack(db)

    s1.add(1)
    s1.add(1)  # used this die
    assert s1.score() == 1

    s2.add(1)
    s2.add(1)
    assert s2.score() == 0

    s1.add(2)
    assert s1.score() == -3  # now rotten

    s2.add(1)  # now has a die to place here
    assert s2.score() == 1  # large pile, but the die has been just placed


def test_canplace():
    game = Game()

    game.board = [game._empty_line() for _ in range(Game.BOARDSIZE)]  # make empty
    game.hand = [DECK[0], DECK[1]]
    game.place_card((2, 2))

    assert not game.can_place((10, 10))  # far away
    assert not game.can_place((2, 2))  # too many rotten
    assert game.can_place((4, 2))  # 2 rotten

    game.dicebox.dice[0] = 1  # just one rotten die
    assert not game.can_place((4, 2))  # cannot place anymore
