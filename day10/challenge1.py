from collections import Counter
import numpy as np
from collections import deque


def check_line(line):
    stack = []
    open_chunks = np.array(['[', '(', '{', '<'])
    close_chunks = np.array([']', ')', '}', '>'])
    penalty = {']': 57, ')':3 , '}':1197, '>':25137}

    for x in line:
        if x in open_chunks:
            stack.append(x)
        if x in close_chunks:
            current = stack.pop()
            expected = open_chunks[close_chunks==x][0]
            if expected!= current:
                return penalty[x]       
    return 0


def main():
    x = np.zeros(4)
    y = np.array(['[', '(', '{', '<'])
    f = open('input.txt', 'r').read().splitlines()
    print(np.sum([check_line(line) for line in f]))
        

if __name__ == '__main__':
    main()
    