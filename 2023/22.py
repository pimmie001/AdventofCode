from copy import deepcopy

with open('22.txt') as fh:
    content = fh.read().split('\n')


class brick:
    def __init__(self, start, end):
        """Begin and end are (x,y,z) coordinates of the brick"""

        self.start = start
        self.end = end

        x1,y1,z1 = start
        x2,y2,z2 = end

        self.cubes = set() # set of cubes corresponding to this brick
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    self.cubes.add((x,y,z))


    def is_under(self, other):
        """Returns whether self brick is under other brick"""

        for (x,y,z) in other.cubes:
            if z == 1 or (x,y,z-1) in self.cubes:
                return True
        return False


### create (list of) bricks
bricks = [] # list of sets of cubes for each brick
for line in content:
    x1,x2 = line.split('~')
    start = [int(y) for y in x1.split(',')]
    end = [int(y) for y in x2.split(',')]

    b = brick(start, end)
    bricks.append(b)


### let bricks fall down
def drop_bricks(bricks, skip=None):
    """
    Drops all bricks ones (if possible)
    Does not consider brick at index 'skip' when finding blocked bricks
    """

    ## find bricks that can drop
    bricks_that_can_drop = []
    for i, b in enumerate(bricks): # brick that is considered to be dropped

        can_drop = True
        for j, b2 in enumerate(bricks): # brick that can block brick 'b'
            if i == j or j == skip:
                continue

            if b2.is_under(b):
                can_drop = False
                break

        if can_drop:
            bricks_that_can_drop.append(b)

    # drop the bricks
    for b in bricks_that_can_drop:
        new_cubes = set()
        for (x,y,z) in b.cubes:
            new_cubes.add((x,y,z-1))
        b.cubes = new_cubes

    # return True iff no bricks dropped
    return len(bricks_that_can_drop) == 0


stopped = False
k = 0
while not stopped:
    # print(k) # for own input takes about 180 drops
    stopped = drop_bricks(bricks)
    k += 1


### count how many bricks are above each brick
safe_bricks = [] # keep track of indices for part 2
for i,b in enumerate(bricks):
    bricks_copy = deepcopy(bricks)
    if drop_bricks(bricks_copy, skip=i):
        safe_bricks.append(i)

print(len(safe_bricks)) # part 1: 519 (takes some time to run)



### part 2
def drop_bricks2(bricks, bricks_fall=set(), skip=None):
    """Similar function as before but keeps track of which bricks fall"""

    ## find bricks that can drop
    bricks_that_can_drop = []
    for i, b in enumerate(bricks): # brick that is considered to be dropped
        if i == skip:
            continue

        can_drop = True
        for j, b2 in enumerate(bricks): # brick that can block brick 'b'
            if i ==j or j == skip:
                continue

            if b2.is_under(b):
                can_drop = False
                break

        if can_drop:
            bricks_that_can_drop.append(b)
            bricks_fall.add(i)

    # drop the bricks
    for b in bricks_that_can_drop:
        new_cubes = set()
        for (x,y,z) in b.cubes:
            new_cubes.add((x,y,z-1))
        b.cubes = new_cubes

    # return True iff no bricks dropped
    return len(bricks_that_can_drop) == 0


total = 0
for i,b in enumerate(bricks):
    if i in safe_bricks:
        continue

    bricks_copy = deepcopy(bricks)
    bricks_fall = set() # set of bricks that fall in when removing brick 'b'

    stopped = False
    while not stopped:
        stopped = drop_bricks2(bricks_copy, bricks_fall, i)

    total += len(bricks_fall)

print(total) # part 2: 109531 (takes a few hours to run)