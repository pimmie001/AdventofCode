import math
with open("12.txt") as fh:
    content=fh.read()
instructions=content.split("\n")

directions=["N","E","S","W"]
face="E"    #starts facing east
x,y=0,0
xw,yw=10,1  # starting position waypoint
for element in instructions:
    instruction=element[0]
    number=int(element[1:])

    if instruction=="F":
        x+=number*xw
        y+=number*yw
    
    elif instruction=="N":
        yw+=number
    elif instruction=="E":
        xw+=number
    elif instruction=="S":
        yw-=number
    elif instruction=="W":
        xw-=number

    elif instruction=="R":  
        radians=-number*math.pi/180     #rechts is een negatieve draairichting daarom de min
        xnew=xw*math.cos(radians)-yw*math.sin(radians)
        ynew=xw*math.sin(radians)+yw*math.cos(radians)
        xw=round(xnew)
        yw=round(ynew)
    elif instruction=="L":
        radians=number*math.pi/180
        xnew=xw*math.cos(radians)-yw*math.sin(radians)
        ynew=xw*math.sin(radians)+yw*math.cos(radians)
        xw=round(xnew)
        yw=round(ynew)

print("coordinates {},{} give Manhattan distance: {}".format(x,y,abs(x)+abs(y)))