import numpy as np 
from collections import Counter


def split(string):
    return [int(char) for char in string]


def return_matches(array, i, bin_value):
    array = np.array([element for element in array if element[i]==bin_value])
    return array


def main():
    f = [split(x.split('\n')[0]) for x in open('input.txt').readlines()]
    oxi = co2 = np.array(f)
    array_len = oxi.shape[1]
    for i in range(array_len):
        column_dict = Counter(oxi[:,i])
        bin_value = 0 if column_dict[0] > column_dict[1] else 1
        oxi = return_matches(oxi, i, bin_value)
        if oxi.shape[0] == 1:
            break

    for i in range(array_len):
        column_dict = Counter(co2[:,i])
        bin_value = 0 if column_dict[0] <= column_dict[1] else 1
        co2 = return_matches(co2, i, bin_value)
        if co2.shape[0] == 1:
            break

    oxi_num = 0
    for i,x in enumerate(reversed(split(oxi[0]))):
        oxi_num+=x*2**(i)

    co2_num = 0
    for i,x in enumerate(reversed(split(co2[0]))):
        co2_num+=x*2**(i)
    print(oxi_num*co2_num)


if __name__ == '__main__':
    main()


    







