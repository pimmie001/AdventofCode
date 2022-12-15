import re

with open('15.txt') as fh:
    input = fh.read().split('\n')


sensors = {}
for line in input:
    n = [int(x) for x in re.findall('[-0-9]+', line)]
    sensors[n[0],n[1]] = n[2], n[3]


def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


y_target = 2000000
no_beacons = set() # set of x-coordinates where x,y_target cannot be a beacon


for a in sensors:
    b = sensors[a]
    dist = distance(a, b)

    dist_y = dist - abs(y_target - a[1])
    for i in range(-dist_y, dist_y+1):
        loc = a[0]+i, y_target
        no_beacons.add(loc)

no_beacons -= set(sensors.values()) 

print(len(no_beacons)) # part 1: 5564017
