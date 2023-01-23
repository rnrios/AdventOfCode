import numpy as np


class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = np.inf
 
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [np.inf] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]
 
        self.printSolution(dist)


def preproc(filename):
    f = open(filename, 'r').read().splitlines()
    array = np.array([[int(x) for x in line] for line in f])
    return array


def create_array(arr):
    flattened_arr = arr.ravel()
    N = flattened_arr.shape[0]
    weights = np.zeros((N, N))
    num_rows, num_cols = arr.shape[0], arr.shape[1]
    for i in range(num_rows):
        for j in range(num_cols):
            if i-1>=0:
                weights[i*num_cols+j][(i-1)*num_cols+j] = arr[i-1][j]
            if j-1>=0:
                weights[i*num_cols+j][i*num_cols+j-1] = arr[i][j-1]
            if i+1<10:
                weights[i*num_cols+j][(i+1)*num_cols+j] = arr[i+1][j]
            if j+1<10:
                weights[i*num_cols+j][i*num_cols+j+1] = arr[i][j+1]
    return weights, N

def main():
    arr = preproc('input.txt')
    weights, N = create_array(arr)
    g = Graph(N)
    g.graph = weights
    g.dijkstra(0)
    

        
if __name__ == '__main__':
    main()