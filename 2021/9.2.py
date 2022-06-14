import numpy as np

with open('9.txt') as fh:
    content = fh.read().split('\n')
grid = []
for line in content: 
    y = []
    for x in line:
        y.append(x)
    grid.append(y)

grid = np.array(grid, dtype = int)
m, n = np.shape(grid)

grid = (grid != 9).astype(int) - 1
# - 1 is the 9's and 0 is everything else


all_locations = []
for x in range(n):
    for y in range(m):
        if grid[y,x] != -1:
            all_locations.append((y,x))


def getunique(A):
    B = []
    for x in A:
        if x not in B:
            B.append(x)
    return B

def getneighbors(grid, y, x):
    N = []
    m, n = np.shape(grid)
    for i, j in [(1,0), (-1,0), (0,1), (0,-1)]:
        if x+i in range(n) and y+j in range(m):
            if grid[y+j, x+i] != -1:
                N.append((y+j, x + i))
    return N

def increasebasin(grid, base):
    base2 = base.copy()

    for y,x in base:
        N = getneighbors(grid, y, x)
        base2.extend(N)
    base2 = getunique(base2)
    
    return base2

def getbasin(grid, base):
    oldbase = base.copy()
    while True:
        newbase = increasebasin(grid, oldbase)
        if oldbase == newbase: 
            return oldbase
        oldbase = newbase.copy()


location_tocheck = all_locations.copy()

sizes = []
while not location_tocheck == []:
    startpoint = [location_tocheck[0]]
    basin = getbasin(grid, startpoint)
    sizes.append(len(basin))
    for location in basin:
        location_tocheck.remove(location)

sizes.sort()
print(np.prod(sizes[-3:])) # 1017792
