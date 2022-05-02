from game_kalah import Game


def test_basic_move():
    kalah = Game()
    kalah.make_move(1)

    assert kalah.board[1:8] == [0, 5, 5, 5, 5, 4, 0]
    assert kalah.upper_player_move


def test_storage_move():
    kalah = Game()
    kalah.make_move(3)

    assert kalah.board[3:8] == [0, 5, 5, 5, 1]
    assert not kalah.upper_player_move


def test_capture_move():
    kalah = Game()
    kalah.make_move(3)
    kalah.make_move(5)
    kalah.make_move(8)
    kalah.make_move(1)

    assert kalah.board[5] == 0  # self
    assert kalah.board[9] == 0  # opp
    assert kalah.board[7] == 9  # storage


def test_game_over():
    kalah = Game()
    kalah.board = [1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2]

    assert kalah.is_end_game()
    kalah.capture_remaining()
    assert kalah.board[kalah.opp_storage()] == 1 + 2 * 6
