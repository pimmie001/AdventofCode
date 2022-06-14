import numpy as np

with open('20.txt') as f:
    content = f.read().split('\n\n')
string = content[0]
g = content[1].split('\n')

m = len(g)
n = len(g[0])

grid = []
for y in range(m):
    a = []
    for x in range(n):
        a.append(g[y][x])
    grid.append(a)
grid = np.array(grid)
grid2 = np.copy(grid)


def extend(grid):
    m = len(grid)
    n = len(grid[0])

    grid2 = []
    a = []
    for i in range(n+2):
        a.append('.')
    grid2.append(a)
    for y in range(m):
        a = ['.']
        for x in range(n):
            a.append(grid[y][x])
        a.append('.')
        grid2.append(a)
    a = []
    for i in range(n+2):
        a.append('.')
    grid2.append(a)

    grid2 = np.array(grid2)

    return grid2


def step(grid):
    m1 = len(grid)
    n1 = len(grid[0])

    grid2 = np.copy(grid)

    for y in range(1, m1-1):
        for x in range(1, n1-1):
            a = ''
            for i in range(-1,2):
                for j in range(-1,2):
                    a += grid[y+i,x+j]

            n = int(a.replace('.','0').replace('#','1'), 2)
            if string[n] == '#':
                grid2[y,x] = '#'
            else:
                grid2[y,x] = '.'

    return grid2


# make sure it is big enough
l = 5
for i in range(l):
    grid = extend(grid)

k = 2
for i in range(k):
    grid = step(grid)
    if i != k: # extend each time except last
        grid = extend(grid)


# stupid thing to make sure you dont count the borders because these are fucked up (because string[0] = #)
total = 0
for y in range(l, len(grid) - l):
    for x in range(l, len(grid[0]) - l):
        if grid[y,x] == '#':
            total += 1

print(total) # 5597
