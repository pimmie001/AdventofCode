import sys
sys.setrecursionlimit(2500) # increase recursion depth


with open('24.txt') as fh:
    map0 = fh.read().split('\n')

n = len(map0)
m = len(map0[0])

start = (1,0)
end = (m-2, n-1)


### create blizzard dictionary
blizzards_0 = {'v':[], '^':[], '<':[], '>':[]}
for y in range(n):
    for x in range(m):
        if map0[y][x] in ['v', '^', '<', '>']:
            blizzards_0[map0[y][x]].append((x,y))



blizzards_directions = [blizzards_0] # list of blizzard directions for each minute
def get_blizzards_directions(min):
    # returns the blizzard directions dictionary at minute 'min'

    if min < len(blizzards_directions): # if it already exists
        return blizzards_directions[min]

    # else: create it
    prev_blizzard_direction = get_blizzards_directions(min-1)
    new_blizzard_direction = {'v':[], '^':[], '<':[], '>':[]}
    for dir in prev_blizzard_direction:
        for x,y in prev_blizzard_direction[dir]:
            if dir == 'v':
                if y == n-2:
                    new_blizzard_direction[dir].append((x,1))
                else:
                    new_blizzard_direction[dir].append((x,y+1))

            elif dir == '^':
                if y == 1:
                    new_blizzard_direction[dir].append((x,n-2))
                else:
                    new_blizzard_direction[dir].append((x,y-1))

            elif dir == '<':
                if x == 1:
                    new_blizzard_direction[dir].append((m-2,y))
                else:
                    new_blizzard_direction[dir].append((x-1,y))

            elif dir == '>':
                if x == m-2:
                    new_blizzard_direction[dir].append((1,y))
                else:
                    new_blizzard_direction[dir].append((x+1,y))


    blizzards_directions.append(new_blizzard_direction)
    return get_blizzards_directions(min)



def make_blizzard_set(blizzard_locations):
    # given blizzard_directions, returns a set of the (x,y) locations that have a blizzard
    blizzard_set = set()
    for key in blizzard_locations:
        for x,y in blizzard_locations[key]:
            blizzard_set.add((x,y))
    return blizzard_set



blizzard_sets = [make_blizzard_set(blizzards_0)]
def get_blizzard_set(min):
    # returns blizzard set at minute 'min
    if min < len(blizzard_sets):
        return blizzard_sets[min]

    # create all missing blizzard sets
    for i in range(len(blizzard_sets), min+1):
        blizzard_sets.append(make_blizzard_set(get_blizzards_directions(i)))
    return get_blizzard_set(min)



def is_dead(state):
    # returns whether the player will die if on location (x,y) at minute 'min'
    x, y, min = state
    blizzard_locations = get_blizzard_set(min)
    return (x,y) in blizzard_locations



def shortest_path(state, target, memo=None):
    if memo is None:
        memo = {}
    # returns the shortest path length for the current state

    x, y, min = state

    ### base cases
    if (x,y) == target: # target achieved
        return 0

    if min == 1000: #! the lower this upperbound is, the faster the code but if it is lower than the actual shortest path length then the function will return inf
        return float('inf')
    if (x,y) != start and (x,y) != end and (x <= 0 or y <= 0 or x >= m-1 or y >= n-1): # in the wall/outside map
        return float('inf')
    if is_dead(state): # died by blizzard
        return float('inf')

    ### check memo
    if state in memo:
        return memo[state]

    ### recursive step
    value_state = float('inf')
    for dx, dy in [(0,1), (-1,0), (0,-1), (1,0), (0,0)]:
        new_state = (x+dx, y+dy, min+1)
        value_new_state = shortest_path(new_state, target, memo)
        if 1 + value_new_state < value_state:
            value_state = 1 + value_new_state

    memo[state] = value_state
    return value_state



## part 1
state = (start[0], start[1], 0)
distance = shortest_path(state, target = end)
print(distance) # answer: 290

## part 2
distance += shortest_path((end[0], end[1], distance), target = start) # go back to start
distance += shortest_path((start[0], start[1], distance), target = end) # go back to target again
print(distance) # answer: 842

