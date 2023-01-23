import re

buffer, total = [], 0
for line in open('input.txt').readlines():
    if re.findall(r'\d+', line):
        buffer += [0, int(re.findall(r'-?\d+', line)[0])]
        cycle = len(buffer) // 20 * 20
        if (len(buffer) % 20 == 0 or len(buffer) % 20 == 1) and cycle//20 % 2 == 1:
            total += cycle*(sum(buffer[:cycle-1])+1)
    else:
        buffer += [0]
        cycle = len(buffer) // 20 * 20
        if len(buffer) % 20 == 0 and cycle//20 % 2 == 1:
            total += cycle * (sum(buffer[:cycle - 1]) + 1)
print(f'Part 1: {total}')
print('Part 2:')

for i in range(240):
    val = sum(buffer[:i]) + 1
    if val - 1 <= i % 40 <= val + 1:
        print('# ', end='')
    else:
        print('. ', end='')
    if i % 40 == 39:
        print()
