import re
from ast import literal_eval


def check_empty(input_list):
    return all(map(check_empty, input_list)) if isinstance(input_list, list) else False


def get_pair(line):
    pair = None
    o, c = [], []
    is_array = False
    for i, char in enumerate(line):
        last_closed = c[-1] if c else -1
        if char == '\n':
            continue
        if char == '[':
            o.append(i)
            if is_array:
                # print('Pair, aux:')
                aux = [int(num) for num in re.findall(r'\d+', line[o[-2]:i])]
                # print(pair, aux, line[o[-2]:i])
                pair = append_inner(pair, aux)
                # print(pair)
            is_array = True
            # print(last_arr)
        elif char == ']':
            c.append(i)
            if is_array:
                aux = [int(num) for num in re.findall(r'\d+', line[o[-1]:i])]
                # if pair is None:
                #     for _ in range(len(o) - len(c)):
                #         pair = [pair] if pair is not None else []
                pair = append_inner(pair, aux)
                is_array = False
        elif char.isdigit() and not is_array:
            pair += [int(char)]
    return pair


def append_inner(l1, l2):
    if isinstance(l1, list):
        if not l1:
            return [l2] if isinstance(l2, int) or l1 is not None else l2
        elif check_empty(l1):
            return [append_inner(l1[0], l2)]
        # return l1 + [l2] if len(l1) > 1 else [l1, append_inner([], l2)]
        return [l1[0], append_inner(l1[1], l2)] if len(l1) > 1 else [l1[0], append_inner(None, l2)]
    else:
        return l2


def compare_inputs(f_list, s_list):
    l1, l2 = f_list.copy(), s_list.copy()
    while l1 and l2:
        ff, ss = l1.pop(0), l2.pop(0)
        is_int = sum([isinstance(x, int) for x in (ff, ss)])
        if is_int == 2:
            diff = ff - ss
        else:
            if is_int == 1:
                if isinstance(ff, list):
                    ss = [ss]
                else:
                    ff = [ff]
            # print(ff, ss)
            diff = compare_inputs(ff, ss)
        if diff != 0 or (l1 == l2 == []):
            return diff
    if not l1 and not l2:
        return 0
    return 1 if not l2 else -1


count = acc = 0
f = s = None
decoder = [[[2]], [[6]]]
d1, d2 = [], []
for i, line in enumerate(open('input.txt').readlines()):
    if line != '\n':
        count += 1
        if count % 2:
            f = literal_eval(line)
            pass
        else:
            s = literal_eval(line)
    else:
        count = 0
        aux = compare_inputs(f, s) < 0
        acc += aux * (i + 1) // 3
        d1 += [compare_inputs(x, [[2]]) < 0 for x in (f, s)]
        d2 += [compare_inputs(x, [[6]]) < 0 for x in (f, s)]
        # print(compare_inputs())
print(f'Part 1: {acc}')
print(f'Part 2: {(sum(d1) + 1)*(sum(d2) + 2)}')
# print(d1*d2)