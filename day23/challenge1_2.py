import numpy as np
from functools import lru_cache

COST_MATRIX = [[2, 4, 6, 8],
               [1, 3, 5, 7],
               [1, 1, 3, 5],
               [3, 1, 1, 3],
               [5, 3, 1, 1],
               [7, 5, 3, 1],
               [8, 6, 4, 2]]


def clear_path(hallway, h, r, offset=False):
    # moving left
    if h >= r + 2:
        for h in hallway[r + 2:h]:
            if h is not None:
                return False
    # moving right
    else:
        for h in hallway[h + offset:r + 2]:
            if h is not None:
                return False
    return True


def universes(rooms, hallway):
    yield from hallway_to_room(rooms, hallway)
    yield from room_to_hallway(rooms, hallway)


def cost_function(a_type, h, r, r_pos):
    return 10 ** a_type * (COST_MATRIX[h][r] + r_pos)


def hallway_to_room(rooms, hallway):
    for h_pos, a_type in enumerate(hallway):
        if a_type is None:
            continue

        # room: destination room of a_type
        room = rooms_dict[a_type]
        if any(rooms_dict[a] not in [None, room] for a in rooms[room::4]):
            continue

        if not clear_path(hallway, h_pos, room, True):
            continue

        r_pos = max([i for i, a in enumerate(rooms[room::4]) if a is None]) * 4 + room
        cost = cost_function(room, h_pos, room, int(r_pos / 4) + 1)

        new_rooms = rooms[:r_pos] + (a_type,) + rooms[r_pos + 1:]
        new_hallway = hallway[:h_pos] + (None,) + hallway[h_pos + 1:]

        yield (new_rooms, new_hallway), cost


def room_to_hallway(rooms, hallway):
    for room in range(4):
        if all(rooms_dict[r] == room for r in rooms[room::4]):
            continue

        if rooms_dict[rooms[room]] is None and rooms_dict[rooms[room + 4]] == room:
            continue

        for h_pos, _ in enumerate(hallway):

            if not clear_path(hallway, h_pos, room):
                continue

            if any(rooms_dict[a] not in [None, room] for a in rooms[room::4]):
                r_pos = min([i for i, a in enumerate(rooms[room::4]) if a is not None]) * 4 + room
            else:
                continue

            cost = cost_function(rooms_dict[rooms[r_pos]], h_pos, room, int(r_pos / 4) + 1)

            new_rooms = rooms[:r_pos] + (None,) + rooms[r_pos + 1:]
            new_hallway = hallway[:h_pos] + (rooms[r_pos],) + hallway[h_pos + 1:]

            yield (new_rooms, new_hallway), cost


@lru_cache(None)
def best_path(rooms, hallway):
    cost = 0
    if all([all([rooms_dict[r] == room for r in rooms[room::4]]) for room in range(4)]):
        # print(rooms)
        return 0

    min_cost = np.inf
    for state, cost in universes(rooms, hallway):
        # print(cost)
        cost += best_path(state[0], state[1])
        if cost < min_cost:
            min_cost = cost

    return min_cost


rooms_dict = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    None: None
}


def main():
    hallway = (None, None, None, None, None, None, None)
    rooms_pt1 = ('B', 'B', 'D', 'D',
                 'C', 'A', 'A', 'C')
    rooms_pt2 = ('B', 'B', 'D', 'D',
                 'D', 'C', 'B', 'A',
                 'D', 'B', 'A', 'C',
                 'C', 'A', 'A', 'C')
    print('Part 1: ', best_path(rooms_pt1, hallway))
    print('Part 2: ', best_path(rooms_pt2, hallway))


if __name__ == '__main__':
    main()
