import re
from collections import defaultdict


def get_size(nodes_list, files_size):
    acc = 0
    if not nodes_list:
        return files_size
    else:
        for node in nodes_list:
            acc += get_size(dir_dict[node], file_dict[node])
    return acc + files_size


cur_dir, prev_dict = None, {'/': ''}
dir_dict = defaultdict(list)
file_dict = defaultdict(int)
for line in open('input.txt').readlines():
    if line[0] == '$':
        if 'cd' in line:
            if '..' in line:
                cur_dir = prev_dict[cur_dir]
            else:
                cur_dir = cur_dir + '/' + line[5:-1] if cur_dir else '/'
    else:
        if 'dir' in line:
            dir_name = line[4:-1]
            prev_dict[cur_dir + '/' + dir_name] = cur_dir
            dir_dict[cur_dir].append(cur_dir + '/' + dir_name)
        else:
            file_dict[cur_dir] += int(re.findall(r'\d+', line)[0])
mem_sum, MAX1, dir_size = 0, 1e5, {}
for key in prev_dict.keys():
    dir_size[key] = get_size(dir_dict[key], file_dict[key])
    if dir_size[key] < MAX1:
        mem_sum += dir_size[key]

mem_dir, MAX2 = 1e15, 3e7 - (7e7 - dir_size['/'])
list_mem = []
for key in dir_size.keys():
    list_mem.append(dir_size[key])
    if dir_size[key] >= MAX2:
        mem_dir = mem_dir if mem_dir < dir_size[key] else dir_size[key]
print(f'Part 1: {mem_sum}')
print(f'Part 2: {mem_dir}')
list_mem = sorted(list_mem)
