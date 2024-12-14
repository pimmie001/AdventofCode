with open("12.txt") as fh:
    grid = fh.read().split('\n')


def find_regeion(x,y):
    """Given x,y, finds entire region of plants of same type"""

    type = grid[y][x]
    locations = {(x,y)}

    while True:
        new_locations = locations.copy()

        for x,y in locations:
            for (dx,dy) in ((1,0), (0,1), (-1,0), (0,-1)):
                newx = x + dx
                newy = y + dy
                if newx < 0 or newx >= len(grid[0]) or newy < 0 or newy >= len(grid): # if out of grid
                    continue

                if grid[newy][newx] == type: # add if same type
                    new_locations.add((newx,newy))

        if locations == new_locations:
            break
        else:
            locations = new_locations

    return locations


### Find all regions
regions = []
all_locations = set() # set of all positions that are in any region in regions

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (x,y) in all_locations:
            continue

        region = find_regeion(x,y)
        regions.append(region)
        for loc in region:
            all_locations.add(loc)


### Find perimeter of a region
def get_perimeter(region):
    perimeter_locations = set()

    for x,y in region:
        for (dx,dy) in ((1,0), (0,1), (-1,0), (0,-1)):

            if (x+dx, y+dy) not in region:
                perimeter_locations.add((x+dx/2, y+dy/2))

    return len(perimeter_locations)


### Find total price
total = 0
for region in regions:
    total += len(region) * get_perimeter(region)
print(total) # part 1: 1461752 