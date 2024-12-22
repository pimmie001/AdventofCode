import heapq

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



## create graph for dijkstra function
graph = {}
for node in nodes:
    graph[node] = {}

    for neighbor in get_neighbors(node):
        graph[node][neighbor] = distance(node, neighbor)



def dijkstra(graph, start):
    """More efficient Dijkstra function using priority queue"""

    # Initialize the distance
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store (distance, node)
    pq = [(0, start)] # (distance to start node, start node)

    while pq:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)

        # If this distance is greater than the already found distance: continue
        if current_distance > distances[current_node]:
            continue

        # Explore the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


distances = dijkstra(graph, start=(start)+(1,))
shortest_distance = min([distances[(end)+(dir,)] for dir in range(4)])
print(shortest_distance) # part 1: 66404


### output of dijkstra is a dictionary with key a node and value distance from starting point. 
### We now need to do this for every starting point.
all_distances = {}
for node in nodes:
    distances = dijkstra(graph, start=node)
    all_distances[node] = distances


# for each node, check if distance from start_node to node + node to end_node is the shortest distance
locations = set()
for node in nodes:
    x,y,_ = node

    if min([all_distances[(start)+(1,)][node] + all_distances[node][(end)+(dir,)] for dir in range(4)]) == shortest_distance:
        locations.add((x,y))

print(len(locations)) # part 2: 433
