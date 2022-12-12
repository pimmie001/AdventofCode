import numpy as np
import string


alf = string.ascii_lowercase
index = {}
for i in range(len(alf)):
    index[alf[i]] = i
index['S'] = 0
index['E'] = 25

with open('12.txt') as fh:
    map = fh.read().split('\n')
n, m = len(map), len(map[0])


# find start/end point
for y in range(n):
    for x in range(m):
        if map[y][x] == 'S':
            start = x,y

        if map[y][x] == 'E':
            end = x,y


def smallest_so_far(dist, visited):
    # returns the key and value of the smallest distance so far
    d = float('inf')
    for u in dist:
        if u in visited:
            continue
        if dist[u] <= d:
            v = u
            d = dist[u]
    return v, d


def dijkstra(end):
    # dijkstra algorithm finds the shortest path from every point to end

    dist = {}
    for y in range(n):
        for x in range(m):
            dist[x,y] = float('inf')
    dist[end] = 0

    visited = set()
    while len(visited) < m*n:
        u, dist_u = smallest_so_far(dist, visited)

        visited.add(u)

        x,y = u
        current_height = index[map[y][x]]

        neighbors = []
        if x > 0 and index[map[y][x-1]] >= current_height - 1:
            neighbors.append((x-1, y))
        if x < m-1 and index[map[y][x+1]] >= current_height - 1:
            neighbors.append((x+1,y))
        if y > 0 and index[map[y-1][x]] >= current_height - 1:
            neighbors.append((x,y-1))
        if y < n-1 and index[map[y+1][x]] >= current_height - 1:
            neighbors.append((x,y+1))

        for neighbor in neighbors:
            dist[neighbor] = min(dist[neighbor], dist_u + 1)

    return dist

dist = dijkstra(end)
print(dist[start]) # part 1: 350


### part 2:
all_shortest_pahts = [dist[start]]
for y in range(n):
    for x in range(m):
        if map[y][x] == 'a':
            all_shortest_pahts.append(dist[x,y])
print(min(all_shortest_pahts)) # part 2: 349
