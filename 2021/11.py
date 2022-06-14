import numpy as np

with open('11.txt') as fh:
    content = fh.read().split("\n")
m = len(content)
n = len(content[0])
input = np.zeros((m,n), dtype = int)
for y in range(m):
    for x in range(n):
        input[y,x] = content[y][x]



def findneighbors(grid, y, x):
    m = len(grid)
    n = len(grid[0])
    xcoor = []
    ycoor = []

    for i in range(-1,2):
        for j in range(-1,2):
            if i + x in range(n) and j + y in range(m) and abs(i) + abs(j) != 0:
                xcoor.append(i+x)
                ycoor.append(j+y)
    return [ycoor, xcoor]


def step(input):
    result = np.copy(input)
    result += 1

    allx =[]
    ally = []

    flashcount = 0
    while np.size(np.where(result >= 10)) > 0:
        ind = np.where(result >= 10) 
        yinds, xinds = ind

        flashcount += len(yinds)
        for k in range(len(yinds)): 
            ally.append(yinds[k])
            allx.append(xinds[k])
            neigh = findneighbors(input, yinds[k], xinds[k])
            result[neigh] += 1

        result[ally, allx] = 0 # flashed lights can not increase this step

    return result, flashcount


grid = np.copy(input)
steps = 100

flashcount = 0
for it in range(steps):
    nextstep = step(grid)
    grid = nextstep[0]
    flashcount += nextstep[1]
print(f'part 1: {flashcount}\n') # part 1: 1700 


### part 2:
grid = np.copy(input)

i = 1
while True:
    nextstep = step(grid)
    if nextstep[1] == n*m:
        print(f'part 2: {i}')
        break
    grid = nextstep[0]
    i += 1
# 273