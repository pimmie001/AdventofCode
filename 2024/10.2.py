with open('10.txt') as fh:
    grid = fh.read().split('\n')


def search(positions, num):
    if num == 9:
        return len(positions)


    new_positions = []
    for x,y in positions:
        for (dx,dy) in [(1,0), (0,1), (-1,0), (0,-1)]:
            newx = x + dx
            newy = y + dy
            if newx < 0 or newx >= len(grid[0]) or newy < 0 or newy >= len(grid): # if out of grid
                continue

            if int(grid[newy][newx]) == num + 1:
                new_positions.append((x+dx, y+dy))

    return search(new_positions, num+1)


total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if int(grid[y][x]) == 0:
            total += search([(x,y)], 0)
print(total) # part 1: 688
