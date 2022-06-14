import numpy as np

# test
# xmin = 20
# xmax = 30
# ymin = -10
# ymax = -5

# own input
xmin = 288
xmax = 330
ymin = -96
ymax = -50


def decreaseabs(x):
    if x > 0: x -= 1
    elif x < 0: x += 1
    return x

def isintarget(location, target):
    # location = (x, y)
    # target = xmin, xmax, ymin, xmax
    if location[0] in range(target[0], target[1] + 1) and location[1] in range(target[2], target[3] + 1): 
        return True
    return False

def anyintarget(A, target):
    # checks if any of the locations in A is in target
    for x in A:
        if isintarget(x, target):
            return True
    return False

def getpositions(forward, upward, ybound, xbound, start = None):
    if start == None:
        start = np.array([0,0])
    velocity = np.array([forward, upward])
    A = [start]
    loc = start.copy()
    while True:
        loc = loc + velocity
        A.append(loc)
        velocity[0] = decreaseabs(velocity[0])
        velocity[1] -= 1
        if loc[1] < ybound or loc[0] > xbound: 
            break
    return A

def gethighpoint(A):
    a = 0
    for x in A:
        if x[1] > a:
            a = x[1]
    return a


# # this is a guess, range should be as large as possible subject to that it does not take too long
# lbfordward = 0
# ubforward = 50
# lbupwards = 0
# ubupwards = 100


# results = []
# target = (xmin, xmax, ymin, ymax)
# for forward in range(lbfordward, ubforward):
#     for upward in range(lbupwards, ubupwards):
#         positions = getpositions(forward, upward, ymin, xmax)
#         if anyintarget(positions, target):
#             results.append(gethighpoint(positions))

# print(max(results)) # 4560, using bounds of 0,50 and 0,100
# ez clap solution
print(int(abs(ymin) * (abs(ymin) - 1) / 2)) # 4560


### part 2

# again this is a guess by trial and error
lbfordward = 0
ubforward = 400
lbupwards = ymin
ubupwards = 400

# very similiar for loop
results2 = 0 # for part 2
target = (xmin, xmax, ymin, ymax)
for forward in range(lbfordward, ubforward):
    for upward in range(lbupwards, ubupwards):
        positions = getpositions(forward, upward, ymin, xmax)
        if anyintarget(positions, target):
            results2 += 1

print(results2) # 3344, using bounds of 0,400 and -400,400

