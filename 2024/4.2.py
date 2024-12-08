import numpy as np

with open("4.txt") as fh:
    grid = fh.read().split('\n')

grid = np.array([list(x) for x in grid])


count = 0
for y in range(grid.shape[0]-2):
    for x in range(grid.shape[1]-2):

        diagonal = np.diag(grid[y:y+3, x:x+3])
        anti_diagonal = np.flipud(grid[y:y+3, x:x+3]).diagonal()

        diagonal = ''.join(diagonal)
        anti_diagonal = ''.join(anti_diagonal)

        if diagonal in ("MAS", "SAM") and anti_diagonal in ("MAS", "SAM"):
            count += 1

print(count) # part 2: 1950
