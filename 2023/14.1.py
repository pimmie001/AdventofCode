with open('14.txt') as fh:
    content = fh.read().split('\n')

grid = []
for line in content:
    grid.append(list(line))

n = len(grid)
m = len(grid[0])


def tilt(grid):
    can_stop = True
    for y in range(1, n):
        for x in range(m):
            if grid[y][x] == 'O' and grid[y-1][x] == '.':
                grid[y-1][x] = 'O'
                grid[y][x] = '.'
                can_stop = False
    return can_stop



can_stop = False
while not can_stop:
    can_stop = tilt(grid)


total = 0
for y in range(n):
    for x in range(m):
        if grid[y][x] == 'O':
            total += n-y
print(total) # part 1: 108840
