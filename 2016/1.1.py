with open("1.txt") as fh:
    instructions = fh.read().split(", ")

h,v = 0,0
direction = 0       # 0,1,2,3 = N,E,S,W (start facing north)

for x in instructions:
    y = x[0]        # left or right
    z = int(x[1:])  # amount of steps

    direction += 1 if y=="R" else -1
    direction %= 4
    
    if direction == 0:
        h += z
    elif direction == 1:
        v += z
    elif direction == 2:
        h -= z
    elif direction == 3:
        v -= z


print(abs(h)+abs(v)) # 299