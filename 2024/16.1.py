with open('16.txt') as fh:
    grid = fh.read().split('\n')

nodes = set()
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'S':
            start = x,y
        if grid[y][x] == 'E':
            end = x,y

        if grid[y][x] != '#':
            for dir in range(4):
                nodes.add((x,y,dir)) # (x,y,dir) is a node used in Dijkstra's algorithm


def distance(a, b):
    """"Returns distance between node a and b. is inf if arc (a,b) doesnt exist"""
    x1,y1,dir1 = a 
    x2,y2,dir2 = b


    if abs(x1 - x2) > 1 or  abs(y1 - y2) > 1:
        return float('inf')

    ## move 90 degrees
    if abs(dir1 - dir2) in (1, 3) and abs(x1 - x2) + abs(y1 - y2) == 0:
        return 1000

    ## make step forward
    if dir1 == dir2:
        dx,dy = {0: (0,-1), 1: (1,0), 2: (0,1), 3: (-1,0)}[dir1]
        if x1+dx == x2 and y1+dy == y2: # can only move in current direction
            return 1

    return float('inf')


def get_neighbors(a):
    x,y,dir = a
    neighbors = [(x,y,(dir+1)%4), (x,y,(dir-1)%4)]
    dx,dy = {0: (0,-1), 1: (1,0), 2: (0,1), 3: (-1,0)}[dir]
    if grid[y+dy][x+dx] != '#': neighbors.append((x+dx,y+dy,dir))
    return neighbors


A = {} # set of arcs
for a in nodes:
    for b in get_neighbors(a):
        d = distance(a, b)
        if d!= float('inf'):
            if a in A:
                A[a].append((b,d)) # neighbor, distance to neighbor
            else:
                A[a] = [(b, d)]


## Dijkstra algorithm
dist = {}
for x in nodes:
    dist[x] = float('inf')
dist[(start)+(1,)] = 0 # current direction is 1 (0 north, 1 east, 2 south, 3 west)

unvisited = nodes.copy()
while unvisited:
    u = min(unvisited, key=lambda x: dist[x])
    unvisited.remove(u)

    for (v, d) in A[u]: # v is neighbor of u
        if v in unvisited:
            alt = dist[u] + d
            if alt < dist[v]:
                dist[v] = alt

print(min([dist[(end)+(dir,)] for dir in range(4)])) # part 1: 66404
