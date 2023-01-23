score = 0
score_dict = {'X': 1, 'Y': 2, 'Z': 3}
for play in open('input.txt').readlines():
    a, b = play.split()
    if a + b in ['AX', 'BY', 'CZ']:
        score += 3
    else:
        if a == 'A':
            score += 6 if b == 'Y' else 0
        if a == 'B':
            score += 6 if b == 'Z' else 0
        if a == 'C':
            score += 6 if b == 'X' else 0
    score += score_dict[b]
print(f'Final score for rule 1: {score}')

# part 2
score = 0
result_list = [1, 2, 3]
for play in open('input.txt').readlines():
    a, b = play.split()
    if a == 'A':
        score += result_list[(score_dict[b] + 1) % 3]
    if a == 'B':
        score += result_list[score_dict[b] - 1]
    if a == 'C':
        score += result_list[(score_dict[b] % 3)]
    score += (score_dict[b] - 1)*3
    print(score)
print(f'Final score for rule 2: {score}')
