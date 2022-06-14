fh=open("6.txt","r")
content=fh.read()
fh.close
instructions=content.split("\n")

biglist=[]        # biglist[x][y]
for i in range(1000):
    j=[0]*1000
    biglist.append(j)

for i in instructions:
    j=i.split()
    instruction=j[0]
    if instruction=="turn":
        instruction+=" "+j[1]
        coordinates1=j[2]
        coordinates2=j[4]
    else:
        coordinates1=j[1]
        coordinates2=j[3]
    
    startco=coordinates1.split(",")
    start_x=int(startco[0])
    start_y=int(startco[1])
    endco=coordinates2.split(",")
    end_x=int(endco[0])
    end_y=int(endco[1])
    
    if instruction == "toggle":
        for x in range(start_x,end_x+1):
            for y in range(start_y, end_y+1):
                biglist[x][y]=1-biglist[x][y]

    elif instruction == "turn on":
        for x in range(start_x,end_x+1):
            for y in range(start_y, end_y+1):
                biglist[x][y]=1
    
    elif instruction == "turn off":
        for x in range(start_x,end_x+1):
            for y in range(start_y, end_y+1):
                biglist[x][y]=0

lightcount=0
for x in range(len(biglist)):
    for y in range(len(biglist)):
        if biglist[x][y]==1:
            lightcount+=1

print(lightcount)