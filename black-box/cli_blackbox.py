from game_blackbox import Game, ExitType


def setup_board():
    board = [[" " for _ in range(10)] for _ in range(10)]
    for r in range(1, 9):
        for c in range(1, 9):
            board[r][c] = "."
    for k in range(1, 9):
        board[k][0] = ">"
        board[k][9] = "<"
        board[0][k] = "v"
        board[9][k] = "^"
    return board


game = Game()
board = setup_board()
orange_counter = 1


def print_board():
    print()
    for r in board:
        print("".join([e for e in r]))


def green_balls():
    balls = []
    for r in range(1, 9):
        for c in range(1, 9):
            balls.append((r, c))
    return balls


def on_buttons():
    return sum([len([e for e in r if e not in " v^<>.o"]) for r in board])


def set_result(r, c, result):
    if result.exit_type == ExitType.HIT:
        board[r][c] = "H"
    elif result.exit_type == ExitType.REFLECT:
        board[r][c] = "R"
    else:
        board[r][c] = str(orange_counter)


def set_second_marker(r, c):
    global orange_counter
    board[r][c] = str(orange_counter)
    orange_counter += 1


print_board()
while (rc := input("(row, col) to push, enter to end: ")) or len(green_balls()) != 4:
    r, c = [int(x) for x in rc.split()]

    if 0 < r < 9 and 0 < c < 9:  # flip a green ball
        if board[r][c] == "o":
            board[r][c] = "."
        elif len(green_balls()) <= 3:
            board[r][c] = "o"
    else:  # trace
        if board[r][c] == ">":
            vr, vc = 0, 1
        elif board[r][c] == "<":
            vr, vc = 0, -1
        elif board[r][c] == "v":
            vr, vc = 1, 0
        else:  # ^
            vr, vc = -1, 0
        result = game.trace(r, c, vr, vc)

        set_result(r, c, result)
        if result.exit_type == ExitType.DETOUR:
            set_second_marker(result.r, result.c)

    print_board()

print(f"Final score: {game.score(green_balls(), on_buttons)}")
print(game.hidden_balls)
