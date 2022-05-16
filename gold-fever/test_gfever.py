from game_gfever import Game, Player, Stone


class PlayerExt(Player):
    def __init__(self, stones):
        super().__init__()
        self.stones = stones

    def draw_stone(self):
        return self.stones.pop()


class GameExt(Game):
    def __init__(self, player1, player2):
        super().__init__()
        self.players = [player1, player2]


def test_basic_actions():
    p1 = PlayerExt([Stone.GOLD, Stone.BLACK, Stone.WHITE])
    p2 = PlayerExt([])
    game = GameExt(p1, p2)

    assert game.draw_stone() == (Stone.WHITE, True)
    assert game.draw_stone() == (Stone.BLACK, True)
    assert game.draw_stone() == (Stone.GOLD, True)
    assert game.table_stones == [Stone.WHITE, Stone.BLACK, Stone.GOLD]

    game.end_turn()  # swap players
    assert game.opponent().score == 1
    assert game.player().stones == [Stone.WHITE, Stone.BLACK]


def test_second_white():
    p1 = PlayerExt([Stone.WHITE, Stone.BLACK, Stone.WHITE])
    p2 = PlayerExt([])
    game = GameExt(p1, p2)

    assert game.draw_stone() == (Stone.WHITE, True)
    assert game.draw_stone() == (Stone.BLACK, True)
    assert game.draw_stone() == (Stone.WHITE, False)  # swap players
    game.resolve(Stone.WHITE)
    assert game.opponent().stones == [Stone.WHITE, Stone.BLACK, Stone.WHITE]


def test_second_black():
    p1 = PlayerExt([Stone.BLACK, Stone.GRAY, Stone.BLACK])
    p2 = PlayerExt([Stone.GRAY])
    game = GameExt(p1, p2)

    assert game.draw_stone() == (Stone.BLACK, True)
    assert game.draw_stone() == (Stone.GRAY, True)
    assert game.draw_stone() == (Stone.BLACK, False)  # swap players
    game.resolve(Stone.BLACK)
    assert game.player().stones == []  # passed to the opponent
    assert len(game.opponent().stones) == 4
