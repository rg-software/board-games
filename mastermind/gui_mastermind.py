import pgzrun
from game_mastermind import Game

WIDTH = 400
HEIGHT = 750
TITLE = "Mastermind"

MAX_TURNS = 12
MARGIN = 40
STEP = 50
R = 20
INPUT_Y = 700
COLORS = ["blue", "cyan", "gray", "green", "red", "gold"]

game = Game()


class Attempt:
    def __init__(self):
        self.code = []

    def _draw_pegs(self, pos):
        p_colors = ["black"] * game.black_pegs(self.code)
        p_colors += ["gray"] * game.white_pegs(self.code)
        x, y = pos
        p = [(x, y), (x + 20, y), (x, y + 20), (x + 20, y + 20)]
        for i, color in enumerate(p_colors):
            screen.draw.filled_circle(p[i], 8, color=color)

    def draw(self, pos):
        for i, c in enumerate(self.code):
            p = (pos[0] + STEP * i, pos[1])
            screen.draw.filled_circle(p, R, color=COLORS[c])
            if len(self.code) == 4:
                self._draw_pegs((350, pos[1]))

    def is_correct(self):
        return game.is_correct(self.code)

    def try_add_peg(self, color_idx):
        if color_idx not in self.code:
            self.code.append(color_idx)
        return len(self.code) == 4  # returns if complete


class History:
    def __init__(self):
        self.game_over = False
        self.attempts = [Attempt()]

    def _add_attempt(self):
        if len(self.attempts) == MAX_TURNS or self.is_correct():
            self.game_over = True
        else:
            self.attempts.append(Attempt())

    def is_correct(self):
        return self.attempts[-1].is_correct()

    def add_code_peg(self, color_idx):
        if self.attempts[-1].try_add_peg(color_idx):
            self._add_attempt()


history = History()


def draw():
    screen.fill("white")

    for i, v in enumerate(history.attempts):
        screen.draw.text(f"#{i + 1}", (MARGIN, MARGIN + STEP * i), color="black")
        v.draw((MARGIN + 50, MARGIN + STEP * i))

    for i, c in enumerate(COLORS):
        screen.draw.filled_circle((MARGIN + STEP * i, INPUT_Y), R, color=c)

    if history.game_over:
        pref = "Correct! " if history.is_correct() else ""
        screen.draw.text(f"{pref}Game over.", (MARGIN, INPUT_Y - 50), color="black")


def on_mouse_down(pos):
    y_ok = INPUT_Y - R < pos[1] < INPUT_Y + R
    color_idx = (pos[0] + MARGIN - R) // STEP - 1
    coord_ok = y_ok and color_idx in range(6)
    if coord_ok and not history.game_over:
        history.add_code_peg(color_idx)


pgzrun.go()
