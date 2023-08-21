with open('17.txt') as fh:
    gas_direction = fh.read()


rock1 = [(2,4), (3,4), (4,4), (5,4)]
rock2 = [(3,6), (2,5), (3,5), (4,5), (3,4)]
rock3 = [(4,6), (4,5), (4,4), (3,4), (2,4)]
rock4 = [(2,7), (2,6), (2,5), (2,4)]
rock5 = [(2,5), (3,5), (2,4), (3,4)]

rocks = [rock1, rock2, rock3, rock4, rock5]



def spawn_rock(rock, floor):
    positions = []
    for x,y in rock:
        positions.append((x, y + max(floor)))
    return positions


def move_rock(positions, current_rocks, direction = 'v'):
    new_positions = []
    if direction == '<':
        for x,y in positions:
            x -= 1
            if x < 0 or (x,y) in current_rocks:
                return positions
            new_positions.append((x,y))

    elif direction == '>':
        for x,y in positions:
            x += 1
            if x >= 7 or (x,y) in current_rocks: 
                return positions
            new_positions.append((x,y))

    else: # direction = 'v'
        for x,y in positions:
            y -= 1
            if (x,y) in current_rocks:
                return positions, True
            new_positions.append((x,y))

    if direction == 'v':
        return new_positions, False
    else:
        return new_positions



### floor and current_rocks setup
floor = [0]*7 # for each x-coordinate: the highest level of rock
current_rocks = set()
for x in range(7):
    current_rocks.add((x,0))


rocknum = 0
gasnum = 0
target = 1_000_000_000_000
all_states = {}
while rocknum < target:
    ##### Idea: look for a pattern (same floor levels, gas directions, rocknumber), then use this to 'fast-forward' until rocknum is very close to target
    ### 1. create a state
    relative_floor = (0,)
    for x in floor[1:]:
        relative_floor += (x-floor[0],)
    state = (rocknum%len(rocks), gasnum) + relative_floor

    ### 2. if state is recognized: fast-forward
    if state in all_states:
        delta_rocknum = rocknum - all_states[state][0]
        delta_floor = floor[0] - all_states[state][1]
        M = (target - rocknum) // delta_rocknum # amount of times we can fast-forward

        for i in range(len(floor)):
            floor[i] += M * delta_floor # update floor

        new_current_rocks = set()
        for (x,y) in current_rocks:
            new_current_rocks.add((x, y + M * delta_floor))

        current_rocks = new_current_rocks # update current rocks
        rocknum = rocknum + delta_rocknum * M # update rocknum

    ### 3. add state to dictioanry
    all_states[state] = (rocknum, floor[0])



    ### code from part 1
    rock = rocks[rocknum % len(rocks)]
    rocknum += 1

    positions = spawn_rock(rock, floor)

    rest = False
    while not rest:
        gas_dir = gas_direction[gasnum]
        gasnum = (gasnum + 1) % len(gas_direction)

        positions = move_rock(positions, current_rocks, direction = gas_dir)
        positions, rest = move_rock(positions, current_rocks, direction = 'v')

    for x,y in positions:
        floor[x] = max(floor[x], y)
        current_rocks.add((x,y))



print(max(floor)) # part 2: 1532163742758

