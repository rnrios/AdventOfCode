import itertools as it
import functools

OUTCOMES = tuple(map(sum, it.product([1, 2, 3], repeat=3)))


def new_position(position, roll):
    if position + roll < 11:
        position = position + roll
    else:
        position = (position + roll) % 10
        if position == 0:
            position = 10
    return position


@functools.lru_cache(maxsize=None)
def dirac_dice(this_pos, this_score, next_pos, next_score):
    if this_score >= 21:
        return 1, 0

    elif next_score >= 21:
        return 0, 1

    p1_wins = p2_wins = 0
    for outcome in OUTCOMES:
        temp_score = this_score
        temp_pos = new_position(this_pos, outcome)
        temp_score += temp_pos

        n, t = dirac_dice(next_pos, next_score, temp_pos, temp_score)

        p1_wins += t
        p2_wins += n

    return p1_wins, p2_wins


def main():
    p1 = [2, 0]
    p2 = [10, 0]
    x, y = dirac_dice(p1[0], p1[1], p2[0], p2[1])
    print(x if x > y else y)


if __name__ == '__main__':
    main()
