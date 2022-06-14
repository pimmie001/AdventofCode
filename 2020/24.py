A=[]
def getpoint(line):
    nw=line.count("nw")
    ne=line.count("ne")
    se=line.count("se")
    sw=line.count("sw")
    w=line.count("w")-nw-sw
    e=line.count("e")-ne-se

    x,y=0,0
    x+=2*(e-w) + ne+se-sw-nw
    y+=ne+nw-sw-se
    point="({},{})".format(x,y)
    A.append(abs(x))
    A.append(abs(y))
    return point

with open("24.txt") as fh:
    lines=fh.read().split("\n")

dictionary={}
for line in lines:
    point=getpoint(line)
    if point in dictionary:
        dictionary[point]=1-dictionary[point]
    else:
        dictionary[point]=1

count=0
for point in dictionary:
    if dictionary[point]== 1:
        count+=1

# print(count)        # answer part 1: 320

biggest=max(A) + 5     ###
loops=100

for x in range(-(biggest+2*loops),biggest+2*loops+1):
    for y in range(-(biggest+loops),biggest+loops+1):
        point="({},{})".format(x,y)
        if not point in dictionary:
            dictionary[point]=0

for loop in range(loops):
    dictionary2=dictionary.copy()
    for x in range(-(biggest+2*loop),biggest+2*loop+1):
        for y in range(-(biggest+loop),biggest+loop+1):
            point="({},{})".format(x,y)
            blackcount=0
            # count how many adjacent black tiles
            for i in range(-1,2):
                for j in range(-1,2):
                    if i==0 or j==0:
                        continue
                    p="({},{})".format(x+i,y+j)
                    if dictionary[p]==1:
                        blackcount+=1
            peast="({},{})".format(x+2,y)
            pwest="({},{})".format(x-2,y)
            if dictionary[peast]==1:
                blackcount+=1
            if dictionary[pwest]==1:
                blackcount+=1

            if dictionary[point]==0:        # white
                if blackcount==2:
                    dictionary2[point]=1
            elif dictionary[point]==1:      # black
                if blackcount==0 or blackcount > 2:
                    dictionary2[point]=0

    dictionary=dictionary2

count2=0
for point in dictionary2:
    if dictionary2[point]== 1:
        count2+=1

print(count2)       # answer part 2: 3777, duurt 1-2 min 