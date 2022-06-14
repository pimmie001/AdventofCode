fh=open("3.txt","r")
directions=fh.read()
fh.close

x=0
y=0

coordinates=["0,0"]
for i in range(len(directions)):
    direction=directions[i]
    
    if direction=="^":
        y+=1
    elif direction==">":
        x+=1
    elif direction=="<":
        x-=1
    elif direction=="v":
        y-=1

    string="{},{}".format(x,y)

    if not (string in coordinates):
        coordinates.append(string)

# print(coordinates)
print(len(coordinates))
