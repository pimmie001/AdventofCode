import numpy as np

with open('test.txt') as f:
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

def step(grid, iter):
    m1 = len(grid)
    n1 = len(grid[0])

    grid2 = np.copy(grid)

    for y in range(m1):
        for x in range(n1):
            if x > 0 and x < n1-1 and y > 0 and y < m1-1:
                a = ''
                for i in range(-1,2):
                    for j in range(-1,2):
                        a += grid[y+i,x+j]

                n = int(a.replace('.','0').replace('#','1'), 2)
                if string[n] == '#':
                    grid2[y,x] = '#'
                else:
                    grid2[y,x] = '.'

            else:
                if iter % 2 == 1:
                    grid2[y,x] = string[0]
                else:
                    grid2[y,x] = string[-1]

    return grid2


k = 50
l = 5

# the function is modified a bit to change the borders of the grid, to make this work we have to extend first and then do the steps
for i in range(k+l):
    grid = extend(grid)
for i in range(1, k + 1):
    grid = step(grid, i)



# can now loop over all as the corners are fixed by the function
total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y,x] == '#':
            total += 1

print(total) # 18723