# Blokus Duo

![blokus-duo](screenshot.png)

## Rules Summary

- The game is played on a 14 &times; 14 board with two identical sets of 21 pieces.

![game pieces](pieces.png)

- Each of two players receives his own set of pieces (white or black).

- Players take turns placing their pieces until neither of the players can make the next move. When a player cannot make a move, he skips his turn. When the opponent cannot make his move either, the game is over.

- During the first turn, the white player must place a piece so it overlaps a starting position at row 5, column 5. Likewise, the black player must start at row 10, column 10. During placement, a piece can be flipped and rotated.

- During subsequent turns, players place pieces making sure that:

  - a newly placed piece occupies empty board cells only;

  - at least one corner of a newly placed piece touches a corner of another piece of the same color;

  - no pieces of the same color occupy adjacent cells, sharing an edge. Touching opponent's pieces is allowed.

- After the end of the game, players count the number of unit squares in the remaining (non-placed) pieces to obtain the final score. Each square yields a -1 score point. A player earns +15 bonus points if all 21 of his pieces are placed, and an additional +5 bonus points if the smallest one-square piece was placed last.

Note: this is a dedicated two-player version of [Blokus](https://boardgamegeek.com/boardgame/2453/blokus).

## Running the Game

Console version:

```shell
poetry run python cli_blokusduo.py
```

GUI version:

```shell
poetry run python gui_blokusduo.py
```
