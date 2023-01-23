import numpy as np
from utils import count_increases


def window_counts():
    f = open('input1.txt')
    array = [float(line.split('\n')[0]) for line in f.readlines()]
    sum = []
    for i in range(len(array) - 2):
        sum.append(np.sum(array[i:i+3]))
    print(count_increases(sum))

if __name__ == '__main__':
    window_counts()
    
