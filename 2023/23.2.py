with open('23.txt') as fh:
    grid = fh.read().split('\n')

n = len(grid)
m = len(grid[0])

start = (1,0)
end = (m-2,n-1)

### 1. find points of interest
points_of_interest = [start] # locations where more than 2 directions can be taken (including start and end)
for x in range(1, m-1):
    for y in range(1, n-1):
        if grid[y][x] == '#':
            continue

        count = 0
        for (dx, dy) in [(0,1), (0,-1), (1,0), (-1,0)]:
            if grid[y+dy][x+dx] != '#':
                count += 1
        if count > 2:
            points_of_interest.append((x,y))

points_of_interest.append(end) # add0 'end' to interesting points
# print(len(points_of_interest)) # only 36 for own input


### find arcs and distance between all pairs of points of interests
points_of_interest_set = set(points_of_interest)

def explore(start):
    result = [] # list of neighbors, distance when starting in start

    visited = set([start])
    current = [(start, 0)] # location, distance

    while current:
        new = []
        for ((x,y), d) in current:

            for (dx,dy) in [(0,1), (0,-1), (1,0), (-1,0)]:
                x2,y2 = x+dx, y+dy

                if (x2,y2) in visited:
                    continue
                visited.add((x2,y2))

                if (x2,y2) in points_of_interest_set:
                    result.append(((x2,y2), d+1))

                elif y2 >=0 and y2 < n and grid[y2][x2] != '#':
                    new.append(((x2,y2), d+1))

        current = new

    return result

graph = {} # keys are indicies of points of interest. Values are index, length
for i,point in enumerate(points_of_interest):
    result = explore(point)

    graph[i] = []
    for neighbor, distance in result:
        j = points_of_interest.index(neighbor)
        graph[i].append((j, distance))


### find longest path
def longest_path(start, end, visited = set(), memo = {}):
    if start == end:
        return 0

    if (start, frozenset(visited)) in memo:
        return memo[(start, frozenset(visited))]


    maximum = float("-inf")
    for neighbor, distance in graph[start]:
        if neighbor in visited:
            continue

        new_visited = visited.copy()
        new_visited.add(neighbor)

        dist = distance + longest_path(neighbor, end, new_visited, memo)
        maximum = max(maximum, dist)

    memo[start, frozenset(visited)] = maximum
    return maximum


start_ind = 0
end_ind = len(points_of_interest) - 1

print(longest_path(start_ind, end_ind)) # part 2: 6630
