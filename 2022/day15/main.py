import re

y_ref = 2000000
positions = []
inc, exc, append_to_exc = [], [], []
beacons, sensors = [], []
for line in open('input.txt').readlines():
    sensor_string = re.findall(r'-?\d+', line)
    s = tuple([int(x) for x in sensor_string[:2]])
    b = tuple([int(x) for x in sensor_string[2:]])
    beacons.append(b)
    sensors.append(s)
    aux = abs(s[0] - b[0]) + abs(s[1] - b[1]) - abs(y_ref - s[1])
    if aux < 0:
        continue
    tup = (s[0] - abs(aux), s[0] + abs(aux))
    # Uncomment for brute force ;)
    # positions += [ele for ele in list(range(tup[0], tup[1] + 1))]

    append_to_exc = []
    if not inc:
        inc.append(tup)
        continue

    for inc_tup in inc:
        if (tup[0] - inc_tup[1]) > 0 or (inc_tup[0] - tup[1]) > 0:
            continue
        inter = (max(tup[0], inc_tup[0]), min(tup[1], inc_tup[1]))
        append_to_exc.append(inter)
    for other in exc:
        if (tup[0] - other[1]) > 0 or (other[0] - tup[1]) > 0:
            continue
        inter = (max(tup[0], other[0]), min(tup[1], other[1]))
        if inter not in append_to_exc:
            inc = inc + [inter]
        else:
            append_to_exc.remove(inter)
    inc.append(tup)
    exc += append_to_exc
# print brute force result (takes 1.52 seconds)
# print(len(set(sorted(positions))) - 1)
print(f'Part 1 : {sum(map(lambda x: x[1] - x[0] + 1, inc)) - sum(map(lambda x: x[1] - x[0] + 1, exc)) - 1}')

# Part 2
min_c, max_c = 0, 4000000
for b, s in zip(beacons, sensors):
    found = False
    dist = abs(b[0] - s[0]) + abs(b[1] - s[1])
    for i in range(dist + 1):
        xx, yy = s[0] + i + 1, s[1] - dist + i
        if xx > max_c or xx < min_c or yy > max_c or yy < min_c:
            continue
        for other_beacon, other_sensor in (zip(beacons, sensors)):
            if s == other_sensor:
                continue
            d = abs(other_beacon[0] - other_sensor[0]) + abs(other_beacon[1] - other_sensor[1])
            if abs(xx - other_sensor[0]) + abs(yy - other_sensor[1]) <= d:
                is_closer = True
                break
            is_closer = False
        if not is_closer:
            found = True
            break
    if found:
        print(f'Part 2: {xx*max_c + yy}')
        break
