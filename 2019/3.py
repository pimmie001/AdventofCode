with open("3.txt") as file:
    content=file.read().split("\n")
instructions1=content[0].split(",")
instructions2=content[1].split(",")

pathwire1=[]
steps1={}
step=0
x,y=0,0     
for instruction in instructions1:
    direction=instruction[0]
    value=int(instruction[1:])
    if direction=="R":
        for i in range(value):
            x+=1
            pathwire1.append((x,y))
            step+=1
            steps1[(x,y)]=step
    elif direction=="D":
        for i in range(value):
            y-=1
            pathwire1.append((x,y))
            step+=1
            steps1[(x,y)]=step
    elif direction=="L":
        for i in range(value):
            x-=1
            pathwire1.append((x,y))
            step+=1
            steps1[(x,y)]=step
    elif direction=="U":
        for i in range(value):
            y+=1
            pathwire1.append((x,y))
            step+=1
            steps1[(x,y)]=step

pathwire2=[]
steps2={}
step=0
x,y=0,0     
for instruction in instructions2:
    direction=instruction[0]
    value=int(instruction[1:])
    if direction=="R":
        for i in range(value):
            x+=1
            pathwire2.append((x,y))
            step+=1
            steps2[(x,y)]=step
    elif direction=="D":
        for i in range(value):
            y-=1
            pathwire2.append((x,y))
            step+=1
            steps2[(x,y)]=step
    elif direction=="L":
        for i in range(value):
            x-=1
            pathwire2.append((x,y))
            step+=1
            steps2[(x,y)]=step
    elif direction=="U":
        for i in range(value):
            y+=1
            pathwire2.append((x,y))
            step+=1
            steps2[(x,y)]=step

intersections=list(set(pathwire1).intersection(pathwire2))

distances=[]
for point in intersections:
    distance=0
    for number in point:
        distance+=abs(number)
    distances.append(distance)

print(min(distances))   # answer part 1: 731

distancetraveled=[]
for point in intersections:
    n1= steps1[point]
    n2= steps2[point]
    distancetraveled.append(n1+n2)
print(min(distancetraveled))    # answer part 2: 5672