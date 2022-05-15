# Simple Board Games

This is a collection of simple board games implemented in Python with [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/). These games are selected as possible exercises for entry-level programming courses. More details about the criteria for inclusion and other considerations can be found in [this paper].

The code provided is supposed to be simple and straightforward, resembling a "good enough" exercise solution: there are neither strong fool-proof mechanisms, nor polished GUIs. The main purpose of these examples is to demonstrate the complexity of a particular game from the software developer's perspective.

Each game comes with a text interface, a graphical interface, and a small number of [pytest](https://pytest.org/)-powered unit tests.

## Setup

Install [Poetry](https://python-poetry.org), then run

```shell
poetry install
```

to install dependencies. Check the pages of individual games for more information.

## Current Games

<!--GAMES_TABLE-->
|Name|BGG Rating|Core LOC|GUI value|Players|Category|Topics|
|---|---|---|---|---|---|---|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/161130/pig)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Pig_(dice_game))&nbsp;[Pig](/pig/readme.md)|5.3|25|Low|2|Dice|Basics|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/2448/kalah)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Kalah)&nbsp;[Kalah](/kalah/readme.md)|5.9|50|Low|2|Abstract|Arrays|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/10502/poker-dice)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Poker_dice)&nbsp;[Poker dice](/poker-dice/readme.md)|5.1|100|Low|2+|Dice|Arrays, Algorithms|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/7450/stop-gate)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Domineering)&nbsp;[Stop-Gate](/stop-gate/readme.md)|6.1|50|High|2|Abstract|2D Arrays|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/12942/no-thanks)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/No_Thanks!_(game))&nbsp;[No Thanks!](/no-thanks/readme.md)|7.1|50|Low|3-7|Cards|Arrays, Algorithms|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/2389/othello)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Reversi)&nbsp;[Othello](/othello/readme.md)|6.1|50|High|2|Abstract|2D Arrays, Algorithms+|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/101463/paletto)[<img src=https://upload.wikimedia.org/wikipedia/commons/7/74/Internet-web-browser.svg width=20>](https://spielstein.com/games/paletto/rules)&nbsp;[Paletto](/paletto/readme.md)|6.7|100|High|2-3|Abstract|Graphs, Algorithms+|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/246228/impact-battle-elements)[<img src=https://upload.wikimedia.org/wikipedia/commons/7/74/Internet-web-browser.svg width=20>](https://whatsericplaying.com/2018/12/24/impact-battle-of-elements/)&nbsp;[Impact](/impact/readme.md)|6.7|50|Low|2-5|Dice|Arrays, Algorithms|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/201028/farmers-finances)[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/thread/1525550/farmers-finances-2016-9-card-nanogame-contest)&nbsp;[Farmers Finances](/farmers/readme.md)|6.3|150|Low|2|Economic|Basics|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/245487/orchard-9-card-solitaire-game)[<img src=https://upload.wikimedia.org/wikipedia/commons/7/74/Internet-web-browser.svg width=20>](https://www.sideroomgames.com/product/orchard/)&nbsp;[Orchard](/orchard/readme.md)|7.4|150|High|1|Cards|2D Arrays, Algorithms+|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/165/black-box)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Black_Box_(game))&nbsp;[Black Box](/black-box/readme.md)|6.4|100|Low|1-2|Deduction|2D Arrays, Algorithms+|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/220988/criss-cross)[<img src=https://upload.wikimedia.org/wikipedia/commons/7/74/Internet-web-browser.svg width=20>](https://www.thefamilygamers.com/criss-cross/)&nbsp;[Criss Cross](/criss-cross/readme.md)|6.4|TBD|Low|1-6|Dice||
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/2392/mastermind)[<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>](https://en.wikipedia.org/wiki/Mastermind_(board_game))&nbsp;[Mastermind](/mastermind/readme.md)|5.6|25|Low|1-2|Deduction|Basics, Arrays|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/86169/kings-valley)[<img src=https://upload.wikimedia.org/wikipedia/commons/7/74/Internet-web-browser.svg width=20>](http://www.logygames.com/english/kingsvalley.html)&nbsp;[King's valley](/kings-valley/readme.md)|6.5|100|Low|2|Abstract|2D Arrays, Algorithms|
|[<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>](https://boardgamegeek.com/boardgame/3190/quixo)[<img src=https://upload.wikimedia.org/wikipedia/commons/7/74/Internet-web-browser.svg width=20>]()&nbsp;[Quixo](//readme.md)||TBD|||||

<!--GAMES_TABLE_END-->

## Third-party Contributions

[DejaVu fonts](https://dejavu-fonts.github.io), [Noto emoji fonts](https://github.com/googlefonts/noto-emoji), [Playing cards](https://en.wikipedia.org/wiki/Standard_52-card_deck).
