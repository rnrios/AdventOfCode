count = 0
queue = []
found_position = False
line = open('../inputs/input1.txt').readlines()[0]
for i, char in enumerate(line):
    if char == '(':
        count += 1
        queue.append('(')
    elif char == ')':
        count -= 1
        if queue:
            queue.pop()
        elif not found_position:
            position = i + 1
            found_position = True

print(f'Part 1: {count}')
print(f'Part 1: {position}')
