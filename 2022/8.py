import re
import numpy as np

with open('8.txt') as fh:
    input = fh.read().split('\n')


grid = np.zeros((len(input), len(input[0])), dtype=int)
for i in range(len(input)):
    line = input[i]
    y = [int(x) for x in re.findall('[0-9]', line)]
    grid[i, :] = y 


def max(A):
    if len(A) == 0:
        return -1
    return np.max(A)



total = 0
for i in range(np.shape(grid)[0]):
    for j in range(np.shape(grid)[1]):
        height = grid[i, j]

        visible = False
        if min([max(grid[:i, j]), max(grid[i+1: ,j]), max(grid[i, :j]), max(grid[i, j+1:])]) < height:
            visible = True

        total += visible

print(total) # part 1: 1533



