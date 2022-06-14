with open("14.txt") as fh:
    content = fh.read().split("\n")

def distance(n,prop):
    speed = prop[0]
    time = prop[1]
    rest = prop[2]

    cycle = time + rest
    full = (n + rest) // cycle      # amount of full runs completed within n seconds
    d = full * speed * time

    if n % cycle < time:
        d += (n % cycle) * speed
        
    # print(d)
    return d 

props = {}
reindeers = []
for x in content:
    x = x.split()
    deer = x[0]
    speed = int(x[3])
    time = int(x[6])
    rest = int(x[-2])
    reindeers.append(deer)
    props[deer] = speed,time,rest

n = 2503

distances = {}
for deer in reindeers:
    distances[deer] = distance(n,props[deer])

print("The best deer is {} with a distance of {}\n".format(max(distances),distances[max(distances)]))


### Part 2

points = {}
distances = {}
for deer in reindeers:
    points[deer] = distances[deer] = 0

for i in range(1,n+1):
    for deer in reindeers:
        distances[deer] = distance(i,props[deer])
    winners = []
    for deer in reindeers:
        if distances[deer] == max(distances.values()):
            winners.append(deer)
    for deer in winners:
        points[deer] += 1

print("The bset deer is {} and has {} points".format(max(points),max(points.values())))


