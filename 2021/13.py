import numpy as np

### setup grid
with open('13.txt') as fh:
    content = fh.read().split("\n\n")
    points2 = content[0].split('\n')
    instructions = content[1].split('\n')

points = []
for p in points2:
    y = p.split(',')
    points.append([int(y[0]), int(y[1])])

def getmaxcoordinates(points):
    a = []
    b = []
    for x in points:
        a.append(x[0])
        b.append(x[1])
    return max(a) + 1, max(b) + 1

m,n = getmaxcoordinates(points)
grid = np.empty((n,m), dtype = str)
for y in range(len(grid)):
    for x in range(len(grid[0])):
        grid[y,x] = '.'
for coor in points:
    grid[coor[1], coor[0]] = '#'

### part 1
def verticalfold(grid):
    m,n = np.shape(grid)
    n2 = n//2
    newgrid = np.empty((m,n2), dtype = str)

    for y in range(len(newgrid)):
        for x in range(len(newgrid[0])):
            if grid[y,x] == '#' or grid[y,n-1-x] == '#':
                newgrid[y,x] = '#'
            else:
                newgrid[y,x] = '.'
    
    return newgrid

def horizontalfold(grid): # very similiar as verticalfold
    m,n = np.shape(grid)
    m2 = m//2
    newgrid = np.empty((m2,n), dtype = str)

    for y in range(len(newgrid)):
        for x in range(len(newgrid[0])):
            if grid[y,x] == '#' or grid[m-1-y,x] == '#':
                newgrid[y,x] = '#'
            else:
                newgrid[y,x] = '.'
    
    return newgrid

def counthash(grid):
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y,x] == '#':
                result += 1
    return result

if 'x' in instructions[0]:
    grid1 = verticalfold(grid)
elif 'y' in instructions[0]:
    grid1 = horizontalfold(grid)
print(f'Part 1: {counthash(grid1)}\n') # 678

### part 2
newgrid = np.copy(grid)
for instruction in instructions:
    if 'x' in instruction:
        newgrid = verticalfold(newgrid)
    elif 'y' in instruction:
        newgrid = horizontalfold(newgrid)

print("Par 2:\n")
for arr in newgrid:
    string = ''
    for x in arr:
        if x == '#':
            string += x + ' '
        else:
            string += '  '
    print(string)
# ECFHLHZF
