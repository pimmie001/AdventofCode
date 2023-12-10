with open('10.txt') as fh:
    content = fh.read().split('\n')

n = len(content)
m = len(content[0])

pipes = {} # dictionary (x,y): pipe type
for y in range(n):
    for x in range(m):
        if content[y][x] == 'S':
            S_coor = (x,y)
        pipes[(x,y)] = content[y][x]


def find_adj_pipes(x, y, visited):
    """input: pipe (eg L or J), and x and y coordinate of pipe. 
    Returns adjacent pipes that match"""

    # allowed dx,dy changes given a pipe:
    allowed = {'|': [(0,1), (0,-1)], '-': [(1,0), (-1,0)], 'L': [(1,0), (0,-1)], 'F': [(1,0), (0,1)], '7': [(-1,0), (0,1)], 'J': [(-1,0), (0,-1)], 'S': [(1,0), (-1,0), (0,1), (0,-1)]} 

    adjacent = []
    for dx,dy in allowed[pipes[(x,y)]]:
        if (x+dx, y+dy) in visited or x+dx < 0 or y+dy < 0 or x+dx >= m or y+dy >=n:
            continue

        if (dx,dy) == (1,0):
            if pipes[(x+dx, y+dy)] in ['7', 'J', '-']:
                adjacent.append((x+dx, y+dy))
        elif (dx,dy) == (-1,0):
            if pipes[(x+dx, y+dy)] in ['L', 'F', '-']:
                adjacent.append((x+dx, y+dy))
        elif (dx,dy) == (0,1):
            if pipes[(x+dx, y+dy)] in ['L', 'J', '|']:
                adjacent.append((x+dx, y+dy))
        elif (dx,dy) == (0,-1):
            if pipes[(x+dx, y+dy)] in ['7', 'F', '|']:
                adjacent.append((x+dx, y+dy))

    return adjacent


## loop until no adjacent pipes can be added to loop
all_pipes = [[S_coor]]
visited = set([S_coor])
while all_pipes[-1]:
    new_pipes = []
    for (x,y) in all_pipes[-1]:
        adjacent = find_adj_pipes(x, y, visited)
        new_pipes.extend(adjacent)
        for elem in adjacent:
            visited.add(elem)
    all_pipes.append(new_pipes)


print(len(all_pipes) - 2) # first one is ['S'] and last one is empty list so these two dont count
# part 1: 7063

