fh=open("1.txt","r")
a=fh.read()
fh.close

floor=0
i=1
while True:
    if a[i-1]=="(":
        floor+=1
    else:
        floor-=1

    if floor == -1:
        print(i)
        break
    i+=1



