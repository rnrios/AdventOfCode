import numpy as np
from collections import Counter


def num_lantern_fish(fish_counts, n):
    for i in range(1, n+1):
        new_fishes = 0
        if fish_counts[0] > 0:
            new_fishes = fish_counts[0]
        fish_counts = update_num_fishes(fish_counts, new_fishes)
        print('After {} days: \t {}'.format(i, np.sum(fish_counts)))

        
def update_num_fishes(fish_counts, new_fishes):
    fish_counts = np.roll(fish_counts, -1)
    fish_counts[6] += new_fishes
    fish_counts[8] = new_fishes
    return fish_counts


def main():
    f = open('input.txt').readlines()
    initial_num_fishes = [int(x) for x in f[0].split(',') if x != ',']
    fish_dict = Counter(initial_num_fishes)
    fish_counts = np.zeros(9).astype(int)
    for key in fish_dict.keys():
        fish_counts[key] = fish_dict[key]
    num_lantern_fish(fish_counts, 256)


if __name__ == '__main__':
        main()