import re


def get_pair(line):
    pair = []
    o, c = [], []
    is_array = False
    for i, char in enumerate(line):
        if char == '[':
            last_arr = re.findall(r'\d+', line[o[-1]:i]) if len(o) > 0 else None
            if is_array and len(last_arr):
                aux = [int(num) for num in last_arr]
                pair = append_inner(pair, aux)
            is_array = True
            o.append(i)
        elif char == ']' and is_array:
            c.append(i)
            aux = [int(num) for num in re.findall(r'\d+', line[o[-1]:i])]
            for _ in range(len(o) - len(c)):
                aux = [aux]
            print(pair, aux)
            pair += aux
            is_array = False
        if char.isdigit() and not is_array:
            pair += [int(char)]

    return pair


def append_inner(l1, l2):
    if not l1:
        return l2
    return [l1[0], append_inner(l1[1], l2)] if len(l1) > 1 else [l1[0], append_inner([], l2)]

count = 0
f = s = None
for line in open('day15.txt').readlines():
    if line != '\n':
        count += 1
        if count % 2:
            f = get_pair(line)
            pass
        else:
            s = get_pair(line)
    else:
        count = 0
        print(f)
        print(s)
        print()


x = [[1, [2,5]]]
y = [[2, 3, 4]]
print(append_inner(x, y))
print(x+y)
# print(get_pair('[[[1]]]\n'))
