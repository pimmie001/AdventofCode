def countneighbors(location,lights):
    result = 0
    x = location[0]
    y = location[1]

    for i in range(-1,2):
        for j in range(-1,2):
            if i == j == 0:
                continue
            # print( lights.get((x+i,y+j),0) )
            if lights.get( (x+i,y+j) ,0 ):
                result += 1

    return result



with open("18.txt") as fh:
    content = fh.read().split("\n")

ylen = len(content)
xlen = len(content[0])


lights = {}
for y in range(len(content)):
    line = content[y]
    for x in range(len(line)):
        loc = line[x]
        if loc == ".":
            lights[(x,y)] = 0
        else:
            lights[(x,y)] = 1

loops = 100 
for loop in range(loops):
    newlights = lights.copy()
    for x in range(xlen):
        for y in range(ylen):
            if lights[(x,y)]:
                if not ( countneighbors((x,y),lights) == 2 or countneighbors((x,y),lights) == 3 ):
                    newlights[(x,y)] = 0
            else:
                if countneighbors((x,y),lights) == 3:
                    newlights[(x,y)] = 1
    lights = newlights.copy()


print(sum(newlights.values()))