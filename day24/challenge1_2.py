def parse_txt():
    f = open('input.txt').read().split('\n')
    instructions = []
    i = j = 0
    for j, line in enumerate(f):
        if len(line.split(' ')) == 2 and j != 0:
            instructions.append(f[i:j])
            i = j
    instructions.append(f[i:j])
    return instructions


def alu(vd, instruction, w):
    var_dict = vd.copy()
    for op in instruction:
        if len(op.split(' ')) == 2:
            var_dict['w'] = w
        else:
            opcode, op1, op2 = tuple(op.split(' '))
            if opcode == 'add':
                var_dict[op1] += int(op2) if op2 not in var_dict.keys() else var_dict[op2]
            if opcode == 'mul':
                var_dict[op1] *= int(op2) if op2 not in var_dict.keys() else var_dict[op2]
            if opcode == 'div':
                var_dict[op1] = var_dict[op1] // int(op2) if op2 not in var_dict.keys() else var_dict[op1] // var_dict[
                    op2]
            if opcode == 'mod':
                var_dict[op1] %= int(op2) if op2 not in var_dict.keys() else var_dict[op2]
            if opcode == 'eql':
                var_dict[op1] = var_dict[op1] == int(op2) if op2 not in var_dict.keys() else var_dict[op1] == var_dict[
                    op2]
    return var_dict


def tree_search(instructions, z):
    new_ws = ()
    p1 = int(instructions[0][5].split(' ')[2])
    p2 = int(instructions[0][-3].split(' ')[2])

    if len(instructions) == 1:
        for i, val in enumerate(FIRST):
            if val == z:
                return str(i + 1)

    # DIV 26
    if int(instructions[0][4].split(' ')[2]) != 1:
        # Caso 1
        if 1 <= z - p2 <= 9:
            for i in range(-25, 26):
                if i - p1 != z - p2 and z != 0:
                    upper = tree_search(instructions[1:], i)
                    if upper is not None:
                        new_ws = new_ws + tuple(map(lambda t: t + str(z - p2), upper))
        # Caso 2
        ws2 = [w for w in range(1, 10) if w - p1 >= 0]
        if len(ws2) >= 1:
            for w2 in ws2:
                new_z = 26 * z + w2 - p1
                upper = tree_search(instructions[1:], new_z)
                if upper is not None:
                    new_ws = new_ws + tuple(map(lambda t: t + str(w2), upper))
    # DIV 1
    else:
        new_w = z % 26 - p2
        if 1 <= new_w <= 9:
            if z >= 0:
                new_z = int(z / 26)
            else:
                new_z = int(z / 26) - 1
            upper = tree_search(instructions[1:], new_z)
            if upper is not None:
                new_ws = new_ws + tuple(map(lambda t: t + str(new_w), upper))
    return new_ws


FIRST = []


def main():
    var_dict = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    instructions = parse_txt()
    for w in range(1, 10):
        out = alu(var_dict, instructions[0], w)
        FIRST.append(out['z'])

    x = ()
    for w in range(1, 10):
        tmp_tuple = tuple(map(lambda t: t + str(w), tuple(tree_search(instructions[::-1][1:], w + 7))))
        x = x + tuple(map(lambda t: int(t), tmp_tuple))
    print(f'Max value: {max(x)}')
    print(f'Min value: {min(x)}')


if __name__ == '__main__':
    main()
