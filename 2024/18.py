import heapq

with open('18.txt') as fh:
    coordinates = fh.read().split('\n')

memory_space = set()
for i in range(1024):
    a,b = coordinates[i].split(',')
    memory_space.add((int(a), int(b)))

n = 71


def get_neighbors(x,y, memory_space=memory_space):
    neighbors = []
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in memory_space:
            neighbors.append((nx, ny))
    return neighbors


def dijkstra(memory_space):
    dist = {(x,y): float('inf') for x in range(n) for y in range(n)}
    dist[0,0] = 0

    pq = [(0, (0,0))] # priority queue: distance, coordinates

    while pq:
        current_distance, (x,y) = heapq.heappop(pq) # Pop the node with the smallest distance

        if current_distance > dist[x,y]: # continue if better distance already found
            continue

        # Explore the neighbors of the current node
        for neighbor in get_neighbors(x,y,memory_space=memory_space):
            alt = current_distance + 1

            if alt < dist[neighbor]:
                dist[neighbor] = alt
                heapq.heappush(pq, (alt, neighbor))

    return dist

print(dijkstra(memory_space)[n-1, n-1]) # part 1: 320


### part 2
memory_space = set()
for i in range(len(coordinates)):
    a,b = coordinates[i].split(',')
    a,b = int(a),int(b)
    memory_space.add((a,b))

    if dijkstra(memory_space)[n-1, n-1] == float('inf'):
        print(f'{a},{b}') # part 2: 
        break
