import itertools as it
import numpy as np
from collections import defaultdict
from collections import Counter


def parse_instructions(f):
    instructions = []
    for string in f:
        msg = string.split(' ')[0]
        action = 0 if msg == 'off' else 1
        x = tuple([int(x) for x in string.split('=')[1][:-2].split('..')])
        y = tuple([int(x) for x in string.split('=')[2][:-2].split('..')])
        z = tuple([int(x) for x in string.split('=')[3].split('..')])
        instructions.append((action, (x, y, z)))
    return instructions


def check_intersection(coord, key):
    new_cube = []
    for coord_ax, key_ax in zip(coord, key):
        if max(coord_ax[0], key_ax[0]) <= min(coord_ax[1], key_ax[1]):
            new_cube.append((max(coord_ax[0], key_ax[0]), min(coord_ax[1], key_ax[1])))
        else:
            return None
    return tuple(new_cube)


def product(cuboids):
    total = 0
    for key, val in cuboids.items():
        total += val*(key[0][1] - key[0][0]+1)*(key[1][1] - key[1][0]+1)*(key[2][1] - key[2][0]+1)
    return total


def main():
    f = open('input.txt', 'r').read().splitlines()
    instructions = parse_instructions(f)
    on_cuboids = defaultdict(int)
    off_cuboids = Counter()
    for on, cuboid in instructions:
        temp_off_cuboids = defaultdict(int)
        for other_cuboid in on_cuboids.keys():
            new_cuboid = check_intersection(cuboid, other_cuboid)
            if new_cuboid is None:
                continue
            temp_off_cuboids[new_cuboid] += on_cuboids[other_cuboid]

        for other_cuboid in off_cuboids.keys():
            new_cuboid = check_intersection(cuboid, other_cuboid)
            if new_cuboid is None:
                continue
            on_cuboids[new_cuboid] += off_cuboids[other_cuboid]
        # Update 'off' cuboids after handling double counts
        off_cuboids.update(temp_off_cuboids)
        if on:
            on_cuboids[cuboid] += 1

if __name__ == '__main__':
    main()