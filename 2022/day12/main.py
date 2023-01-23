def preprocess():
    start_node = end_node = None
    nodes_grid = []
    for i, line in enumerate(open('input.txt').readlines()):
        if line == '\n':
            continue
        nodes_grid.append(line[:-1])
        if 'S' in line:
            idx = line[:-1].index('S')
            start_node = (i, idx)
            nodes_grid[i] = nodes_grid[i][:idx] + 'a' + nodes_grid[i][idx+1:]
        if 'E' in line:
            idx = line[:-1].index('E')
            end_node = (i, idx)
            nodes_grid[i] = nodes_grid[i][:idx] + 'z' + nodes_grid[i][idx+1:]
    m, n = len(nodes_grid), len(nodes_grid[0])
    return m, n, nodes_grid, start_node, end_node


def search_neighbors(pos, next_layer_nodes, queue, grid, visited, m, n, back=False):
    r_idx = [-1, 0, 1, 0]
    c_idx = [0, 1, 0, -1]
    r, c = pos[0], pos[1]
    for i in range(4):
        pos = (r + r_idx[i], c + c_idx[i])
        if pos[0] < 0 or pos[0] >= m or pos[1] < 0 or pos[1] >= n:
            continue
        if pos in visited:
            continue
        if not back:
            if ord(grid[pos[0]][pos[1]]) - ord(grid[r][c]) > 1:
                continue
        else:
            if ord(grid[pos[0]][pos[1]]) - ord(grid[r][c]) < -1:
                continue
        queue.append(pos)
        visited.add(pos)
        next_layer_nodes += 1
    return next_layer_nodes


def bfs(back=False):
    m, n, grid, start, end = preprocess()
    queue, visited = [], set()
    this_layer_nodes = 1
    next_layer_nodes = 0
    count = 0
    is_end = False
    if back:
        start, end = end, start
    queue.append(start)
    visited.add(start)
    while len(queue) > 0:
        pos = queue.pop(0)
        if not back:
            if pos == end:
                is_end = True
                break
        else:
            if grid[pos[0]][pos[1]] == 'a':
                is_end = True
                break
        next_layer_nodes = search_neighbors(pos, next_layer_nodes, queue, grid, visited, m, n, back)
        this_layer_nodes -= 1
        if not this_layer_nodes:
            this_layer_nodes = next_layer_nodes
            next_layer_nodes = 0
            count += 1
    if is_end:
        return count
print(f'Part 1: {bfs()}')
print(f'Part 2: {bfs(True)}')