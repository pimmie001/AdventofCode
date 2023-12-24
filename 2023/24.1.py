with open('24.txt') as fh:
    lines = fh.read().split('\n')


class hailstone:
    def __init__(self, coordinates, velocity):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        self.xvel = velocity[0]
        self.yvel = velocity[1]
        self.zvel = velocity[2]

        # find a and b such that line can be described by y = ax + b
        self.a = self.yvel / self.xvel # slope of line
        self.b = self.y - self.a * self.x # intersection y-axis

    def collide(self, other):
        """Finds (x,y) coordinates and times of intersection"""

        if self.a == other.a: # parralel
            return None

        x_intersect = (other.b - self.b) / (self.a - other.a)
        y_intersect = self.a * x_intersect + self.b

        t1 = (x_intersect - self.x) / self.xvel # time of intersection for self
        t2 = (x_intersect - other.x) / other.xvel # time of intersection for other

        return (x_intersect, y_intersect, t1, t2)


hailstones = []
for line in lines:
    c, v = line.split(' @ ')
    c = [int(x) for x in c.split(', ')]
    v = [int(x) for x in v.split(', ')]
    hailstones.append(hailstone(c,v))


LB = 200000000000000 # example: 7
UB = 400000000000000 # example: 27
count = 0
for i in range(len(hailstones)):
    for j in range(i+1, len(hailstones)):
        intersect = hailstones[i].collide(hailstones[j])
        if intersect:
            x,y,t1,t2 = intersect
            count += min(x,y) >= LB and max(x,y) <= UB and min(t1,t2) >= 0 # check if within bounds and if in future
print(count) # part 1: 21679



