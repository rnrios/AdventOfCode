import numpy as np
from queue import PriorityQueue
INF = np.inf
 
# Djikstra implementation taken from: https://www.geeksforgeeks.org/
# shortest-paths-from-all-vertices-to-a-destination/
class Graph:
    def __init__(self, V: int) -> None:
 
        self.V = V

        self.adj = [[] for _ in range(V)]
    def addEdgeRev(self, u: int, v: int, w: int) -> None:
        self.adj[v].append((u, w))
 
    def shortestPath(self, dest: int) -> None:
        pq = PriorityQueue()
        
        dist = [INF for _ in range(self.V)]
 
        pq.put((0, dest))
        dist[dest] = 0
 
        while not pq.empty():
            u = pq.get()[1]
            for i in self.adj[u]: 
                v = i[0]
                weight = i[1]
                if (dist[v] > dist[u] + weight):      
                    dist[v] = dist[u] + weight
                    pq.put((dist[v], v))

        print("Destination Vertex Distance from all vertex")
        for i in range(self.V):
            if i==0:
                print("{} \t\t {}".format(i, dist[i]))

def preproc(filename):
    f = open(filename, 'r').read().splitlines()
    array = np.array([[int(x) for x in line] for line in f])
    return array


def create_list(arr):
    flattened_arr = arr.ravel()
    N = flattened_arr.shape[0]
    num_rows, num_cols = arr.shape[0], arr.shape[1]
    adj_list = []
    for i in range(num_rows):
        for j in range(num_cols):
            if i-1>=0:
                adj_list.append((i*num_cols+j, (i-1)*num_cols+j, arr[i-1][j]))
            if j-1>=0:
                adj_list.append((i*num_cols+j, i*num_cols+j-1, arr[i][j-1]))
            if i+1<num_cols:
                adj_list.append((i*num_cols+j, (i+1)*num_cols+j, arr[i+1][j]))
            if j+1<num_cols:
                adj_list.append((i*num_cols+j, i*num_cols+j+1, arr[i][j+1]))
    return adj_list, N


def main():
    arr = preproc('input.txt')
    adj_list, N = create_list(arr)
    graph = Graph(N)
    for x in adj_list:
        graph.addEdgeRev(x[0], x[1], x[2])
    graph.shortestPath(N-1)
    
    
if __name__ == '__main__':
    main()