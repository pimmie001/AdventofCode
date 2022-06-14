def f(A):
    # finds first double item in an ordered list
    for i in range(len(A)):
        for j in range(i):
            if A[i] == A[j]:
                return A[i]

    return None


with open("1.txt") as fh:
    instructions = fh.read().split(", ")

h,v = 0,0
direction = 0       # 0,1,2,3 = N,E,S,W (start facing north)
Locations = [(0,0)]


for x in instructions:
    y = x[0]        # left or right
    z = int(x[1:])  # amount of steps

    direction += 1 if y=="R" else -1
    direction %= 4
    
    if direction == 0:
        for j in range(z):
            v += 1
            Locations.append((h,v))
    elif direction == 1:
        for j in range(z):
            h += 1
            Locations.append((h,v))
    elif direction == 2:
        for j in range(z):
            v -= 1
            Locations.append((h,v))
    elif direction == 3:
        for j in range(z):
            h -= 1
            Locations.append((h,v))

dest = f(Locations)
print(abs(dest[0]) + abs(dest[1])) # 181



