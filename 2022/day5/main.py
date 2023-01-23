import re
from collections import defaultdict


def crate_mover(is_9000=True):
    stacks_dict = defaultdict(list)
    for line in open('input.txt').readlines():
        if '[' in line:
            for i, char in enumerate(line):
                if i % 4 == 1 and char.isalpha():
                    stacks_dict[i // 4 + 1].append(char)
        elif 'm' in line:
            q, origin, destiny = [int(c) for c in re.findall(r'\d+', line)]
            if is_9000:
                stacks_dict[destiny] = stacks_dict[origin][:q][::-1] + stacks_dict[destiny]
            else:
                stacks_dict[destiny] = stacks_dict[origin][:q] + stacks_dict[destiny]
            stacks_dict[origin] = stacks_dict[origin][q:]
        else:
            continue
    message = ''
    for i in range(1, len(stacks_dict) + 1):
        message += stacks_dict[i][0]
    return message


print(f'Message from part 1: {crate_mover()}')
print(f'Message from part 2: {crate_mover(False)}')
