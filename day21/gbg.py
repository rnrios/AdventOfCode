import itertools as it
import functools

OUTCOMES = tuple(map(sum, it.product([1, 2, 3], repeat=3)))


class Player:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.points = 0
        self.wins = 0

    def update_position(self, to_add):
        temp = self.pos + to_add
        self.pos = temp if temp < 11 else (temp % 10)
        if self.pos == 0:
            self.pos = 10
        self.update_points(self.pos)


    def update_points(self, to_add):
        self.points += to_add


@functools.lru_cache(maxsize=None)
def dirac_dice(p1, p2, p1_turn):
    if p1.points >= 21:
        return 1, 0

    elif p2.points >= 21:
        return 0, 1

    p1_wins = p2_wins = 0
    for outcome in OUTCOMES:
        if p1_turn:
            temp = [p1.pos, p1.points]
            p1.update_position(outcome)
            p1_turn = False
            n, t = dirac_dice(p2, p1, p1_turn)
            p1.pos = temp[0]
            p1.points = temp[1]

        else:
            temp = [p2.pos, p2.points]
            p2.update_position(outcome)
            p1_turn = True
            t, n = dirac_dice(p1, p2, p1_turn)
            p2.pos = temp[0]
            p2.points = temp[1]

        p1_wins += t
        p2_wins += n

    return p1_wins, p2_wins


def main():
    p1 = Player('p1', 2)
    p2 = Player('p2', 10)
    p1_turn = True
    x, y = dirac_dice(p1, p2, p1_turn)
    print(x, y)


if __name__ == '__main__':
    main()
