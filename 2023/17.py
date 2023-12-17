import heapq 

with open('17.txt') as fh:
    grid = fh.read().split('\n')

n = len(grid)
m = len(grid[0])


def get_dxdy(dir, length):
    # given a direction and length (nr of steps), return dx and dy

    if dir == '>':
        return (length,0)
    elif dir == 'v':
        return (0,length)
    elif dir == '<':
        return (-length,0)
    elif dir == '^':
        return (0,-length)



class node:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.dist = int(grid[y][x])


    def get_neighbors(self, length_range):
        self.neighbors = [] # list of neighbor, distance to neighbor

        if self.dir == '>':
            allowed_dirs = ['^', 'v']
        elif self.dir == 'v':
            allowed_dirs = ['<', '>']
        elif self.dir == '<':
            allowed_dirs = ['v', '^']
        elif self.dir == '^':
            allowed_dirs = ['>', '<']
        else: # if dir is None
            allowed_dirs = ['>', '<', 'v', '^']

        for length in length_range:
            for dir in allowed_dirs:
                dx,dy = get_dxdy(dir, length)
                if self.x+dx < 0 or self.y+dy < 0 or self.x+dx >= m or self.y+dy >= n:
                    continue

                neighbor = node_dict[(self.x+dx,self.y+dy,dir)]
                distance = 0
                for l in range(1, length+1):
                    dx_,dy_ = get_dxdy(dir, l)
                    distance += int(grid[self.y+dy_][self.x+dx_])

                self.neighbors.append((neighbor,distance))


    def __lt__(self, other):
        return self.dist < other.dist


def dijkstra(nodes, start):
    # dijkstra shortest path algorithm

    distances = {node: float('inf') for node in nodes}
    distances[start] = 0

    priority_queue = [(0, start)]
    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue) # special heap structure for speed

        if current_dist > distances[current_node]:
            continue

        for neighbor, edge_weight in current_node.neighbors:
            distance = distances[current_node] + edge_weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


### 1. create nodes
nodes = []
node_dict = {}
i = 0
for x in range(m):
    for y in range(n):
        for dir in ['<', 'v', '>', '^']:

            v = node(x,y,dir)
            nodes.append(v)
            node_dict[(x,y,dir)] = v
            i += 1

# special start node with direction None
v = node(0,0,None)
nodes.append(v)
node_dict[(0,0,None)] = v


### 2. add neighbors to nodes
for v in nodes: #! choose here which length_range to use:
    # v.get_neighbors(length_range = range(1,4)) # part 1
    v.get_neighbors(length_range = range(4,11)) # part 2


### 3. run dijkstra algorithm and find minimum length to endpoint (m-1,n-1)
start = node_dict[(0,0,None)]
distances = dijkstra(nodes, start) # contains distances from start to every node

minimum = float('inf')
for dir in ['<', 'v', '>', '^']: # end state of direction doesnt matter, so take the minimum
    minimum = min(distances[node_dict[(m-1,n-1,dir)]], minimum)

print(minimum) 
# part 1: 684
# part 2: 822