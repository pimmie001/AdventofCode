with open('21.txt') as fh:
    grid = fh.read().split('\n')

n = len(grid)
m = len(grid[0])

for x in range(m):
    for y in range(n):
        if grid[y][x] == 'S':
            S_coor = (x,y)


k = 64
current = set([S_coor])
for _ in range(k):
    new = set()
    for (x,y) in current:
        for (dx,dy) in [(0,1), (0,-1), (1,0), (-1,0)]:
            x2, y2 = x+dx, y+dy
            if x2 < 0 or x2 >=m or y2 < 0 or y2 >= n:
                continue
            if grid[y2][x2] != '#':
                new.add((x2,y2))
    current = new

print(len(current)) # part 1: 3660
