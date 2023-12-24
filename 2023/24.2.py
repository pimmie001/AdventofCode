from sympy import symbols, Eq, solve

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


hailstones = []
for line in lines:
    c, v = line.split(' @ ')
    c = [int(x) for x in c.split(', ')]
    v = [int(x) for x in v.split(', ')]
    hailstones.append(hailstone(c,v))


# let (a,b,c) be the starting point and (d,e,f) the velocity of rock. 
# let (t1,t2,t3) be the times where they intersect with hailstone 1,2,3 respectively

# using 3 hailstones, we will have 9 equations with 9 unkowns
# define a function that solves these equations

def my_solve(stone1, stone2, stone3):
    # input: 3 hailstones
    # returns values of (a,b,c,d,e,f,t1,t2,t3)

    ## variables
    a,b,c,d,e,f,t1,t2,t3 = symbols('a b c d e f t1 t2 t3')

    # equations stone 1
    eq1 = Eq(stone1.x - stone1.xvel * t1, a + d*t1)
    eq2 = Eq(stone1.y - stone1.yvel * t1, b + e*t1)
    eq3 = Eq(stone1.z - stone1.zvel * t1, c + f*t1)

    # equations stone 2
    eq4 = Eq(stone2.x - stone2.xvel * t2, a + d*t2)
    eq5 = Eq(stone2.y - stone2.yvel * t2, b + e*t2)
    eq6 = Eq(stone2.z - stone2.zvel * t2, c + f*t2)

    # equations stone 3
    eq7 = Eq(stone3.x - stone3.xvel * t3, a + d*t3)
    eq8 = Eq(stone3.y - stone3.yvel * t3, b + e*t3)
    eq9 = Eq(stone3.z - stone3.zvel * t3, c + f*t3)

    solution = solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9), (a,b,c,d,e,f,t1,t2,t3))

    return solution[0]


a,b,c,d,e,f,t1,t2,t3 = my_solve(hailstones[0], hailstones[1], hailstones[2]) # choose any 3 hailstones
print(a+b+c) # part 2: 566914635762564 