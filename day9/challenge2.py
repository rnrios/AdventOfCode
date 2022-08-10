import numpy as np


def check_surroundings(x, row, col, p, flags):
    count = 1

    if (x[row][col] == 9):
        return 0

    if (x[row][col] <= p):
        return 0

    if flags[row][col] == 0:
        return 0

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if all([r >= 0, col >= 0, r < x.shape[0], c <  x.shape[1]]):
                if (abs(r-row) + abs(c-col) == 1):
                    count += check_surroundings(x, r, c, x[row][col], flags)
    flags[row][col] = 0
    return count


def multiply_array(x):
    if len(x) == 1:
        return x[0]
    
    return x[0]*multiply_array(x[1:])


def main():
    f = open('input.txt', 'r').read().splitlines()
    array = np.array([[int(x) for x in y] for y in f])
    low_pos = []
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            flag = True 
            if i-1 >= 0 and flag==True:
                flag = True if array[i][j] < array[i-1][j] else False
            if j-1 >= 0 and flag==True:
                flag = True if array[i][j] < array[i][j-1] else False
            if j+1 < array.shape[1] and flag==True:
                flag = True if array[i][j] < array[i][j+1] else False
            if i+1 < array.shape[0] and flag==True:
                flag = True if array[i][j] < array[i+1][j] else False
            if flag == True:
                low_pos.append([i,j])
 
    basins = []
    for pos in low_pos:         
        row, col = pos[0], pos[1]  
        x_flags = np.ones(array.shape)
        basins.append(check_surroundings(array, row, col, -1, x_flags))
    print(multiply_array(sorted(basins)[-3:]))

if __name__ == '__main__':
    main()

