#! regions are hardcoded for own input shape
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


## functions
def find_region(x,y):
    if y in range(50):
        if x in range(50, 100):
            return 1
        elif x in range(100, 150):
            return 2
    elif y in range(50, 100):
        if x in range(50, 100):
            return 0
    elif y in range(100, 150):
        if x in range(50):
            return 4
        elif x in range(50, 100):
            return 3
    if y in range(150, 200):
        if x in range(50):
            return 5
    print(f'region not found: {x,y}')



def move(x, y, dir): # new positions are hardcoden when wrapping around edges
    # easy cases: 
    if dir == 0: # right
        if x not in [49, 99, 149]:
            return (x+1, y, dir)
    elif dir == 1: # down
        if y not in [49, 99, 149, 199]:
            return (x, y+1, dir)
    elif dir == 2: # left
        if x not in [0, 50, 100]:
            return (x-1, y, dir)
    elif dir == 3: # up
        if y not in [0, 50, 100, 150]:
            return (x, y-1, dir)

    # otherwise, need to wrap around the cube
    # depends on direction and region (4*6 options)
    region = find_region(x, y)

    if region == 0:
        if dir == 0: # right
            # return (99 + y-49, 49, 3) # dir changed to up
            return (y+50, 49, 3) # dir changed to up
        elif dir == 1: # down
            return (x, y+1, dir)
        elif dir == 2: # left
            return (y-50, 100, 1) # dir changed to down
        elif dir == 3: # up
            return (x, y-1, dir)

    elif region == 1:
        if dir == 0: # right
            return (x+1, y, dir)
        elif dir == 1: # down
            return (x, y+1, dir)
        elif dir == 2: # left
            return (0, 149-y, 0) # dir changed to right
        elif dir == 3: # up
            return (0, x+100, 0) # dir changed to right

    elif region == 2:
        if dir == 0: # right
            return (99, 149-y ,2) # dir changed to left
        elif dir == 1: # down
            return (99, x-50, 2) # dir changed to left
        elif dir == 2: # left
            return (x-1, y, dir)
        elif dir == 3: # up
            return (x-100, 199, 3) # dir changed to up

    elif region == 3:
        if dir == 0: # right
            return (149, 149-y ,2) # dir changed to left
        elif dir == 1: # down 
            return (49, x+100, 2) # dir changed to left
        elif dir == 2: # left
            return (x-1, y, dir)
        elif dir == 3: # up
            return (x, y-1, dir)

    elif region == 4:
        if dir == 0: # right
            return (x+1, y, dir)
        elif dir == 1: # down
            return (x, y+1, dir)
        elif dir == 2: # left
            return (50, 149-y, 0) # dir changed to right
        elif dir == 3: # up
            return (50, 50+x, 0) # dir changed to right

    elif region == 5:
        if dir == 0: # right
            return (y-100, 149, 3) # dir changed to up
        elif dir == 1: # down
            return (x+100, 0, 1) # dir changed to down
        elif dir == 2: # left
            return (y-100, 0, 1) # dir changed to down
        elif dir == 3: # up
            return (x, y-1, dir)



## walk
dir = 0 # 0: right, 1: down, 2: left, 3: up
y,x = start # staring point
for ins in instructions:
    if ins.isnumeric():
        for _ in range(int(ins)):
            new_x, new_y, new_dir = move(x, y, dir)
            if map[new_y][new_x] == '#':
                break
            else:
                x,y,dir = new_x, new_y, new_dir

    else: # change direction
        if ins == 'L':
            dir = (dir-1)%4
        else: # R
            dir = (dir+1)%4


print(1000*(y+1) + 4*(x+1) + dir) # 124302 
