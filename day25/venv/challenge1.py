def move_east(in_matrix, moved, h, w):
    out = in_matrix.copy()
    for i in range(h):
        for j in range(w):
            if in_matrix[i][j] != '>':
                continue
            if in_matrix[i][(j + 1) % w] == '.':
                moved = True
                out[i][j] = '.'
                out[i][(j + 1) % w] = '>'
    return out, moved


def move_south(in_matrix, moved, h, w):
    out = in_matrix.copy()
    for i in range(h):
        for j in range(w):
            if in_matrix[i][j] != 'v':
                continue
            if in_matrix[(i + 1) % h][j] == '.':
                moved = True
                out[i][j] = '.'
                out[(i + 1) % h][j] = 'v'
    return out, moved


def return_moves(in_matrix):
    h, w = in_matrix.shape
    count = 0
    while True:
        moved = False
        m1, moved = move_east(in_matrix, moved, h, w)
        m2, moved = move_south(m1, moved, h, w)
        count += 1
        in_matrix = m2.copy()
        if not moved:
            return count


def parse_txt(file_path):
    f = open(file_path).read().split('\n')
    initial_state = np.zeros((len(f), len(f[0]))).astype(str)
    for i, line in enumerate(f):
        for j, x in enumerate(line):
            initial_state[i][j] = x
    return initial_state


def main():
    initial_state = parse_txt('input.txt')
    print(return_moves(initial_state))


if __name__ == '__main__':
    main()
