import numpy as np 


def return_array(f):
    return np.array([get_num(line) for line in f])


def get_num(line):
    splitted_line = line.split(',')
    splitted_line = [x.split(' -> ') for x in splitted_line]
    coordinates = [int(splitted_line[0][0]), int(splitted_line[1][0]),
    int(splitted_line[1][1]), int(splitted_line[2][0])]
    return coordinates


def check_line(line, matrix):
    if line[0] == line[2]:
         matrix = vertical_line(line, matrix)
    elif line[1] == line[3]:
        matrix = horizontal_line(line, matrix)
    return matrix


def vertical_line(line, matrix):
    ordered_line = sorted([line[1], line[3]])
    y0, y1 = ordered_line[0], ordered_line[1]
    row_position = np.arange(y0, y1 + 1)
    matrix[row_position, line[0]] = matrix[row_position, line[0]] + 1
    return matrix


def horizontal_line(line, matrix):
    ordered_line = sorted([line[0], line[2]])
    x0, x1 = ordered_line[0], ordered_line[1]
    col_position = np.arange(x0, x1 + 1)
    matrix[line[1], col_position] = matrix[line[1], col_position] + 1
    return matrix


def main():
    f = open('input.txt', 'r').read().splitlines()
    lines_array = return_array(f)
    max_val = np.amax(lines_array)
    ground_truth_matrix = np.zeros((max_val+1, max_val+1))
    for line in lines_array:
        ground_truth_matrix = check_line(line, ground_truth_matrix)
    print(ground_truth_matrix)

    print('\nNumber of dangerous areas: ',len(ground_truth_matrix[ground_truth_matrix>1]))


if __name__ == '__main__':
    main()