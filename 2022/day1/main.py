calories = []
prev = -1
lines = open('input.txt').readlines()
for i, line in enumerate(lines):
    if line == '\n':
        calories.append(sum([int(x) for x in lines[prev+1:i]]))
        prev = i
print(f'Max calories: {max(calories)}')
print(f'Sum of top 3: {sum(sorted(calories)[-3:])}')
