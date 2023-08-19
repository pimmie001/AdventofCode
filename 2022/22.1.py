import re


with open('22.txt') as fh:
    map, instructions = fh.read().split('\n\n')

instructions = re.findall(r'(\d+|[A-Za-z])', instructions)
map = map.split('\n')
n = len(map)
m = max(len(map[0]), len(map[-1])) #! no trail spaces are added so depends on shape

for y in range(n): # add trail spaces
    map[y] += ' ' * (m - len(map[y]))


## find starting position
x = 0
while True:
    if map[0][x] == '.':
        start = (0, x)
        break
    x += 1


## walk
dir = 0 # start facing right
y,x = start # staring point
for ins in instructions:
    # print(y,x)
    if ins.isnumeric():
        for _ in range(int(ins)):
            if dir == 0:
                if map[y][(x+1)%m] == '#': 
                    break
                elif map[y][(x+1)%m] == ' ':
                    x2 = (x+1)%m 
                    while True:
                        if map[y][x2] == '.':
                            x = x2
                            break
                        if map[y][x2] == '#':
                            break
                        x2 = (x2+1)%m
                else:
                    x = (x+1)%m

            elif dir == 1:
                if map[(y+1)%n][x] == '#':
                    break
                elif map[(y+1)%n][x] == ' ':
                    y2 = (y+1)%n
                    while True:
                        if map[y2][x] == '.':
                            y = y2
                            break
                        if map[y2][x] == '#':
                            break
                        y2 = (y2+1)%n
                else:
                    y = (y+1)%n

            elif dir == 2:
                if map[y][(x-1)%m] == '#':
                    break
                elif map[y][(x-1)%m] == ' ':
                    x2 = (x-1)%m
                    while True:
                        if map[y][x2] == '.':
                            x = x2
                            break
                        if map[y][x2] == '#':
                            break
                        x2 = (x2-1)%m
                else:
                    x = (x-1)%m

            else: # dir == 3
                if map[(y-1)%n][x] == '#':
                    break
                elif map[(y-1)%n][x] == ' ':
                    y2 = (y-1)%n
                    while True:
                        if map[y2][x] == '.':
                            y = y2
                            break
                        if map[y2][x] == '#':
                            break
                        y2 = (y2-1)%n
                else:
                    y = (y-1)%n


    else: # change direction
        if ins == 'L':
            dir = (dir-1)%4
        else: # R
            dir = (dir+1)%4


print(1000*(y+1) + 4*(x+1) + dir) # 88268
