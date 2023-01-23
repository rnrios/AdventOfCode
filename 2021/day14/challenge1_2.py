import numpy as np


def preproc(filename):
    f = open(filename, 'r').read().splitlines()
    rules = []
    for i, line in enumerate(f): 
        if i==0:
            template = line
        elif i!=1:
            rules.append(line.split(' -> '))
    rules_dict = {}
    position_dict = {}
    
    for i, rule in enumerate(rules):
        rules_dict[rule[0]] = i
        position_dict[i] = [rule[0], rule[1]]
    
    rule_counts= np.zeros(len(rules_dict))
    for i in range(0,len(template)-1):
        char = template[i:i+2]
        rule_counts[rules_dict[char]] = 1

    char_count = {}
    for output in template:
        if output not in char_count:
            char_count[output] = 1
        else:
            char_count[output] += 1
    return [rules_dict, position_dict, rule_counts, char_count]


def value_counts(rules_dict, position_dict, rule_counts, char_count, N):
    for i in range(N):
        rule_counts_temp = np.zeros(rule_counts.shape)
        for idx in np.squeeze(np.argwhere(rule_counts!=0)):      
            curr_char = position_dict[idx][1]
            prev_char = position_dict[idx][0][0]
            next_char = position_dict[idx][0][1]
            if curr_char not in char_count:
                char_count[curr_char] = rule_counts[idx]
            else:
                char_count[curr_char] += rule_counts[idx]
            rule_counts_temp[rules_dict[prev_char+curr_char]] += rule_counts[idx]
            rule_counts_temp[rules_dict[curr_char+next_char]] += rule_counts[idx]
            rule_counts[idx] -= rule_counts[idx]

        rule_counts = rule_counts_temp
    return char_count.values()


def main():
    
    data = preproc('input.txt')
    counts = value_counts(*data, 40)
    max_val, min_val = max(counts), min(counts)
    print(max_val-min_val)
            

if __name__ == '__main__':
    main()
