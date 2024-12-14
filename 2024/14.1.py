with open('14.txt') as fh:
    content = fh.read().split('\n')


n,m = 103,101 # width of grid

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y 
        self.vx = vx
        self.vy = vy

robots = []
for line in content:
    a,b = line.split(' ')
    a = a[2:]
    b = b[2:]
    x,y = a.split(',')
    vx,vy = b.split(',')

    robot = Robot(int(x),int(y),int(vx),int(vy))
    robots.append(robot)


def move_robots(robots):
    for robot in robots:
        robot.x = (robot.x + robot.vx) % m
        robot.y = (robot.y + robot.vy) % n


# move robots
for _ in range(100):
    move_robots(robots)

robots_positions = []
for robot in robots:
    robots_positions.append((robot.x, robot.y))


count = [0, 0, 0, 0]
for (x,y) in robots_positions:
    if 0 <= x < m//2:
        if 0 <= y < n//2:
            count[0] += 1
        elif n//2 < y < n:
            count[1] += 1
    elif m//2 < x < m:
        if 0 <= y < n//2:
            count[2] += 1
        elif n//2 < y < n:
            count[3] += 1


result = 1
for x in count:
    result *= x
print(result) # part 1: 222062148
