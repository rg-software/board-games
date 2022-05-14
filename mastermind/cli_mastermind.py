from game_mastermind import Game

MAX_TURNS = 12

game = Game()
is_correct = False
turn = 1

while not is_correct and turn <= MAX_TURNS:
    print(f"Turn = {turn} of {MAX_TURNS}")
    turn += 1
    s = input("Your guess (4 digits, 0-5): ")
    code = [int(d) for d in s]
    print(f"white pegs = {game.white_pegs(code)}")
    print(f"black pegs = {game.black_pegs(code)}")
    if is_correct := game.is_correct(code):
        print("Correct!")

print("Game over.")
