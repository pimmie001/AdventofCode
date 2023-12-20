from collections import deque


with open('18.txt') as fh:
    instructions = fh.read().split('\n')


### 1. find the border
(x,y) = (0,0)
trenches = set([(0,0)])
xmin = ymin = xmax = ymax = 0

for line in instructions:
    d, n = line.split(' ')[:2]

    for _ in range(int(n)):
        if d == 'R':
            x += 1
        elif d == 'D':
            y += 1
        elif d == 'L':
            x -= 1
        else:
            y -= 1

        trenches.add((x,y))
        xmin = min(x,xmin)
        xmax = max(x,xmax)
        ymin = min(y,ymin)
        ymax = max(y,ymax)



### 2. preparations for shortest path algorithm
class node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_neighbors(self, trenches):
        # sets list of neighbors that are not in the set trenches

        self.neighbors = []
        for (dx,dy) in [(0,1), (0,-1), (1,0), (-1,0)]:
            x = self.x + dx
            y = self.y + dy
            if (x,y) not in trenches and (x,y) in node_dict:
                neighbor = node_dict[(x,y)]
                self.neighbors.append(neighbor)

    def __lt__(self, other):
        return False


def dijkstra(nodes, start):
    # dijkstra shortest path algorithm: returns distance from start to all other nodes

    distances = {node: float('inf') for node in nodes}
    distances[start] = 0

    queue = deque([start])
    while queue:
        current_node = queue.popleft()

        for neighbor in current_node.neighbors:
            distance = distances[current_node] + 1

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append(neighbor)

    return distances


# make set of nodes
nodes = []
node_dict = {}
i = 0
for x in range(xmin-1, xmax+2):
    for y in range(ymin-1, ymax+2):
        v = node(x,y)
        nodes.append(v)
        node_dict[(x,y)] = v
        i += 1

# add neighbors to nodes
for v in nodes:
    v.get_neighbors(trenches)



### 3. find distances
start = node_dict[(xmin-1,ymin-1)]
distances = dijkstra(nodes, start)

total = 0
for v in nodes:
    total += distances[v] == float('inf')
print(total) # part 1: 62500
