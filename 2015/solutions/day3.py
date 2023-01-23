def get_pos(start):
    if char == '<':
        end = (start[0] - 1, start[1])
    if char == '>':
        end = (start[0] + 1, start[1])
    if char == 'v':
        end = (start[0], start[1] - 1)
    if char == '^':
        end = (start[0], start[1] + 1)
    return end


s = s1 = s2 = (0, 0)
places = set()
p1, p2 = set(), set()
p1.add(s)
p2.add(s)
places.add(s)
line = open('../inputs/input3.txt').readlines()[0]
for i, char in enumerate(line):
    s = get_pos(s)
    places.add(s)
    if i % 2:
        s2 = get_pos(s2)
        p2.add(s2)
    else:
        s1 = get_pos(s1)
        p1.add(s1)
print(p1, p2)
print(f'Part 1: {len(places)}')
print(f'Part 2: {len(p1 | p2)}')
