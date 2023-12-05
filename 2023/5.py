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
