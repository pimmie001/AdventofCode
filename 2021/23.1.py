import copy

input = 'B C B D A D C A'.split(' ') # example
bound = 20000

cost = {'A': 1, 'B':10, 'C':100, 'D':1000}
letters = 'A B C D'.split(' ')
allcoordinates = [(x,0) for x in range(11)]
allcoordinates.extend([(2,1), (2,2), (4,1), (4,2), (6,1), (6,2), (8,1), (8,2)])

positions = []
for i in range(len(input)):
    if i < 4:
        positions.append((2*i+2,1))
    else:
        positions.append((2*i-6,2))
state = [positions, input, 0] # coordinates, letter, cost to reach this state


def removedups(A):
    B = []
    for x in A:
        if x not in B:
            B.append(x)
    return B


def clearpath(positions, a, b):
    # dont uncomment
    # if a[0] > b[0]: # a always has lowest x coordinate
    #     return clearpath(state, b, a)
    x1,y1 = a[0],a[1]
    x2,y2 = b[0],b[1]

    if y1 == 0:
        if x1 < x2:
            for x in range(x1 + 1, x2 + 1):
                if (x,y1) in positions: return False
        elif x1 > x2:
            for x in range(x2+1, x1):
                if (x,y1) in positions: return False
        for y in range(y2 + 1):
            if (x2, y) in positions: return False

    else:
        for y in range(y1 -1, -1, -1):
            if (x1, y) in positions: return False
        return clearpath(positions, (x1,0), (x2,y2))

    return True


def canmove(positions,a,b,letter):
    if not clearpath(positions,a,b): return False

    if b in [(x,0) for x in range(2,9,2)]: return False

    if b[1] > 0:
        if letter == 'A':
            if b in [(4,1), (4,2), (6,1), (6,2), (8,1), (8,2)]: return False
        elif letter == 'B':
            if b in [(2,1), (2,2), (6,1), (6,2), (8,1), (8,2)]: return False
        elif letter == 'C':
            if b in [(2,1), (2,2), (4,1), (4,2), (8,1), (8,2)]: return False
        elif letter == 'D':
            if b in [(2,1), (2,2), (4,1), (4,2), (6,1), (6,2)]: return False

    return True


def move(state):
    # state = copy.deepcopy(state)
    positions = state[0]
    L = state[1]

    newstates = []
    for i in range(len(positions)):
        pos = positions[i]
        letter = L[i]

        for newpoint in allcoordinates:
            if canmove(positions, pos, newpoint, letter):
                newstate = copy.deepcopy(state)
                newstate[0][i] = newpoint
                newstate[1][i] = letter 

                length = abs(pos[0]-newpoint[0]) + abs(pos[1] - newpoint[1])
                newstate[2] += length * cost[letter]

                if newstate[2] <= bound:
                    newstates.append(newstate)

    return newstates


found = []
def iscorrect(positions, places, n):
    global found
    for coor in positions:
        if coor[1] == 0: return False

    for i in range(len(positions)):
        pos = positions[i]
        letter = places[i]

        if pos[0] == 2 and letter != 'A':
            return False
        elif pos[0] == 4 and letter != 'B':
            return False
        elif pos[0] == 6 and letter != 'C':
            return False
        elif pos[0] == 8 and letter != 'D':
            return False
    found.append(n)
    print(n)
    return True


def moveall(states):
    allnewstates = []
    for state in states:
        if not iscorrect(state[0], state[1], state[2]):
            newstates = move(state)
            allnewstates.extend(newstates)
        else:
            allnewstates.append(state)

    return removedups(allnewstates)



its = 5
allstates = [state]
for it in range(its):
    allstates = moveall(allstates)









# a = (6,1)
# b = (3,0)

# print('\n\n\nkomtieeee')
# newstates = moveall([state])
# print(newstates)


