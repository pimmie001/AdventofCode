with open('18.txt') as fh:
    input = fh.read().split('\n')

cubes = set()
for line in input:
    x,y,z = line.split(',')
    cubes.add((int(x),int(y),int(z)))

print(sum([sum([c not in cubes for c in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]]) for x,y,z in cubes])) # part 1: 4474
