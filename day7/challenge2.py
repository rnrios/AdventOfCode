import numpy as np


def get_least_fuel(x_arr, test_values):
    fuel_dict = {}
    for value in test_values:
        diff = np.sum([np.sum(range(1, abs(x-value) + 1)) for x in x_arr])
        fuel_dict[value] = diff
    return fuel_dict


def main():
    f = open('input.txt').readlines()
    pos = [int(x) for x in f[0].split(',') if x!=',']
    x_max = int(.5*max(pos))
    test_values = range(x_max)
    fuel_dict = get_least_fuel(pos, test_values)
    print(min(fuel_dict.values()))


if __name__ == '__main__':
        main()
