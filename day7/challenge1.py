import numpy as np


def get_least_fuel(x, test_values):
    fuel_dict = {}
    for value in test_values:
        diff = np.sum(abs(x-value*np.ones(len(x))))
        fuel_dict[value] = diff
    return fuel_dict


def main():
    f = open('input.txt').readlines()
    pos = [int(x) for x in f[0].split(',') if x!=',']
    x_max = 2*max(pos)
    test_values = range(x_max)
    fuel_dict = get_least_fuel(pos, test_values)
    print(min(fuel_dict.values()))
    

if __name__ == '__main__':
        main()