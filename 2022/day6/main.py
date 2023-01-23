first_flag = True
line = open('input.txt').readlines()[0]
for i in range(len(line)):
    n1 = len(set([char for char in line[i:i+4]]))
    n2 = len(set([char for char in line[i:i+14]]))
    if n1 == 4 and first_flag:
        print(f'Part 1: {i + 4}')
        first_flag = False
    if n2 == 14:
        print(f'Part 2 : {i + 14}')
        break
