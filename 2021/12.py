with open('12.txt') as f:
    content = f.read().split('\n')

V = [] # set of vertices
E = [] # set of edges

for line in content:
    x = line.split('-')
    if x[0] not in V: V.append(x[0])
    if x[1] not in V: V.append(x[1])

    E.append((x[0], x[1]))
    E.append((x[1], x[0]))


def iscorrect(path):
    if path[0] == 'start' and path[-1] == 'end': return True
    return False

def countall(paths):
    result = 0
    for path in paths:
        if iscorrect(path): result += 1
    return result

def nextstep(paths, E):
    # paths is an array of current paths
    allnewpaths = []

    for path in paths:
        lastlocation = path[-1]
        if lastlocation != 'end':
            for edge in E:
                if edge[0] == lastlocation:
                    # extra condition for not visiting small caves twice (start is lowercase so wont get visited twice)
                    if edge[1] == edge[1].upper() or edge[1] not in path: 
                        newpath = path.copy()
                        newpath.append(edge[1])
                        allnewpaths.append(newpath)

        else:
            allnewpaths.append(path)

    return allnewpaths


paths = [['start']]

while True:
    oldspaths = paths.copy()
    paths = nextstep(paths, E)
    if oldspaths == paths:
        print(f'Part 1: {countall(paths)}\n')
        break
# 3779


### part 2:

def nextstep2(paths, E, V):
    allnewpaths = []

    for path in paths:
        lastlocation = path[-1]
        if lastlocation != 'end':
            for edge in E:
                if edge[0] == lastlocation:
                    # do not go back to start and (edge should be uppercase or not in path or should be time to visit extra smallpath)
                    if edge[1] != 'start' and (edge[1] == edge[1].upper() or edge[1] not in path or not alreadytwicesmall(path, V)):
                        newpath = path.copy()
                        newpath.append(edge[1])
                        allnewpaths.append(newpath)

        else:
            allnewpaths.append(path)

    return allnewpaths

def alreadytwicesmall(path, V):
    # checks wether there is already a small cave twice in the path
    for x in V:
        if x == x.lower():
            if path.count(x) == 2:
                return True
    return False


paths = [['start']]

while True:
    oldspaths = paths.copy()
    paths = nextstep2(paths, E, V)
    if oldspaths == paths:
        # print(paths)
        print(f'Part 2: {countall(paths)}')
        break
# 96988