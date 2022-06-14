fh=open("2.txt","r")
a=fh.readlines()
b=fh.readline()
fh.close

feetcount=0
ribboncount=0
for i in range(len(a)):
    x=a[i]
    x=x.replace("\n","")
    y=x.split("x")
    y1=int(y[0])
    y2=int(y[1])
    y3=int(y[2])
    Y=[y1,y2,y3]
    ymin=min(Y)
    if y1==ymin:            # meest lompe if else statement om de op 1 na kleinste variable te ontdekken
        ymin2=min(y2,y3)
    elif y2==ymin:
        ymin2=min(y1,y3)
    elif y3==ymin:
        ymin2=min(y1,y2)

    feetcount+=2*(y1*y2+y2*y3+y1*y3)
    feetcount+=ymin*ymin2
    ribboncount+=2*(ymin+ymin2)
    ribboncount+=y1*y2*y3

print("feetcount is: ",feetcount)           # answer part 1
print("ribboncount is: ",ribboncount)       # answer part 2