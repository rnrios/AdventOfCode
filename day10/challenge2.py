from collections import Counter
import numpy as np
from collections import deque


def check_line(line):
    stack = []
    open_chunks = np.array(['[', '(', '{', '<'])
    close_chunks = np.array([']', ')', '}', '>'])
    points = {'(': 1, '[':2 , '{':3, '<':4}

    for i, x in enumerate(line):
        if x in open_chunks:
            stack.append(x)
        if x in close_chunks:
            current = stack.pop()
            expected = open_chunks[close_chunks==x][0]
            if expected!= current:
                return 0   
    
    acc = 0
    flipped_stack = np.flip(stack)
    for x in flipped_stack:
        acc = 5*acc + points[x]
    
    return acc


def main():
    x = np.zeros(4)
    y = np.array(['[', '(', '{', '<'])
    f = open('input.txt', 'r').read().splitlines()
    scores = np.array([check_line(line) for line in f])
    print(np.median(scores[scores!=0]))
        

if __name__ == '__main__':
    main()
    