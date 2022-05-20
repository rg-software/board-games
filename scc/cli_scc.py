from game_scc import Game

scc = Game()

while not scc.game_over():
    for roll in range(1, 4):
        print()
        print(f"round: {scc.turn // 2 + 1}, score: {scc.score}")
        print(f"current player: {scc.current_player + 1}, roll: {roll}")

        hold3 = hold4 = False
        if scc.hold_idx() == 3:
            indices = input("hold dice (3, 4): ")
            hold3 = "3" in indices
            hold4 = "4" in indices

        scc.roll_dice(hold3, hold4)

        print(f"dice: {scc.dice}")

    scc.end_turn()

print(f"final score: {scc.score}")
