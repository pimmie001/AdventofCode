import math


with open('8.txt') as fh:
    instructions, lines = fh.read().split('\n\n')

## read data and put in a graph (dictionary)
graph = {}
lines = lines.split('\n')
for line in lines:
    start, dest = line.split(' = ')
    left, right = dest[1:-1].split(', ')
    graph[start] = (left, right)


## find all locations to start with
currents = []
for location in graph:
    if location[-1] == 'A':
        currents.append(location)



def find_loop(current):
    # return index of first time a loop is found and the length of the loop

    visited = {(current, 0): 0}
    i = 0

    while True:
        direction = instructions[i%len(instructions)]
        current = graph[current][direction == 'R']
        i += 1

        if (current, i%len(instructions)) in visited:
            break
        visited[(current, i%len(instructions))] = i

    return i, (i - visited[((current, i%len(instructions)))])


def find_Z_indices(current, max_ind):
    # find indices that end in a location ending in Z

    i = 0
    indices = []
    while i < max_ind:
        direction = instructions[i%len(instructions)]
        current = graph[current][direction == 'R']
        i += 1
        if current[-1] == 'Z':
            indices.append(i)
    return indices


# it was checked that find_Z_indices always contained one element
loop_lengths = []
Z_indices = []
for current in currents:
    i, length = find_loop(current)
    Z_ind = find_Z_indices(current, i)
    loop_lengths.append(length)
    Z_indices.append(Z_ind[0])

# that this index is always the same as the loop length
# therefore, we only need to find least common multiple of these numbers

lcm = 1
for x in Z_indices:
    lcm = math.lcm(lcm, x)
print(lcm) # part 2: 18625484023687
