import itertools as it
import numpy as np
from collections import defaultdict


def reboot_steps(f):
    cuboids = defaultdict(int)
    for string in f:
        msg = string.split(' ')[0]
        action = 0 if msg == 'off' else 1
        x = [int(x) for x in string.split('=')[1][:-2].split('..')]
        y = [int(x) for x in string.split('=')[2][:-2].split('..')]
        z = [int(x) for x in string.split('=')[3].split('..')]
        if any([x[0] < -50, y[0] < -50, z[0] < -50, x[1] > 50, y[1] > 50, z[1] > 50]):
            continue

        cuboid = it.product(np.arange(x[0], x[1] + 1), np.arange(y[0], y[1] + 1), np.arange(z[0], z[1] + 1))
        for cube in cuboid:
            cuboids[cube] = action

    return cuboids


def main():
    f = open('input.txt', 'r').read().splitlines()
    print(sum(reboot_steps(f).values()))


if __name__ == '__main__':
    main()
