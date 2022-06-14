size=8+6        #
A={}
for x in range(-size,size+1):
    for y in range(-size,size+1):
        for z in range(-size,size+1):
            point="({},{},{})".format(x,y,z)
            A[point]=0

with open("17.txt") as fh:
    content=fh.read().split("\n")

for i in range(len(content)):
    for j in range(len(content[0])):
        state=content[i][j]
        point="({},{},{})".format(j,i,0)
        if state=="#":
            A[point]=1
Anew={}
for loop in range(6):
    for z in range(-size+1,size):
        for y in range(-size+1,size):
            for x in range(-size+1,size):
                point="({},{},{})".format(x,y,z)
                activecount=0
                for k in range(-1,2):
                    for j in range(-1,2):
                        for i in range(-1,2):
                            if i==j==k==0:  # niet zichzelf meetellen
                                continue 
                            p2="({},{},{})".format(x+i,y+j,z+k)
                            try:
                                if A[p2]==1:
                                    activecount+=1
                            except:
                                pass

                if A[point]==1:       # active
                    if activecount==2 or activecount==3:
                        Anew[point]=1
                    else:
                        Anew[point]=0
                elif A[point]==0:     # unactive
                    if activecount==3:
                        Anew[point]=1
                    else:
                        Anew[point]=0
    A=Anew.copy()

totalcount=0
for key in Anew:
    if Anew[key]==1:
        totalcount+=1
print(totalcount)       # answer part 1: 391
