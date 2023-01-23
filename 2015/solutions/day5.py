from collections import Counter
from itertools import product


def get_3_vowels(input_string):
    char_dict = Counter(input_string)
    return sum(char_dict[k] for k in ('a', 'e', 'i', 'o', 'u')) >= 3


def get_double(input_string):
    for i in range(97, 123):
        if chr(i) + chr(i) in input_string:
            return True
    return False


def get_exclusions(input_string):
    for word in ('ab', 'cd', 'pq', 'xy'):
        if word in input_string:
            return False
    return True


def get_repeat_no_overlap(input_string):
    w = [chr(i) for i in range(97, 123)]
    for (x, y) in product(w, w):
        d = 0
        res = input_string.count(x + y)
        if x == y and res >= 2:
            d = input_string.count(x + y + x) - 1
        res -= d
        if res >= 2:
            return True
    return False


def get_palindrome_3(input_string):
    w = [chr(i) for i in range(97, 123)]
    for (x, y) in product(w, w):
        res = input_string.count(x + y + x)
        # if x == 'o' and y == 'd':
        #     print(res, x + y + x, input_string.count('odo'), input_string)
        if res >= 1:
            return True
    return False


count = count_p2 = 0
for string in open('../inputs/input5.txt'):
    string = string.strip()
    if all((get_3_vowels(string), get_double(string), get_exclusions(string))):
        count += 1
    if all((get_palindrome_3(string), get_repeat_no_overlap(string))):
        count_p2 += 1
print(f'Part 1: {count}')
print(f'Part 2: {count_p2}')

