from itertools import product


def make_move(start, c):
    if c == 'R':
        return start[0] + 0, start[1] + 1
    elif c == 'L':
        return start[0] + 0, start[1] - 1
    elif c == 'U':
        return start[0] + 1, start[1]
    elif c == 'D':
        return start[0] - 1, start[1]


def get_places(commands, n):
    t_list = [(0, 0)] * n
    visited = {t_list[0]}
    for d, v in commands:
        while v:
            t_list[0] = make_move(t_list[0], d)
            for i in range(1, n):
                if abs(t_list[i - 1][1] - t_list[i][1]) <= 1 and abs(t_list[i - 1][0] - t_list[i][0]) <= 1:
                    continue
                if abs(t_list[i - 1][1] - t_list[i][1]) + abs(t_list[i - 1][0] - t_list[i][0]) == 2:
                    if t_list[i - 1][1] == t_list[i][1]:
                        t_aux = make_move(t_list[i], 'U') if t_list[i-1][0] > t_list[i][0] else make_move(t_list[i], 'D')
                    if t_list[i - 1][0] == t_list[i][0]:
                        t_aux = make_move(t_list[i], 'R') if t_list[i-1][1] > t_list[i][1] else make_move(t_list[i], 'L')
                else:
                    min_dist = 10
                    for x, y in product((-1, 1), (-1, 1)):
                        if abs(t_list[i - 1][1] - t_list[i][1]-y) + abs(t_list[i - 1][0] - t_list[i][0]-x) < min_dist:
                            min_dist = abs(t_list[i - 1][1] - t_list[i][1]) + abs(t_list[i - 1][0] - t_list[i][0])
                            t_aux = (t_list[i][0] + x, t_list[i][1] + y)
                t_list[i] = t_aux
            visited.add(t_list[n - 1])
            v -= 1
    return visited


cmd_list = []
for line in open('input.txt').readlines():
    if line == '\n':
        continue
    direction, value = line.split(' ')
    cmd_list.append((direction, int(value[:-1])))
print(f'Part 1: {len(get_places(cmd_list, 2))}')
print(f'Part 2: {len(get_places(cmd_list, 10))}')
