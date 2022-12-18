import sys
sys.setrecursionlimit(10000) # needs to be at least 21**3 for has_path function


with open('18.txt') as fh:
    input = fh.read().split('\n')

cubes = set()
for line in input:
    x,y,z = line.split(',')
    cubes.add((int(x),int(y),int(z)))

print(sum([sum([c not in cubes for c in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]]) for x,y,z in cubes])) # part 1: 4474


### part 2

n = 22
def has_path(src, visited=set()):
    # returns if src has a path towards the outside (it is not in the interior)
    if min(src) < 0 or max(src) >= n:
        return True

    visited.add(src)
    x,y,z = src
    for neighbor in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]:
        if neighbor in cubes:
            continue
        if neighbor in visited:
            continue
        if has_path(neighbor, visited):
            return True

    return False


# determine interior
interior = set()
for x in range(n):
    for y in range(n):
        for z in range(n):
            if (x,y,z) in cubes:
                continue
            if not has_path((x,y,z), set()):
                interior.add((x,y,z))


total = 0
for x,y,z in cubes:
    for c in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]:
        if not (c in cubes or c in interior):
            total += 1
print(total) # 2518
