fh=open("3.txt","r")
directions=fh.read()
fh.close

xsanta=0
ysanta=0
xrobot=0
yrobot=0

coordinates=["0,0"]
k=1                         # odd/even
for i in range(len(directions)):
    direction=directions[i]

    if k%2==1:
        if direction=="^":
            ysanta+=1
        elif direction==">":
            xsanta+=1
        elif direction=="<":
            xsanta-=1
        elif direction=="v":
            ysanta-=1
        string="{},{}".format(xsanta,ysanta)
        if not (string in coordinates):
            coordinates.append(string)

    elif k%2==0:
        if direction=="^":
            yrobot+=1
        elif direction==">":
            xrobot+=1
        elif direction=="<":
            xrobot-=1
        elif direction=="v":
            yrobot-=1
        string="{},{}".format(xrobot,yrobot)
        if not (string in coordinates):
            coordinates.append(string)

    k+=1                # odd/even


# print(coordinates)
print(len(coordinates))
