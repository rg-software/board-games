# Simple Board Games

This is a collection of simple board games implemented in Python with [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/). These games are selected as possible exercises for entry-level programming courses. More details about the criteria for inclusion and other considerations can be found in [this paper].

The code provided is supposed to be simple and straightforward, resembling a reasonable exercise solution: there are neither strong fool-proof mechanisms, nor polished GUIs. The main purpose of these examples is to demonstrate the complexity of a particular game from the software developer's perspective.

Each game comes with a text interface, a graphical interface, and a small number of [pytest](https://pytest.org/)-powered unit tests.

## Setup

Install [Poetry](https://python-poetry.org), then run

```shell
poetry install
```

to install dependencies. Check the pages of individual games for more information.

## Current Games

<!--GAMES_TABLE-->
|Name|BGG Rating|Core LOC|GUI value|Players|Category|CS topics|
|---|---|---|---|---|---|---|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/161130/pig)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Pig_(dice_game))&nbsp;[Pig](/pig/readme.md)|5.3|25|Low|2|Dice|basic structures|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/2448/kalah)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Kalah)&nbsp;[Kalah](/kalah/readme.md)|5.9|50|Low|2|Strategy|arrays|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/10502/poker-dice)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Poker_dice)&nbsp;[Poker dice](/poker-dice/readme.md)|5.1|100|Low|2+|Dice|arrays, algorithms|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/7450/stop-gate)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Domineering)&nbsp;[Stop-Gate](/stop-gate/readme.md)|6.1|50|High|2|Strategy|2d arrays|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/12942/no-thanks)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/No_Thanks!_(game))&nbsp;[No Thanks!](/no-thanks/readme.md)|7.1|50|High|3-7|Cards|arrays, algorithms|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/2389/othello)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Reversi)&nbsp;[Othello](/othello/readme.md)|6.1|50|High|2|Strategy|2d arrays|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/101463/paletto)[<img src=https://upload.wikimedia.org/wikipedia/commons/7/74/Internet-web-browser.svg width=20>](https://spielstein.com/games/paletto/rules)&nbsp;[Paletto](/paletto/readme.md)|6.7|100|High|2-3|Strategy|graphs|

<!--GAMES_TABLE_END-->

## Third-party Contributions

Deja vu font, noto emoji, Wikipedia cards