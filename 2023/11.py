with open('11.txt') as fh:
    grid = fh.read().split('\n')
    grid2 = grid.copy() # for part 2

n = len(grid)
m = len(grid[0])


def printgrid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end='', sep='')
        print()


## expand universe
# 1. get x and y coordinates that should be expanded
x_expand = []
for x in range(m):
    expand = True
    for y in range(n):
        if grid[y][x] == '#':
            expand = False
            break
    if expand:
        x_expand.append(x)

y_expand = []
for y in range(n):
    expand = True
    for x in range(m):
        if grid[y][x] == '#':
            expand = False
            break
    if expand:
        y_expand.append(y)

# 2. expand y coordinates
for y in reversed(y_expand):
    grid.insert(y, '.'*m)
n += len(y_expand)

# 3. expand x coordinates
for x in reversed(x_expand):
    for y in range(n):
        grid[y] = grid[y][:x] + '.' + grid[y][x:]
m += len(x_expand)


## get coordinates
coors = []
for y in range(n):
    for x in range(m):
        if grid[y][x] == '#':
            coors.append((x,y))


## sum distance of all pairs
total = 0
for i in range(len(coors)):
    x1,y1 = coors[i]
    for j in range(i+1, len(coors)):
        x2,y2 = coors[j]
        total += abs(x1-x2) + abs(y1-y2)
print(total) # part 1: 9329143


##### part 2
x_expand = set(x_expand)
y_expand = set(y_expand)

def get_distance(x1,y1,x2,y2, M=1_000_000):
    xsmall = min(x1,x2)
    xlarge = max(x1,x2)
    ysmall = min(y1,y2)
    ylarge = max(y1,y2)

    dist = 0
    for x in range(xsmall+1, xlarge+1):
        if x in x_expand:
            dist += M
        else: 
            dist += 1
    for y in range(ysmall+1, ylarge+1):
        if y in y_expand:
            dist += M
        else:
            dist += 1

    return dist


## get coordinates on standard grid
n = len(grid2)
m = len(grid2[0])
coors2 = []
for y in range(n):
    for x in range(m):
        if grid2[y][x] == '#':
            coors2.append((x,y))

## sum distance of all pairs
total = 0
for i in range(len(coors2)):
    x1,y1 = coors2[i]
    for j in range(i+1, len(coors2)):
        x2,y2 = coors2[j]
        total += get_distance(x1,y1,x2,y2)
print(total) # part 2: 710674907809
