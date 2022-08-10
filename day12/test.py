import numpy as np


def create_tree(pos, matrix, flags):
    count = 0
    transitions = np.argwhere(matrix[pos, :]!=0).ravel()
    next_loc = [x for x in transitions if x!= 0 and flags[x]]
    print(pos, next_loc, flags)
    if pos == len(matrix) - 1:
        flags[pos] = 1
        return 1, flags

    if len(next_loc) == 0:
        flags[pos] = 1
        return 0, flags

    for loc in next_loc:
        if matrix[pos][loc] == 2:
            flags[loc] = 0
        c, flags = create_tree(loc, matrix, flags)
        print('\t\t\t',pos, flags)
        flags[loc] = 1
        count += c
       
    return count, flags


def main():
    f = open('test_input1.txt', 'r').read().splitlines()
    connections = [x.split('-') for x in f]
    loc_dict = {}
    for line in connections:
        for x in line:
            if x not in loc_dict.keys():
                loc_dict[x] = len(loc_dict.keys())
    
    num_locations = len(loc_dict)
    transition_matrix = np.zeros((num_locations, num_locations))
    
    for conn in connections:
        row = loc_dict[conn[0]]
        col = loc_dict[conn[1]]
        transition_matrix[row][col] = 2 if conn[1].islower() else 1
        transition_matrix[col][row] = 2 if conn[0].islower() else 1
    flags = np.ones(transition_matrix.shape[1])

    print(transition_matrix)
    print(create_tree(0, transition_matrix, flags)[0])
    
    
if __name__ == '__main__':
    main()