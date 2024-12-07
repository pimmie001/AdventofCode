with open("6.txt") as fh:
    grid = fh.read().split('\n')

# find starting position
direction = '^'
for y in range(len(grid)):
    if direction in grid[y]:
        cur_x = grid[y].index('^')
        cur_y = y


movement = {'^': (0, -1), '<': (-1,0), '>': (1,0), 'v': (0,1)} # dx,dy with x going right and y going down 

locations = set() # set of all visited locations

while True:
    locations.add((cur_x, cur_y))

    dx,dy = movement[direction]

    next_x = cur_x + dx
    next_y = cur_y + dy

    if next_y < 0 or next_y >= len(grid) or next_x < 0 or next_x >= len(grid[0]):
        break

    if grid[next_y][next_x] == '#':
        direction = {'^': '>', '>': 'v', 'v': '<', '<': '^'}[direction]
    else:
        cur_x, cur_y = next_x, next_y

print(len(locations)) # part 1: 4973
