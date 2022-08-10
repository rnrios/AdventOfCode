import numpy as np


def create_dict(inputs):
    len_dict = {2: 1, 3:7, 4:4, 7:8}
    know_numbers = {}

    for x in inputs:
        if len(x) in len_dict.keys():
            know_numbers[len_dict[len(x)]] = x

    output_dict = {}

    for x in inputs:
        if x not in know_numbers.values():
            output_dict = compare_digits(x, know_numbers, len(x), output_dict)
        else:
            output_dict[x] = len_dict[len(x)]
    return output_dict


def compare_digits(unknown, known, len, output_dict):
    if len == 5:
        digits_1 = np.sum([x in unknown for x in known[1]])
        if digits_1 == 2:
            output_dict[unknown] = 3
        else:
            digits_4 = np.sum([x in unknown for x in known[4]])
            if digits_4 == 2:
                output_dict[unknown] = 2
            else:
                output_dict[unknown] = 5

    elif len == 6:
        digits_4 = np.sum([x in unknown for x in known[4]])
        if digits_4 == 4:
            output_dict[unknown] = 9
        else:
            digits_7 = np.sum([x in unknown for x in known[7]])
            if digits_7 == 3:
                output_dict[unknown] = 0
            else:
                output_dict[unknown] = 6
    return output_dict
    

def check_dict(x, keys):
    for key in keys:
        key_flag = True
        for char in x:
            if char in key:
                continue
            else:
                key_flag = False
                break
        if key_flag == True and len(x) == len(key):
            return key


def return_sum(x):
    x = np.array(x)
    y = 10**(np.array(list(reversed(range(len(x))))))
   
    return np.dot(x, y)


def main():
    f = open('input.txt', 'r').read().splitlines()
    inputs, outputs = [], []

    total_sum = 0
    for i, line in enumerate(f):
        line = line.split(' ')
        inputs = line[:10]
        outputs = line[-4:]
        
        output_list = []
        output_dict = create_dict(inputs)
        for output in outputs:
            key = check_dict(output, list(output_dict.keys()))
            output_list.append(output_dict[key])
        total_sum += return_sum(output_list)
    print('Total sum: ', total_sum)  


if __name__ == '__main__':
        main()
