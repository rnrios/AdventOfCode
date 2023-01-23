import numpy as np 
from collections import Counter


def split(string):
    return [int(char) for char in string]


def main():
    f = [split(x.split('\n')[0]) for x in open('input.txt').readlines()]
    x = np.array(f)
    array_len = x.shape[1]
    gamma = 0
    for i in range(array_len):
        column_dict = Counter(x[:,i])
        bin_value = 0 if column_dict[0] > column_dict[1] else 1
        gamma += bin_value*2**(array_len-i-1)
    epsilon = 2**(array_len) - 1 - gamma
    print(gamma*epsilon)


if __name__ == '__main__':
        main()