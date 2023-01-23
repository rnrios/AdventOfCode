import numpy as np


def get_score(val, arr):
    num = 0
    for x in arr:
        num += 1
        if val <= x:
            return num
    return num


for i, line in enumerate(open('input.txt').readlines()):
    if i == 0:
        trees = np.empty((0, len(line) - 1), int)
    trees = np.append(trees, np.array([[int(x) for x in line[:-1]]]), axis=0)

M, N, visible = trees.shape[0], trees.shape[1], 0
max_score = 0
for i in range(1, M - 1):
    for j in range(1, N - 1):
        if any([trees[i, j] > max(trees[i, :j]),
                trees[i, j] > max(trees[:i, j]),
                trees[i, j] > max(trees[i, j + 1:]),
                trees[i, j] > max(trees[i + 1:, j])]):
            visible += 1
        l = get_score(trees[i, j], trees[i, :j][::-1])
        t = get_score(trees[i, j], trees[:i, j][::-1])
        r = get_score(trees[i, j], trees[i, j + 1:])
        d = get_score(trees[i, j], trees[i + 1:, j])
        prod = l*t*r*d
        if prod > max_score:
            max_score = prod

print(f'Part 1: {visible + 2 * (M + N - 2)}')
print(f'Part 2: {max_score}')

