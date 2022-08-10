import numpy as np
from collections import Counter

visited = []
def create_tree(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:      
        if node in path and node.islower():
            lower_counts = [x for x in path if x.islower()]
            if max(Counter(lower_counts).values()) == 2 or node=='start':
                continue
        newpaths = create_tree(graph, node, end, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths  


def append_to_dict(conn_dict, key, val):
    if key in conn_dict.keys():
            conn_dict[key].append(val)
    else:
        conn_dict[key] = [val]
    return conn_dict


def main():
    visited = []
    f = open('input.txt', 'r').read().splitlines()
    lines = [x.split('-') for x in f]
    conn_dict = {}
    for line in lines:
        conn_dict = append_to_dict(conn_dict, line[0], line[1])
        conn_dict = append_to_dict(conn_dict, line[1], line[0])
    paths = create_tree(conn_dict, 'start', 'end')
    print(len(paths))

   
if __name__ == '__main__':
    main()