import numpy as np

with open("4.txt") as fh:
    grid = fh.read().split('\n')


## add layers of 0's so we dont get index out of bound errors
A = [list('000'+x+'000') for x in grid]
for _ in range(3):
    A.insert(0, ['0']*len(A[0]))
    A.append(['0']*len(A[0]))


grid = np.array([list(x) for x in A])


count = 0
for y in range(3, grid.shape[0]-3):
    for x in range(3, grid.shape[1]-3):

        diagonal = np.diag(grid[y:y+3, x:x+3])
        anti_diagonal = np.flipud(grid[y:y+3, x:x+3]).diagonal()

        diagonal = ''.join(diagonal)
        anti_diagonal = ''.join(anti_diagonal)

        if diagonal in ("MAS", "SAM") and anti_diagonal in ("MAS", "SAM"):
            count += 1

print(count) # part 2: 1950
