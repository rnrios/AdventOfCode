def str_to_num(char):
    return ord(char.lower()) - 96 + (1 - char.islower()) * 26


# part 1
acc = 0
for line in open('input.txt').readlines():
    n = len(line)
    f, s = line[:int(n/2)], line[int(n/2):]
    common = [char for char in f if char in s]
    acc += str_to_num(common[0])
print(acc)
# part 2
f, s, acc = [], [], 0
for i, line in enumerate(open('input.txt').readlines()):
    if i % 6 < 3:
        f.append([ch for ch in line])
    else:
        s.append([ch for ch in line])
        if i % 6 == 5:
            ch1 = set(f[0]) & set(f[1]) & set(f[2]) - set('\n')
            ch2 = set(s[0]) & set(s[1]) & set(s[2]) - set('\n')
            f, s = [], []
            acc += str_to_num(ch1.pop()) + str_to_num(ch2.pop())
print(acc)


