import numpy as np


with open('15.txt') as fh:
    content = fh.read().split('\n')

m = len(content)
n = len(content[0])
grid = np.zeros((m,n), dtype = int)
for y in range(m):
    for x in range(n):
        grid[y,x] = int(content[y][x])


def getneighbors(x:int, m = m, n = n):
    # gets neighbors of x (grid is m X n)
    N = [] # neighbors
    left = True if x%n == 0 else False
    right = True if x%n == n-1 else False
    up = True if x < n else False
    down = True if x >= (n-1)*m else False

    if not left: N.append(x-1)
    if not right: N.append(x+1)
    if not up: N.append(x-n)
    if not down: N.append(x+n)

    return N


V = np.arange(m*n)
# print(V.reshape((m,n)))
E = {}
for v in V:
    for neigh in getneighbors(v, m, n):
        # print(neigh//n, neigh%n)
        E[v, neigh] = grid[neigh//n, neigh%n]


def dijkstra(start, end, V = V, E = E):
    # not very efficient implementation
    n = len(V) # number of vertices
    dist = np.full(n, np.inf)
    dist[start] = 0

    Q = list(V.copy())

    while end in Q:
        mindist = min(dist[Q])
        for x in Q:
            if dist[x] == mindist:
                u = x
                break

        Q.remove(u)

        for v in getneighbors(u):
            if v in Q:
                alt = dist[u] + E[u,v]
                if alt < dist[v]:
                    dist[v] = alt

    return dist[end]


print(dijkstra(0,m*n -1, V, E)) # 472
