from collections import defaultdict, deque
from copy import deepcopy
from itertools import combinations
import sys
sys.setrecursionlimit(10_000) # might need a larger recursion limit for dfs


### prepare data
with open('25.txt') as fh:
    content = fh.read().split('\n')

# find set of nodes
nodes = set()
for line in content:
    a, neighbors = line.split(': ')
    nodes.add(a)
    for b in neighbors.split(' '):
        nodes.add(b)

# find edges
graph = {node:set() for node in nodes} # key: node, value: set of neighbors

for line in content:
    a, neighbors = line.split(': ')
    for b in neighbors.split(' '):
        graph[a].add(b)
        graph[b].add(a)


### functions for removing edges and determining if graph is disconnected
def find_nodes(graph, start):
    # starting in an arbitraty node, counts number of nodes that can be reached

    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph[current]:
            queue.append(neighbor)

    return len(visited)

def is_disconnected(graph, nodes=nodes, start='bvb'):
    # checks if graph is disconnected, return 0 if connected and product of nr of nodes if disconnected

    n = find_nodes(graph, start)
    return 0 if len(nodes) == n else n * (len(nodes) - n)

def remove_edges(graph, edges_remove):
    # given a graph and list of edges, removes these edges and returns new graph

    graph = deepcopy(graph)

    for (a,b) in edges_remove:
        graph[a].remove(b)
        graph[b].remove(a)

    return graph


##### stuff for max flow min cut algorithm

class Graph:
    def __init__(self, graph_dict):
        self.graph = defaultdict(dict)

        for node, neighbors in graph_dict.items():
            for neighbor in neighbors:
                self.graph[node][neighbor] = 1

    def max_flow_min_cut(self, source, sink):
        parent = defaultdict(lambda: -1)
        max_flow = 0

        while True:
            queue = deque()
            queue.append(source)
            parent = defaultdict(lambda: -1)
            parent[source] = source

            while queue:
                u = queue.popleft()

                for v, capacity in self.graph[u].items():
                    if parent[v] == -1 and capacity > 0:
                        parent[v] = u
                        queue.append(v)

            if parent[sink] != -1:
                path_flow = float('inf')
                s = sink

                while s != source:
                    path_flow = min(path_flow, self.graph[parent[s]][s])
                    s = parent[s]

                max_flow += path_flow

                v = sink
                while v != source:
                    u = parent[v]
                    self.graph[u][v] -= path_flow
                    self.graph[v][u] += path_flow
                    v = u

            else:
                break

        visited = set()
        self.dfs(source, visited)
        min_cut = [(u, v) for u in self.graph.keys() for v in self.graph[u] if u in visited and v not in visited]

        return max_flow, min_cut

    def dfs(self, u, visited):
        visited.add(u)
        for v in self.graph[u]:
            if v not in visited and self.graph[u][v] > 0:
                self.dfs(v, visited)


### run the max-flow min-cut algorithm until a cut of length 3 has been found

for source, sink in combinations(nodes, 2): 
    g = Graph(deepcopy(graph))

    max_flow, min_cut = g.max_flow_min_cut(source, sink)

    if max_flow == 3:
        # remove edges from the min cut and calculate nodes in each sub-graph
        new_graph = remove_edges(graph, edges_remove = min_cut)
        print(is_disconnected(new_graph)) # answer: 514794
        break