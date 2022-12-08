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
        total += min([max(grid[:i, j]), max(grid[i+1: ,j]), max(grid[i, :j]), max(grid[i, j+1:])]) < grid[i, j]
print(total) # part 1: 1533


### part 2:

def scenic_score(i, j):
    counts = []
    for line in [reversed(grid[:i, j]), grid[i+1:, j], reversed(grid[i, :j]), grid[i, j+1:]]:
        counts.append(visible_trees(grid[i, j], line))

    return np.prod(counts)


def visible_trees(own_height, line):
    count = 0
    max_tree = -1
    for x in line:
        if x < own_height and x >= max_tree:
            count += 1

        if x >= own_height:
            count += 1
            break

    return count


best_score = 0
for i in range(1, np.shape(grid)[0]-1):
    for j in range(1, np.shape(grid)[1]-1):
        score = scenic_score(i, j)
        if score > best_score:
            best_score = score
print(best_score) # 345744
