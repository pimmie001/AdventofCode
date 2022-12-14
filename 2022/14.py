with open('14.txt') as fh:
    input = fh.read().split('\n')


ymax = 0
rocks = set()

for line in input:
    coordinates = line.split(' -> ')
    for i in range(len(coordinates)-1):
        x1, y1 = coordinates[i].split(',')
        x2, y2 = coordinates[i+1].split(',')
        x1, x2 = min(int(x1), int(x2)), max(int(x1), int(x2))
        y1, y2 = min(int(y1), int(y2)), max(int(y1), int(y2))

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                rocks.add((x,y))

        ymax = max(ymax, y1)


sand_spawn = 500,0
sand = set()

def move_sand():
    x, y = sand_spawn
    while True:
        if (x,y+1) not in rocks and (x,y+1) not in sand: # move below
            y += 1
        elif (x-1,y+1) not in rocks and (x-1,y+1) not in sand: # move left/below
            x -= 1
            y += 1
        elif (x+1,y+1) not in rocks and (x+1,y+1) not in sand: # move right/below
            x += 1
            y += 1
        else: # rest sand
            sand.add((x,y))
            return None

        if y > ymax: # sand will fall for infinite
            return len(sand)


while True:
    result = move_sand()
    if result is not None:
        print(result)# part 1: 799 
        break


### part 2:

def move_sand2():
    x, y = sand_spawn
    while sand_spawn not in sand:
        if y == ymax + 1: # sand reached floor
            sand.add((x,y))
            return None

        elif (x,y+1) not in rocks and (x,y+1) not in sand: # move below
            y += 1
        elif (x-1,y+1) not in rocks and (x-1,y+1) not in sand: # move left/below
            x -= 1
            y += 1
        elif (x+1,y+1) not in rocks and (x+1,y+1) not in sand: # move right/below
            x += 1
            y += 1
        else: # rest sand
            sand.add((x,y))
            return None

    return len(sand)


while True:
    result = move_sand2()
    if result is not None:
        print(result)# part 2: 29076 
        break
