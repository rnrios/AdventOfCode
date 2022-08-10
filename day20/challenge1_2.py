import numpy as np


def check_neighbors(matrix, copy_matrix, i, j, alg):
    pos = (i, j)
    counts = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            counts.append(1 if matrix[pos[0] + i, pos[1] + j] == '#' else 0)
    counts_num = bin2dec(counts)
    copy_matrix[pos] = alg[counts_num]
    return copy_matrix


def all_zeros(matrix, i, j):
    return (matrix[i - 1:i + 2, j - 1:j + 2] == '.').all()


def all_ones(matrix, i, j):
    return (matrix[i - 1:i + 2, j - 1:j + 2] == '.').all()


def bin2dec(arr):
    arr_len = len(arr) - 1
    for i, x in enumerate(arr):
        arr[i] = x * 2 ** (arr_len - i)
    return np.sum(arr)


def main():
    f = open('input.txt', 'r').read().splitlines()
    algorithm: str = f[0]
    h = w = len(f[2])
    matrix = np.zeros((h, w)).astype(str)
    for i, line in enumerate(f[2:]):
        for j, row in enumerate(line):
            matrix[i, j] = f[2:][i][j]

    num = 50
    matrix = np.pad(matrix, [num + 1, num + 1], mode='constant', constant_values='.')
    for k in range(num):
        copy_matrix = matrix.copy()
        for i, line in enumerate(matrix):
            for j, row in enumerate(matrix):
                if not all([i > 0, i < matrix.shape[0] - 1, j > 0, j < matrix.shape[1] - 1]):
                    if algorithm[0] == '.':
                        copy_matrix[i][j] = '.'
                    else:
                        copy_matrix[i][j] = '#' if k % 2 == 0 else '.'
                elif all_zeros(matrix, i, j):
                    copy_matrix[i][j] = algorithm[0]
                elif all_ones(matrix, i, j):
                    copy_matrix[i][j] = algorithm[-1]
                else:
                    copy_matrix = check_neighbors(matrix, copy_matrix, i, j, algorithm)
        matrix = copy_matrix
    print(np.count_nonzero(matrix == '#'))


if __name__ == '__main__':
    main()
