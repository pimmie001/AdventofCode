import time

with open('14.txt') as fh:
    content = fh.read().split('\n')

grid = []
for line in content:
    grid.append(list(line))

n = len(grid)
m = len(grid[0])


## tilt and cycle functions
def tilt_north(grid):
    can_stop = True
    for y in range(1, n):
        for x in range(m):
            if grid[y][x] == 'O' and grid[y-1][x] == '.':
                grid[y-1][x] = 'O'
                grid[y][x] = '.'
                can_stop = False
    return can_stop

def tilt_west(grid):
    can_stop = True
    for x in range(1, m):
        for y in range(n):
            if grid[y][x] == 'O' and grid[y][x-1] == '.':
                grid[y][x-1] = 'O'
                grid[y][x] = '.'
                can_stop = False
    return can_stop

def tilt_south(grid):
    can_stop = True
    for y in reversed(range(n-1)):
        for x in range(m):
            if grid[y][x] == 'O' and grid[y+1][x] == '.':
                grid[y+1][x] = 'O'
                grid[y][x] = '.'
                can_stop = False
    return can_stop

def tilt_east(grid):
    can_stop = True
    for x in reversed(range(m-1)):
        for y in range(n):
            if grid[y][x] == 'O' and grid[y][x+1] == '.':
                grid[y][x+1] = 'O'
                grid[y][x] = '.'
                can_stop = False
    return can_stop


def cycle(grid):
    for tilt in [tilt_north, tilt_west, tilt_south, tilt_east]:
        can_stop = False
        while not can_stop:
            can_stop = tilt(grid)
    return


## get state function
def get_state(grid):
    state = ''
    for y in range(n):
        for x in range(m):
            state += grid[y][x]
    return state


## print function
def print_grid(grid):
    for y in range(n):
        for x in range(m):
            print(grid[y][x], sep='', end='')
        print()
    print()


start_time = time.time()

memo = {}
K = 1_000_000_000
k = 0
while k < K:
    current_state = get_state(grid)
    if current_state in memo: # check if state is recognized to skip a lot of steps
        k += (k - memo[current_state]) * ((K-k) // (k - memo[current_state]))
    memo[current_state] = k

    cycle(grid)
    k += 1

print(f'time: {time.time() - start_time}')

total = 0
for y in range(n):
    for x in range(m):
        if grid[y][x] == 'O':
            total += n-y
print(f'Answer part 2: {total}') # part 2: 103445 (takes about 30 seconds)
