def prod_array(array):
    if len(array) == 1:
        return array[0]
    return array[0] * prod_array(array[1:])


t1 = t2 = 0
for line in open('../inputs/input2.txt'):
    arr = list(map(int, line.strip().split('x')))
    t1 += 2 * (arr[0] * arr[1] + arr[1] * arr[2] + arr[0] * arr[2])
    t2 += prod_array(arr)
    arr.pop(arr.index(max(arr)))
    # total = total + arr[0] * arr[1]
    t1 += arr[0] * arr[1]
    t2 += 2*(arr[0] + arr[1])
print(f'Part 1: {t1}')
print(f'Part 2: {t2}')
