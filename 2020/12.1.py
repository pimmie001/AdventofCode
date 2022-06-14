with open("12.txt") as fh:
    content=fh.read()
instructions=content.split("\n")

directions=["N","E","S","W"]
face="E"    #starts facing east
x,y=0,0
for element in instructions:
    instruction=element[0]
    number=int(element[1:])
    if instruction=="F": 
        instruction=face
    
    if instruction=="N":
        y+=number
    elif instruction=="E":
        x+=number
    elif instruction=="S":
        y-=number
    elif instruction=="W":
        x-=number
    elif instruction=="R":
        Q=number/90
        currentindex=directions.index(face)+1   
        newindex=int((currentindex+Q)%4)
        face=directions[newindex-1]           
    elif instruction=="L":
        Q=number/90
        currentindex=directions.index(face)+1
        newindex=int((currentindex-Q+4)%4)
        face=directions[newindex-1]

print("coordinates {},{} give Manhattan distance: {}".format(x,y,abs(x)+abs(y)))