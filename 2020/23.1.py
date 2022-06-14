with open("23.txt") as fh:
    content=fh.read()

cuplist=[]
for x in content:
    cuplist.append(int(x))
current=cuplist[0]
indexcurrent=cuplist.index(current)


loops=15
for loop in range(loops):
    if indexcurrent<len(cuplist)-3:
        pickup=cuplist[indexcurrent+1:indexcurrent+4]
    else: 
        pickup=[]
        possible=len(cuplist)-1-indexcurrent
        for i in range(indexcurrent+1,indexcurrent+1+possible):
            pickup.append(cuplist[i])
        for i in range(3-possible):
            pickup.append(cuplist[i])

    for number in pickup:
            cuplist.remove(number)
    destination=current-1
    while not destination in cuplist:
        if destination<min(cuplist):
            destination=max(cuplist)
            break
        destination-=1
    indexdestination=cuplist.index(destination)
    for i in range(len(pickup)):
        number=pickup[i]
        cuplist.insert(i+1+indexdestination,number)

    indexcurrent=cuplist.index(current) 
    if indexcurrent+1==len(cuplist):
        indexcurrent=0
    else:
        indexcurrent+=1
    current=cuplist[indexcurrent]

indexone=cuplist.index(1)
part1=cuplist[:indexone]
part2=cuplist[indexone+1:]
result=""
for number in part2:
    result+=str(number)
for number in part1:
    result+=str(number)

print(result)
