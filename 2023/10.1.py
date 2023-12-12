with open('10.txt') as fh:
    content = fh.read().split('\n')

n = len(content)
m = len(content[0])

pipes = {} # dictionary (x,y): pipe type
for y in range(n):
    for x in range(m):
        if content[y][x] == 'S':
            S_coor = (x,y)
        pipes[(x,y)] = content[y][x]


def find_adj_pipes(x, y, visited):
    """input: pipe (eg L or J), and x and y coordinate of pipe. 
    Returns adjacent pipes that match"""

    # allowed dx,dy changes given a pipe:
    allowed = {'|': [(0,1), (0,-1)], '-': [(1,0), (-1,0)], 'L': [(1,0), (0,-1)], 'F': [(1,0), (0,1)], '7': [(-1,0), (0,1)], 'J': [(-1,0), (0,-1)], 'S': [(1,0), (-1,0), (0,1), (0,-1)]} 

    adjacent = []
    for dx,dy in allowed[pipes[(x,y)]]:
        if (x+dx, y+dy) in visited or x+dx < 0 or y+dy < 0 or x+dx >= m or y+dy >=n:
            continue

        if (dx,dy) == (1,0):
            if pipes[(x+dx, y+dy)] in ['7', 'J', '-']:
                adjacent.append((x+dx, y+dy))
        elif (dx,dy) == (-1,0):
            if pipes[(x+dx, y+dy)] in ['L', 'F', '-']:
                adjacent.append((x+dx, y+dy))
        elif (dx,dy) == (0,1):
            if pipes[(x+dx, y+dy)] in ['L', 'J', '|']:
                adjacent.append((x+dx, y+dy))
        elif (dx,dy) == (0,-1):
            if pipes[(x+dx, y+dy)] in ['7', 'F', '|']:
                adjacent.append((x+dx, y+dy))

    return adjacent


## loop until no adjacent pipes can be added to loop
all_pipes = [[S_coor]]
visited = set([S_coor])
while all_pipes[-1]:
    new_pipes = []
    for (x,y) in all_pipes[-1]:
        adjacent = find_adj_pipes(x, y, visited)
        new_pipes.extend(adjacent)
        for elem in adjacent:
            visited.add(elem)
    all_pipes.append(new_pipes)


print(len(all_pipes) - 2) # first one is ['S'] and last one is empty list so these two dont count
# part 1: 7063


##### part 2 #! not finished: probably because some pipes that are connected to loop but not part of loop are in set visited


def print_map(visited=visited):
    for y in range(n):
        for x in range(m):
            if (x,y) in visited:  
                print('#', sep='', end='')
            else:
                print('.', sep='', end='')
        print()


def can_escape(x, y, memo={}, previous=set()):
    """Returns whether location x,y can escape the map without running into the bounary (loop of pipes)."""

    ## base cases
    if (x,y) in visited:
        return False

    if x < 0 or y < 0 or x > m or y > n:
        return True

    if (x,y) in memo:
        return memo[(x,y)]


    ## other cases
    previous.add((x,y))
    for (dx,dy) in [(1,0), (-1,0), (0,1), (0,-1)]:
        if (x+dx, y+dy) not in previous and can_escape(x+dx, y+dy, memo, previous):
            memo[(x,y)] = True
            return True

    memo[(x,y)] = False
    return False

print()
total = 0
for x in range(m):
    for y in range(n):
        previous = set()
        memo = {}
        if (x,y) not in visited and not can_escape(x, y, memo, previous):
            print(x,y)
            total += 1
print('\n', total)

x, y = 3,2
memo = {}
previous = set()
print(can_escape(x, y, memo, previous))


print_map()

# total = 0
# memo = {}
# for x in range(m):
#     for y in range(n):
#         total += not can_escape(x, y, memo)
# print(total)

print('finished')

# # for each x coordinate (0,...,m-1), find the y coordinates of pipes that are in loop
# # eg X_list = [[0,2], [1,2]] means that (0,0),(0,2),(1,1),(1,2) are pipes in the loop
# X_list = []
# for x in range(m):
#     temp = []
#     for y in range(n):
#         if (x,y) in visited:
#             temp.append(y)
#     X_list.append(temp)

# # do same for y
# Y_list = []
# for y in range(n):
#     temp = []
#     for x in range(m):
#         if (x,y) in visited:
#             temp.append(x)
#     Y_list.append(temp)


# def checkx(x, y):
#     # check whether x coordinate can be contained in loop

#     if x in Y_list[y]:
#         return False

#     contained = False
#     Y = Y_list[y].copy()
#     Y.insert(0, -1)
#     for i in range(len(Y) - 1):
#         if Y[i] < x and x < Y[i+1]:
#             return contained
#         contained = not contained

#     return False


# def checky(x, y):
#     # check whether x coordinate can be contained in loop

#     if y in X_list[x]:
#         return False

#     contained = False
#     X = X_list[x].copy()
#     X.insert(0, -1)
#     for i in range(len(X) - 1):
#         if X[i] < y and y < X[i+1]:
#             return contained
#         contained = not contained

#     return False


# total = 0
# for x in range(m):
#     for y in range(n):
#         total += checkx(x,y) and checky(x,y)
# print(total)
# # 264 too low
# 861 too high