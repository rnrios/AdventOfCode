import re
import numpy as np


def get_pile_count(arr, max_x, thresh=False):
    if thresh:
        max_x += 2
        arr[max_x + 2, :] = 1
    sx, sy = 0, 500
    c = 0
    marked = True

    while marked:
        rolling = True
        while rolling:
            if arr[sx + 1, sy] == 0:
                sx = sx + 1
            elif arr[sx + 1, sy - 1] == 0:
                sx, sy = sx + 1, sy - 1
            elif arr[sx + 1, sy + 1] == 0:
                sx, sy = sx + 1, sy + 1
            else:
                c += 1
                if (sx, sy) == (0, 500):
                    marked = False
                    break
                arr[sx, sy] = 2
                sx, sy = 0, 500
                rolling = False
            if sx > max_x:
                marked = False
                break
    return c

X = np.zeros((1000, 1000))
max_x = 0
for line in open('input.txt').readlines():
    moves = [int(x) for x in re.findall(r'\d+', line)]
    y, x = moves[::2], moves[1::2]
    for i, (xx, yy) in enumerate(zip(x[:-1], y[:-1])):
        max_x = xx if xx > max_x else max_x
        X[min(xx, x[i + 1]):max(xx, x[i + 1]) + 1, min(yy, y[i + 1]):max(yy, y[i + 1]) + 1] = 1
print(f'Part 1: {get_pile_count(X.copy(), max_x)}')
print(f'Part 2: {get_pile_count(X.copy(), max_x, True)}')
