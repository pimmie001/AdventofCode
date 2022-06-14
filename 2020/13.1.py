with open("13.txt") as fh:
    content=fh.read().split("\n")

arrival=int(content[0])
list1=content[1].split(",")
listofbusses=[]
for x in list1:
    if x=="x":
        continue
    else:
        listofbusses.append(int(x))

earliestbustimes=[0]*len(listofbusses)

for x in listofbusses:
    i=0
    while True:
        if i*x>=arrival:
            earliestbustimes[listofbusses.index(x)]=i*x
            break
        i+=1

earliest=min(earliestbustimes)
bestbus=listofbusses[ earliestbustimes.index(earliest)]

print((earliest-arrival)*bestbus)