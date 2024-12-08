import numpy as np

with open("4.txt") as fh:
    grid = fh.read().split('\n')


## add layers of 0's so we dont get index out of bound errors
A = [list('000'+x+'000') for x in grid]
for _ in range(3):
    A.insert(0, ['0']*len(A[0]))
    A.append(['0']*len(A[0]))


grid = np.array([list(x) for x in A])


# bit hardcoded because original code didnt work
count = 0
for y in range(3, grid.shape[0]-3):
    for x in range(3, grid.shape[1]-3):
        char = grid[y][x]

        text = ""
        for dy in range(4):
            text += grid[y+dy][x]
        count += text == "XMAS" or text == "SAMX"


        text = ""
        for dx in range(4):
            text += grid[y][x+dx]
        count += text == "XMAS" or text == "SAMX"


        text = ""
        for d in range(4):
            text += grid[y+d][x+d]
        count += text == "XMAS" or text == "SAMX"


        text = ""
        for d in range(4):
            text += grid[y-d][x+d]
        count += text == "XMAS" or text == "SAMX"

print(count) # part 1: 2593
