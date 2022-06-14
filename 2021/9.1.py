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

count = 0
for y in range(m):
    for x in range(n):
        dumdum = True
        for i in range(-1,2): 
            for j in range(-1,2):
                if (y+i) in range(m) and (x+j) in range(n) and abs(i) + abs(j) != 0: 
                    if grid[y,x] >= grid[y+i, x+j]: dumdum = False
        if dumdum:
            count += 1 + grid[y,x]

print(count) # 554
