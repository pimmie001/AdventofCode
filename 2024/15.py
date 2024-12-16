with open('15.txt') as fh:
    grid, instructions = fh.read().split('\n\n')
    grid = grid.split('\n')
    grid = [list(row) for row in grid]
    instructions = instructions.replace("\n", "")

n = len(grid)
m = len(grid[0])
for y in range(n):
    for x in range(m):
        if grid[y][x] == '@':
            cur_x, cur_y = x, y # location of robot
            grid[y][x] = '.'


def move(grid, cur_x, cur_y, inst):
    dx, dy = {'>':(1,0), '<':(-1,0), 'v':(0,1), '^':(0,-1)}[inst]

    org_x, org_y = cur_x, cur_y

    first_box = None # first encountered box while attempting to move
    while True:
        new_x, new_y = cur_x+dx, cur_y+dy

        if grid[new_y][new_x] == '#': # wall
            return org_x, org_y # dont move anything

        if grid[new_y][new_x] == '.': # free space
            if first_box is None:
                org_x+dx, org_y+dy
            else:
                grid[new_y][new_x] = 'O' # move first box to first empty space
                grid[first_box[1]][first_box[0]] = '.' # where first box was is now empty
            return org_x+dx, org_y+dy

        if grid[new_y][new_x] == 'O': # box
            if first_box is None:
                first_box = (new_x, new_y)

        cur_x, cur_y = new_x, new_y 


def print_grid(grid, cur_x=cur_x, cur_y=cur_y):
    for y in range(n):
        for x in range(n):
            print('@' if y==cur_y and x==cur_x else grid[y][x], end='')
        print()
    print()



for inst in instructions:
    cur_x, cur_y = move(grid, cur_x, cur_y, inst)
    # print_grid(grid, cur_x, cur_y)


total = 0
for y in range(n):
    for x in range(m):
        if grid[y][x] == 'O':
            total += x + 100*y
print(total) # part 1: 1478649

