import numpy as np


def parse_txt(f):
    dots = []
    instructions = []
    for i, line in enumerate(f):
        if line == '':
            instructions = f[i+1:]
            break
        else:
            dots.append([int(x) for x in line.split(',')])
    msg_list = []
    for instruction in instructions:
        msg = instruction.split('fold along ')[1].split('=')
        msg_list.append([msg[0], int(msg[1])])
    return msg_list, dots


def print_code(matrix):
    prints_str = []
    for row in matrix:
        string = ''
        for x in row:
            c = '#' if x == 1 else ' '
            string += c
        prints_str.append([string])
    
    for string in prints_str:
        print(string)


def main():
    f = open('input.txt', 'r').read().splitlines()
    msg_list, dots = parse_txt(f)
    dots_array = np.array(dots)
    max_x = max(dots_array[:,1]) + 1
    max_y = max(dots_array[:,0]) + 1
    matrix = np.zeros((max_x, max_y)).astype(int)
    for dot in dots:
        matrix[dot[1]][dot[0]] = 1
    for i, msg in enumerate(msg_list):
        if msg[0] == 'y':
            matrix = matrix[:msg[1],:] | np.flip(matrix[-msg[1]:,:], axis=0)
        if msg[0] == 'x':
            matrix = matrix[:,:msg[1]] | np.flip(matrix[:,-msg[1]:], axis=1)
    print_code(matrix)    


if __name__ == '__main__':
    main()