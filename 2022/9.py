import numpy as np

with open ('9.txt') as fh:
    instructions = fh.read().split('\n')


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def move_head(x_h, y_h, dx, dy):
    x_h += dx
    y_h += dy
    return x_h, y_h


def move_tail(x_h, y_h, x_t, y_t):
    x_dis = x_h - x_t
    y_dis = y_h - y_t

    if y_dis == 0 and abs(x_dis) >= 2:
        x_t += sign(x_dis)

    if x_dis == 0  and abs(y_dis) >= 2:
        y_t += sign(y_dis)

    if abs(x_dis) + abs(y_dis) >= 3:
        x_t += sign(x_dis)
        y_t += sign(y_dis)

    return x_t, y_t



tail_visited = set() # set that keeps track of visited locations

# starting positions:
x_h, y_h = 0, 0
x_t, y_t = 0, 0
for instruction in instructions:
    direction, n = instruction.split(' ')
    n = int(n)
    
    if direction == 'R':
        dx, dy = 1, 0
    elif direction == 'L':
        dx, dy = -1, 0
    elif direction == 'U':
        dx, dy = 0, 1
    else:
        dx, dy = 0, -1

    for i in range(n):
        x_h, y_h = move_head(x_h, y_h, dx, dy)
        x_t, y_t = move_tail(x_h, y_h, x_t, y_t)
        tail_visited.add((x_t, y_t))

print(len(tail_visited)) # part 1: 6494



### part 2:
num = 10 # 9 tails + head
locations = np.zeros((num, 2))

last_tail_visited = set()


for instruction in instructions:
    direction, n = instruction.split(' ')
    n = int(n)
    
    if direction == 'R':
        dx, dy = 1, 0
    elif direction == 'L':
        dx, dy = -1, 0
    elif direction == 'U':
        dx, dy = 0, 1
    else:
        dx, dy = 0, -1

    for i in range(n):
        locations[0, :] = move_head(locations[0, 0], locations[0, 1], dx, dy)
        for tail in range(1, num):
            locations[tail, :] = move_tail(locations[tail-1, 0], locations[tail-1, 1], locations[tail, 0], locations[tail, 1])

        last_tail_visited.add((locations[-1, 0], locations[-1, 1]))

print(len(last_tail_visited)) # 2691
