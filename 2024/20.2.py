with open('20.txt') as fh:
    grid = fh.read().split('\n')
m = len(grid)
n = len(grid[0])

## find start, end and all non-wall locations
race_track = set()
for y in range(m):
    for x in range(n):
        if grid[y][x] != '#':
            race_track.add((x, y))
        if grid[y][x] == 'S':
            start = x, y
        if grid[y][x] == 'E':
            end = x, y


## find distance to end
distances = {}
unvisited = race_track.copy()

current = end
dist = 0
while unvisited:
    distances[current] = dist 
    unvisited.remove(current)

    x,y = current
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+dx, y+dy
        if (nx, ny) in unvisited and (nx, ny) not in distances:
            current = nx, ny
            break # there is only one adjacent tile

    dist += 1


### some functions
def manhattan_distance(s,e):
    """Returns manhattan distance between s and e"""
    return abs(s[0]-e[0]) + abs(s[1]-e[1])


def get_endpoints(s, distance=20):
    """Given start point s, and allowed (maximum) manhattan distance, returns list of all possible end points within grid"""

    x,y = s
    end_points = []

    for dx in range(-distance, distance + 1):
        for dy in range(-distance + abs(dx), distance - abs(dx) + 1):
            if 0 <= x + dx < n and 0 <= y + dy < m: # check if within grid
                end_points.append((x + dx, y + dy))

    return end_points


def cheat_score(s, e):
    """
    Given s and e (start and end coordinates of cheat location), returns number of saved seconds by using cheat
    Note that start and end have a manhattan distance of 2
    """

    if grid[e[1]][e[0]] == '#': # cheat not allowed
        return -1

    return distances[s] - distances[e] - manhattan_distance(s, e)


### calculation
checked_cheats = set()
total = 0
i = 0
for (x,y) in race_track:
    s = (x,y)
    for e in get_endpoints(s):
        if (s,e) not in checked_cheats:
            if cheat_score(s, e) >= 100:
                total += 1
            checked_cheats.add((s,e))

print(total) # part 2: 1017615 