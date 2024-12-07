from copy import deepcopy

with open("6.txt") as fh:
    grid = fh.read().split('\n')

# find starting position
for y in range(len(grid)):
    if '^' in grid[y]:
        cur_x = grid[y].index('^')
        cur_y = y


def is_loop(grid, start_x, start_y):
    """"Function checks if guard walks in loop"""

    cur_x, cur_y = start_x, start_y # current position

    dir = '^' # current direction

    states = set() # set of all states (x,y,direction)

    while True:
        if (cur_x, cur_y, dir) in states:
            return True # found a loop

        states.add((cur_x, cur_y, dir))

        dx,dy = {'^': (0, -1), '<': (-1,0), '>': (1,0), 'v': (0,1)}[dir]

        next_x = cur_x + dx
        next_y = cur_y + dy

        if next_y < 0 or next_y >= len(grid) or next_x < 0 or next_x >= len(grid[0]):
            return False   # out of grid: no loop

        if grid[next_y][next_x] == '#':
            dir = {'^': '>', '>': 'v', 'v': '<', '<': '^'}[dir]
        else:
            cur_x, cur_y = next_x, next_y


count = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] != '#':
            new_grid = deepcopy(grid)
            new_grid[y] = new_grid[y][:x] + '#' + new_grid[y][x+1:]
            count += is_loop(new_grid, cur_x, cur_y)
print(count) # part 2: 1482
