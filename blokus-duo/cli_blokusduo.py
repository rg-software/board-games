from game_blokusduo import Game, Cell

game = Game()
block_idx = 0


def blockchar(b):
    return "=" if b == Cell.BLOCK_1 else ("#" if b == Cell.BLOCK_2 else ".")


def print_game_board():
    print()
    for r in game.board:
        print("".join([blockchar(b) for b in r]))


def print_block(block):
    size_r = 1 + max([r for (r, _) in block.coord()])
    size_c = 1 + max([c for (_, c) in block.coord()])
    blockboard = [[" " for _ in range(size_c)] for _ in range(size_r)]
    for dr, dc in block.coord():
        blockboard[dr][dc] = "*"

    for r in blockboard:
        print("".join(r))


while not game.is_game_over():
    print_game_board()
    print(f"{game.player_name()} move, current block {block_idx + 1}:")
    block = game.get_block(block_idx)
    print_block(block)

    action = input("(N)ext, (P)revious, (R)otate, (F)lip or place at (r, c): ")
    if action == "n":
        block_idx = game.next_block(block_idx)
    elif action == "p":
        block_idx = game.prev_block(block_idx)
    elif action == "r":
        game.rotate_block(block_idx)
    elif action == "f":
        game.flip_block(block_idx)
    else:
        r, c = [int(x) for x in action.split()]
        if game.can_place_at(r, c, block):
            game.place_at(r, c, block)
            game.next_player()
            block_idx = 0
        else:
            print("Illegal placement!")

print(f"Game over! {game.player_name()} player lost")
