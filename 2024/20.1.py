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


def cheat_score(s, e):
    """
    Given s and e (start and end coordinates of cheat location), returns number of saved seconds by using cheat
    Note that start and end have a manhattan distance of 2
    """

    if not (0 <= e[0] < n and 0 <= e[1] < m): # out of grid
        return -1

    if grid[e[1]][e[0]] == '#': # cheat not allowed
        return -1

    return distances[s] - distances[e] - 2


score_list = {}
for (x,y) in race_track:
        if (x,y) == (9,7):
            kjsldfs = 3
        for (dx,dy) in [(1,1), (1,-1), (-1,1), (-1,-1), (2,0), (-2,0), (0,2), (0,-2)]:
            s = (x,y)
            e = s[0]+dx, s[1]+dy
            score_list[s, e] = cheat_score(s, e)

print(sum(1 for x in score_list.values() if x >= 100)) # part 1: 1448
