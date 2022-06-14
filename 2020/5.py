fh=open("5.txt","r")
content=fh.read()
fh.close
content=content.split()

allseatid=[]
for seat in content:
    rows=seat[:7]
    columns=seat[7:]
    row,column=0,0

    for i in range(len(rows)):
        if rows[i]=="B":
            row+=2**(6-i)

    for i in range(len(columns)):
        if columns[i]=="R":
            column+=2**(2-i)

    seatid=8*row+column
    allseatid.append(seatid)

print(max(allseatid))     # answer to part 1

for row in range(127):
    for column in range(7):
        seat=8*row+column
        if not(seat in allseatid) and seat<=max(allseatid) and seat>50:
            print(seat)     # answer part 2