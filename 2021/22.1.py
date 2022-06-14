with open('22.1.txt') as fh:
    instruction = fh.read().split('\n')


grid = {}
for i in instruction:
    j = i.split()
    word = j[0]
    j = j[1].split(',')
    xrange = j[0].replace('x=','').split('..')
    yrange = j[1].replace('y=','').split('..')
    zrange = j[2].replace('z=','').split('..')

    for x in range(int(xrange[0]), int(xrange[1]) + 1):
        for y in range(int(yrange[0]), int(yrange[1]) + 1):
            for z in range(int(zrange[0]), int(zrange[1]) + 1):
                if word == 'on':
                    grid[x,y,z] = 1
                else:
                    grid[x,y,z] = 0

print(sum(grid.values())) # 602574

