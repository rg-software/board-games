import pgzrun
from pgzero.builtins import Actor
from game_blackbox import Game, ResultType

WIDTH = 550
HEIGHT = 600
CELL = 40
MARGIN = 50
TITLE = "Black Box"

balls = []
buttons = {}
btn_end = Actor("end", pos=(240, 550))
game = Game()
game_over = False


class Ball(Actor):
    def __init__(self, r, c):
        super().__init__("gray_s", (MARGIN + c * CELL, MARGIN + r * CELL))
        self.r = r
        self.c = c

    def is_on(self):
        return self.image == "green_s"

    def flip(self, can_flip_on):
        if self.image == "green_s":
            self.image = "gray_s"
        elif can_flip_on:
            self.image = "green_s"


class SideButton(Actor):
    orange_counter = 1

    def __init__(self, r, c, vr, vc):
        super().__init__("button", (MARGIN + c * CELL, MARGIN + r * CELL))
        self.r = r
        self.c = c
        self.vr = vr
        self.vc = vc
        self.orange_counter = None

    def is_pressed(self):
        return self.image != "button"

    def set_type(self, result):
        if result.result_type == ResultType.HIT:
            self.image = "button-red"
        elif result.result_type == ResultType.REFLECT:
            self.image = "button-yellow"
        else:
            self.image = "button-orange"
            self.orange_counter = SideButton.orange_counter

    def set_second_marker(self):
        self.image = "button-orange"
        self.orange_counter = SideButton.orange_counter
        SideButton.orange_counter += 1

    def draw(self):
        super().draw()
        if self.orange_counter:
            screen.draw.text(f"{self.orange_counter}", center=self.pos)


for r in range(1, 9):
    for c in range(1, 9):
        balls.append(Ball(r, c))


for r in range(8):
    buttons[(r + 1, 0)] = SideButton(r + 1, 0, 0, 1)
    buttons[(r + 1, 9)] = SideButton(r + 1, 9, 0, -1)

for c in range(8):
    buttons[(0, c + 1)] = SideButton(0, c + 1, 1, 0)
    buttons[(9, c + 1)] = SideButton(9, c + 1, -1, 0)


def widget_clicked(pos, widgets):
    for b in widgets:
        if b.collidepoint(pos):
            return b
    return None


def green_balls():
    return [(b.r, b.c) for b in balls if b.is_on()]


def on_mouse_down(pos):
    global game_over

    if game_over:
        return

    if btn_end.collidepoint(pos) and len(green_balls()) == 4:
        game_over = True

    if b := widget_clicked(pos, balls):
        b.flip(len(green_balls()) <= 3)

    if (btn := widget_clicked(pos, buttons.values())) and not btn.is_pressed():
        result = game.trace(btn.r, btn.c, btn.vr, btn.vc)

        btn.set_type(result)

        if result.result_type == ResultType.DETOUR:
            buttons[(result.r, result.c)].set_second_marker()


def draw():
    screen.fill("white")

    btn_end.draw()
    for b in balls + list(buttons.values()):
        b.draw()

    if game_over:
        on_buttons = [b for b in buttons.values() if b.is_pressed()]
        s = game.score(green_balls(), len(on_buttons))
        for (r, c) in game.hidden_balls:
            pos = (MARGIN + c * CELL, MARGIN + r * CELL)
            screen.draw.text("O", center=pos, color="black")

        screen.draw.text(f"Final score: {s}", pos=(200, 500), color="black")


pgzrun.go()
