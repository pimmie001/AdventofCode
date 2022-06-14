dimx = 50
dimy = 6

def rect(A,B,S):
    S2 = S.copy()
    for i in range(A):
        for j in range(B):
            S2[(i,j)] = 1
    return S2

def rotatecol(x,a,S):
    S2 = S.copy()
    for i in range(dimy):
        S2[(x,i)] = S[(x,(i-a) % dimy)]
    return S2

def rotaterow(y,a,S):
    S2 = S.copy()
    for i in range(dimx):
        S2[(i,y)] = S[((i-a) % dimx, y)]
    return S2

screen = {}
for i in range(dimx):
    for j in range(dimy):
        screen[(i,j)] = 0


with open("8.txt") as fh:
    instructions = fh.read().split("\n")

for x in instructions:
    x = x.split()
    if x[0] == "rect":
        A,B = x[1].split("x")
        screen = rect(int(A),int(B),screen)
    elif x[0] == "rotate":
        y = int(x[2].split("=")[1])
        a = int(x[-1])
        if x[1] == "column":
            screen = rotatecol(y,a,screen)
        else: 
            screen = rotaterow(y,a,screen)

count = 0
for key in screen.keys():
    if screen[key]: count += 1
print(count)       # 119


### part 2

for j in range(dimy):
    string = ""
    for i in range(dimx):
        if screen[(i,j)] == 1:
            string += "#"
        else: string += " "
        if i % 5 == 4:      # extra space after each letter for readability 
            string += " "
    print(string)