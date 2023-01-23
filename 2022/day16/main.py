import re
from collections import defaultdict
from functools import partial
from itertools import product
from math import inf as INFINITY


valves_rates, tunnels = {}, {}
no_flow = []
for line in open('input.txt').readlines():
    rate = int(line.split('=')[1].split(';')[0])
    v = re.findall(r'[A-Z]+', line)
    # if rate or v[1] == 'AA':
    valves_rates[v[1]] = rate
    tunnels[v[1]] = v[2:]

distances = {}
for valve in valves_rates:
    dist = 0
    if not valves_rates[valve] and valve != 'AA':
        continue
    tmp_queue, visited = [], set()
    distances[valve] = {}
    queue = [v for v in tunnels[valve]]
    while queue:
        next_ele = queue.pop(0)
        visited.add(next_ele)
        if valves_rates[next_ele] and next_ele not in distances[valve]:
            distances[valve][next_ele] = dist + 1
        for other_valve in tunnels[next_ele]:
            if other_valve != valve:
                tmp_queue.append(other_valve)
        if not len(queue):
            dist += 1
            queue.extend(set(tmp_queue) - visited)


def get_paths(distances, tunnels, state, path):
    for nxt in tunnels:
        new_time = state[0] - distances[state[1]][nxt] - 1
        if new_time < 2:
            continue
        new_chosen = dict(path.items() | {nxt: new_time}.items())
        yield from get_paths(distances, tunnels - {nxt}, (new_time, nxt), new_chosen)
    yield path


def score(rates, chosen_valves):
    tot = 0
    for valve, time_left in chosen_valves.items():
        tot += rates[valve] * time_left
    return tot

print(len(distances.keys()))
# score = partial(score, valves_rates)
# best = max(map(score, get_paths(distances, distances.keys() - {'AA'}, (30, 'AA'), {})))
# print(best)
