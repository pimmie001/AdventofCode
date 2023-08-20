with open('23.txt') as fh:
    content = fh.read().split('\n')


elves_locations = []
for y in range(len(content)): # down by one means that y goes up by one
    for x in range(len(content[y])): # right by one means that x goes up by one
        if content[y][x] == '#':
            elves_locations.append((x,y))


### some functions

def propose_north(x,y, locations):
    return (not ((x,y-1) in locations or (x-1,y-1) in locations or (x+1,y-1) in locations)), (x,y-1)

def propose_south(x,y, locations):
    return (not ((x,y+1) in locations or (x-1,y+1) in locations or (x+1,y+1) in locations)), (x,y+1)

def propose_west(x,y, locations):
    return (not ((x-1,y) in locations or (x-1,y-1) in locations or (x-1,y+1) in locations)), (x-1,y)

def propose_east(x,y, locations):
    return (not ((x+1,y) in locations or (x+1,y-1) in locations or (x+1,y+1) in locations)), (x+1,y)


def find_unique_indices(A):
    """Find indices of element that are unique in the list"""

    element_count = {}

    # Count the occurrences of each element and store their indices
    for idx, element in enumerate(A):
        if element is None:
            continue
        if element in element_count:
            element_count[element][0] += 1
        else:
            element_count[element] = [1, idx]

    # Create a list of indices where elements occurred once
    unique_indices = set()
    for count, index in element_count.values():
        if count == 1:
            unique_indices.add(index)

    return unique_indices


def print_map(locations):
    xmin = ymin = float('inf')
    xmax = ymax = float('-inf')
    for (x,y) in elves_locations:
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y

    for y in range(ymin-1, ymax+2):
        for x in range(xmin-1, xmax+2):
            if (x,y) in locations:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print('\n')


priority = [propose_north, propose_south, propose_west, propose_east] # order of considering movements

### main loop
# print_map(elves_locations)
for _ in range(10):
    ## determine the proposition
    propositions = []
    for i,(x,y) in enumerate(elves_locations):
        if (x,y) == (2,1):
            a = 'sdfkljwelkjrflkwwe'
        all_clear = True
        is_stuck = True
        for f in priority[::-1]:
            can_move, to_location = f(x,y, elves_locations)
            if can_move:
                proposition = to_location
                is_stuck = False
            else:
                all_clear = False

        if all_clear or is_stuck: 
            proposition = None

        propositions.append(proposition)

    ## find which propoistions are valid
    elves_locations_new = []
    unique_indices = find_unique_indices(propositions)
    for i,(x,y) in enumerate(elves_locations):
        if i in unique_indices:
            elves_locations_new.append(propositions[i])
        else:
            elves_locations_new.append(elves_locations[i])
    elves_locations = elves_locations_new
    # print_map(elves_locations)

    ## change priority
    priority.append(priority.pop(0))



### part 1
xmin = ymin = float('inf')
xmax = ymax = float('-inf')
for (x,y) in elves_locations:
    if x < xmin:
        xmin = x
    if x > xmax:
        xmax = x
    if y < ymin:
        ymin = y
    if y > ymax:
        ymax = y

print((xmax-xmin+1)*(ymax-ymin+1)-len(elves_locations)) # 4025


