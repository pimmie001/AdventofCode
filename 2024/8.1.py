with open("8.txt") as fh:
    grid = fh.read().split('\n')
    m = len(grid)
    n = len(grid[0])

frequencies = {}
for y in range(m):
    for x in range(n):
        char = grid[y][x]
        if char != '.':
            if char in frequencies:
                frequencies[char].append((x,y))
            else:
                frequencies[char] = [(x,y)]


anti_node_locations = set()
for x in frequencies:
    locations = frequencies[x] # locations of antenna x

    for i in range(len(locations)):
        x1,y1 = locations[i]
        for j in range(i+1, len(locations)):
            x2,y2 = locations[j]

            x1_new = x1 - (x2-x1)
            y1_new = y1 - (y2-y1)
            x2_new = x2 + (x2-x1)
            y2_new = y2 + (y2-y1)

            # add if within map
            if x1_new >= 0 and x1_new < n and y1_new >= 0 and y1_new < m:
                anti_node_locations.add((x1_new,y1_new))
            if x2_new >= 0 and x2_new < n and y2_new >= 0 and y2_new < m:
                anti_node_locations.add((x2_new, y2_new))

print(len(anti_node_locations)) # part 1: 400
