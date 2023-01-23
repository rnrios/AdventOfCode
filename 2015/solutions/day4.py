from hashlib import md5


def find_hash(prefix='00000'):
    num = 0
    while True:
        num += 1
        input_string = base + str(num)
        string_decoded = md5(input_string.encode()).hexdigest()
        if string_decoded[:len(prefix)] == prefix:
            return num


base = open('../inputs/input4.txt').read()
print(f'Part 1: {find_hash()}')
print(f'Part 2: {find_hash("000000")}')
