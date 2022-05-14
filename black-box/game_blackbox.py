from enum import Enum
import random


class ExitType(Enum):
    NONE = 0
    HIT = 1
    REFLECT = 2
    DETOUR = 3


class TraceResult:
    def __init__(self, rt, r, c):
        self.exit_type = rt
        self.r = r
        self.c = c


class Game:
    def __init__(self):
        self.board = [[False for _ in range(10)] for _ in range(10)]
        self.hidden_balls = self._generate_balls()

        for (r, c) in self.hidden_balls:
            self.board[r][c] = True

    def _generate_balls(self):
        result = []
        while len(result) < 4:
            r = random.randint(1, 8)
            c = random.randint(1, 8)
            if (r, c) not in result:
                result.append((r, c))
        return result

    def _get_speeds(self, r, c, vr, vc):
        if self.board[r + vr][c + vc]:
            return 0, 0

        dc = int(vr != 0)
        dr = int(vc != 0)

        c1 = self.board[r + vr + dr][c + vc + dc]
        c2 = self.board[r + vr - dr][c + vc - dc]

        if c1 and c2:
            return -vr, -vc
        elif c1:
            return -dr, -dc
        elif c2:
            return dr, dc
        return vr, vc

    def trace(self, r, c, vr, vc):
        start_r, start_c = r, c

        do_loop = True
        entered_box = False
        while do_loop:
            vr, vc = self._get_speeds(r, c, vr, vc)
            r += vr
            c += vc
            in_box = 0 < r < 9 and 0 < c < 9
            entered_box = entered_box or in_box
            do_loop = in_box and (vr, vc) != (0, 0)

        result = TraceResult(ExitType.DETOUR, r, c)

        if in_box:
            result.exit_type = ExitType.HIT
        if (start_r, start_c) == (r, c):
            result.exit_type = ExitType.REFLECT if entered_box else ExitType.HIT
        elif not entered_box:
            result.exit_type = ExitType.REFLECT

        return result

    def score(self, balls, on_buttons_count):
        ball_score = 5 * (4 - len(set(balls) & set(self.hidden_balls)))
        return ball_score + on_buttons_count
