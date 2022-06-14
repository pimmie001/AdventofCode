with open("2.txt") as fh:
    instructions = fh.read().split("\n")


A = {(0,0):1, (-1,-1):2, (0,-1):3, (1,-1):4, (-2,-2):5, (-1,-2):6, (0,-2):7, (1,-2):8, (2,-2):9, (-1,-3):"A", (0,-3):"B", (1,-3):"C", (0,-4):"D"}

place = [-2,-2]
current = A[tuple(place)]

password = ""
for instruction in instructions:
    for x in instruction:
        old = current
        if x == "U":
            if A.get( (place[0], place[1] + 1) ) != None:
                current = A.get( (place[0], place[1] + 1) )
                place[1] += 1
        elif x == "D":
            if A.get( (place[0], place[1] - 1) ) != None:
                current = A.get( (place[0], place[1] - 1) )
                place[1] -= 1
        elif x == "L":
            if  A.get((place[0]-1,place[1])) != None:
                current = A.get((place[0]-1,place[1]))
                place[0] -= 1
        elif x == "R":
            if  A.get((place[0]+1,place[1])) != None:
                current = A.get((place[0]+1,place[1]))
                place[0] += 1
    password += str(current)

print(password)