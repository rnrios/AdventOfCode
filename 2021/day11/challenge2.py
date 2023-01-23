import numpy as np

def increase_neighbors(oct_matrix, flags, pos):
    row, col = pos[0], pos[1]

    if oct_matrix[row][col] <= 9:
        return oct_matrix, flags
    

    oct_matrix[row][col] = 0
    flags[row][col] = 0

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if all([r>=0, r<oct_matrix.shape[0], c>=0, c<oct_matrix.shape[1]]):
                if (r!=row or c!=col):
                    if flags[r][c]:
                        oct_matrix[r][c] += 1
                    oct_matrix, flags = increase_neighbors(oct_matrix, flags,[r, c])
    return oct_matrix, flags
            

def main():
    f = open('input.txt', 'r').read().splitlines()
    oct_matrix = np.array([[int(x) for x in line] for line in f])
    i, acc =  0, 0
    while acc < 100:
        oct_matrix += 1
        flags = np.ones(oct_matrix.shape)
        
        max_pos = np.argwhere(oct_matrix>9)
        for pos in max_pos:
            oct_matrix, flags = increase_neighbors(oct_matrix, flags, pos)
        acc = np.sum(oct_matrix==0)
        i+=1
    print('Flashes synchronized at {} epoch.'.format(i))


if __name__ == '__main__':
    main()