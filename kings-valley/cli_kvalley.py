from game_kvalley import Game, Player, Pieces

game = Game()


def print_board():
    pieces = {
        Pieces.B_KING: "X",
        Pieces.B_PAWN: "x",
        Pieces.W_KING: "O",
        Pieces.W_PAWN: "o",
        Pieces.EMPTY: ".",
    }
    for r in game.board:
        print("".join([pieces[piece] for piece in r]))


def player_name(p):
    return "White" if p == Player.WHITE else "Black"


while game.winner() == Player.NONE:
    print()
    print_board()
    print(f"Current player: {player_name(game.player)}")
    v = input("Move (row, col, compass direction): ").split()
    r, c, dir = int(v[0]), int(v[1]), v[2].upper()
    if game.move(r, c, dir):
        game.pass_turn()
    else:
        print("Illegal move!")

print(f"Winner: {player_name(game.winner())}")
