import math
import itertools as it


def split(f, i):
    num = int(f[i:i+2])
    val = '[' + str(math.floor(num/2)) + str(',') + str(math.ceil(num/2)) + ']'
    return f[:i] + val + f[i+2:]
        

def get_suffix(num, string):
    string_list = list(string)
    for i, x in enumerate(string_list):
        if x not in ['[', ']', ',']:
            if string_list[i+1] not in ['[', ']', ',']:
                string_list[i:i+2] = str(num+int(x+string_list[i+1]))
                break
            else:
                string_list[i] = str(num+int(x))
                break
    return ''.join(string_list)


def get_preffix(num, string):
    string_list = list(string)
    for i, x in reversed(list(enumerate(string))):
        if x not in ['[', ']', ',']:
            if string_list[i-1] not in ['[', ']', ',']:
                string_list[i-1:i+1] = str(num+int(string_list[i-1]+x))
                break
            else:
                string_list[i] = str(num+int(x))
                break
    return ''.join(string_list)


def explode(f, i):
    block = f[i:].split(',')[0]
    count = 0
    for pos, x in enumerate(f[i:]):
        if x == ']':
            count+=1
        if count == 2:
            break

    while f[i+3] == '[':
        if f[i+3] == '[':
            i+=3
            while f[i+1] == '[':
                i+=1
    
    off1 = len(f[i+1:i+6].split(',')[0])
    off2 = len(f[i+1:i+6].split(',')[1].split(']')[0])
    preffix = get_preffix(int(f[i+1:i+1+off1]), f[:i])
    suffix = get_suffix(int(f[i+2+off1:i+2+off1+off2]), f[i+3+off1+off2:])
    new_f = preffix + '0' + suffix

    return new_f


def return_snailfish_num(f):
    count = 0
    aux = 0
    while True:
        initial_string = f
        count = 0
        f = check_explode(f)
        f = check_split(f)
        if f == initial_string:
            return f


def add_snailfish_num(x1, x2):
    return '[' + x1 + ',' + x2 +']'


def check_split(f):
    for i, x in enumerate(f):
        if x not in ['[', ']', ','] and f[i+1] not in ['[', ']', ',']: 
            f = split(f, i)
            break
    return f


def check_explode(f):
    while True:
        count = 0
        init = f
        for i, x in enumerate(f):
            if x in ['[', ']', ',']:
                if x == '[':
                    count+=1
                if x == ']':
                    count -= 1
            if count == 5:
                if f[i+1] == '[':
                    count -=1
                    continue
                f = explode(f, i)
                break
        if f == init:
            return f

def mag_sum(string):
    arr_list = [x if x in ['[', ',', ']'] else int(x) for x in string]
    while True:
        if len(arr_list) < 4:
            break
        for i, x in enumerate(arr_list):
            if x != ']':
                continue
            
            num = arr_list[i-3]*3 + arr_list[i-1]*2
            arr_list = arr_list[:i-4] + [num] + arr_list[i+1:]
            break
    return arr_list[0]


def main():
    f = open('input.txt', 'r').read().splitlines()
    
    comb = it.product(f, f)
    max_value = 0
    for c in comb:
        if c[0] != c[1]:
            result = add_snailfish_num(c[0], c[1])
            value = mag_sum(return_snailfish_num(result))
            max_value = max_value if max_value > value else value
    print(max_value)


if __name__ == '__main__':
    main()