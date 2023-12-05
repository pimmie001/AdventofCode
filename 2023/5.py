import re

with open('5.txt') as fh:
    content = fh.read().split('\n\n')

seeds = [int(x) for x in re.findall(r'\d+', content[0])]
content = content[1:]


maps = {}
for string in content:
    string = string.split('\n')
    c1, c2 = string[0].split(' ')[0].split('-to-') # categories

    map = []
    for line in string[1:]:
        dest, source, length = (int(x) for x in re.findall(r'\d+', line))
        end = source + length - 1
        increment = dest - source
        map.append((source, end, increment))

    maps[(c1, c2)] = map


categories = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

def get_location(seed):
    for i in range(len(categories) - 1):
        c1, c2 = categories[i:i+2]
        map = maps[(c1, c2)]

        for start, end, increment in map:
            if seed >= start and seed <= end:
                seed += increment
                break

    return seed


minimum = float('inf')
for seed in seeds:
    minimum = min(minimum, get_location(seed))
print(minimum) # part 1: 278755257



#### part 2

def get_location2(seed):
    # Given a seed, return the location, also keeps track on how many numbers can be skipped.
    # Can skip a certain of numbers if all 'skip' next numbers are also in the same range for every map since
    # final location value will just be the current value + some number.

    skip = float('inf')
    for i in range(len(categories) - 1):
        c1, c2 = categories[i:i+2]
        map = maps[(c1, c2)]

        for start, end, increment in map:
            if seed >= start and seed <= end:
                diff = end - seed
                skip = min(skip, diff + 1)
                seed += increment
                break

    return seed, skip


ranges = []
for i in range(len(seeds)//2):
    start_seed = seeds[i*2]
    ranges.append((start_seed, start_seed + seeds[i*2+1]))

minimum2 = float('inf')
for x in ranges:
    current = x[0]
    while current < x[1]:
        value, skip = get_location2(current)
        minimum2 = min(minimum2, value)
        current += skip

print(minimum2) # part 2: 26829166
