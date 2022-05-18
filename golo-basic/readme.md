# GOLO (Basic Version)

![GOLO](screenshot.png)

## Rules Summary

- The player's challenge is to obtain the lowest "nine-hole score" in a golf course.

- The game inventory consists of nine 12-sided dice with the following faces:

  - Die #1: 1, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 8.

  - Die #2: 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7.

  - Dice #3 to #7: 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8.

  - Die #8: 3, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 10.

  - Die #9: 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9.

- The game session proceeds as follows:

  - First, a player rolls all nine dice.

  - Next, any number of dice (but at least one) with the lowest scores are removed from the game. _Note: while the "lowest-scores" condition is stated in the rules, it is not necessary to enforce it in practice: any reasonable strategy suggests removing the lowest-scoring dice anyway._

  - The remaining dice are rolled until all of them are removed.

- The sum of all removed dice is the final score.

## Running the Game

Console version:

```shell
poetry run python cli_golo.py
```

GUI version:

```shell
poetry run python gui_golo.py
```
