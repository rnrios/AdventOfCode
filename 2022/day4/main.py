acc, acc_total, count = 0, 0, 0
for count, line in enumerate(open('input.txt').readlines()):
    if line == '\n':
        continue
    first, second = line.split(',')
    ff, fs = first.split('-')
    sf, ss = second.split('-')
    if int(ff) <= int(sf) and int(fs) >= int(ss):
        acc += 1
    elif int(sf) <= int(ff) and int(ss) >= int(fs):
        acc += 1
    if int(fs) < int(sf) or int(ff) > int(ss):
        acc_total += 1
print(f'Part 1: {acc}')
print(f'Part 2: {count + 1 - acc_total}')
