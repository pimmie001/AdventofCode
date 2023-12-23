with open('23.txt') as fh:
    grid = fh.read().split('\n')

n = len(grid)
m = len(grid[0])


def get_directions(x,y):
    if grid[y][x] == 'v':
        return [(0,1)]
    elif grid[y][x] == '>':
        return [(1,0)]
    elif grid[y][x] == '<':
        return [(-1,0)]
    elif grid[y][x] == '^':
        return [(0,1)]

    directions = [(0,1), (0,-1), (1,0)]
    if y > 0:
        directions.append((-1,0))
    return directions


start = (1,0)
end = (m-2,n-1)

path_lenghts = []

visited = [set()] # list of sets of visited nodes
current = [start] # list of current locations
while current:
    new = [] # new locations
    new_visited = [] # new list of sets

    for i, (x,y) in enumerate(current):
        new_vis = visited[i].copy()

        for (dx, dy) in get_directions(x,y):
            if (x+dx,y+dy) in visited[i] or y+dy < 0:
                continue
            
            if (x,y) == end:
                path_lenghts.append(len(new_vis))
                continue

            if grid[y+dy][x+dx] != '#':
                new.append((x+dx,y+dy))
                new_vis.add((x,y))
                new_visited.append(new_vis)

    current = new 
    visited = new_visited


print(max(path_lenghts)) # part 1: 2406
