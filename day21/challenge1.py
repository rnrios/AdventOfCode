import numpy as np


class Player:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.points = 0
        self.won = False

    def update_position(self, to_add):
        temp = self.pos + to_add
        self.pos = temp if temp < 11 else (temp % 10)
        if self.pos == 0:
            self.pos = 10
        self.update_points(self.pos)
        self.check_won()

    def update_points(self, to_add):
        self.points += to_add

    def check_won(self):
        if self.points >= 1000:
            self.won = True


def main():
    c = 0
    x = np.arange(1, 101)
    p1 = Player('player1', 2)
    p2 = Player('player2', 10)

    while True:
        points = np.sum(np.roll(x, -c)[:3])
        if c / 3 % 2 == 0:
            p1.update_position(points)
            print(f'P1: {np.roll(x, -c)[:3]} \t {p1.pos} \t {p1.points}')
        else:
            p2.update_position(points)
            print(f'P2: {np.roll(x, -c)[:3]} \t {p2.pos} \t {p2.points}')
        c += 3

        if p1.won or p2.won:
            loser = p1.points if p1.points < p2.points else p2.points
            print(c*loser)
            break


if __name__ == '__main__':
    main()
