with open("16.txt") as fh:
    content=fh.read().split("\n\n")

content1=content[0].split("\n")
content2=content[2].split("\n")
content2=content2[1:]

listofvalidnumbers=[]
for line in content1:
    line=line.split(":")[1].replace(" ","").split("or")
    range1=line[0].split("-")
    range2=line[1].split("-")
    n1=int(range1[0])
    n2=int(range1[1])
    m1=int(range2[0])
    m2=int(range2[1])
    
    for i in range(n1,n2+1):
        if not i in listofvalidnumbers:
            listofvalidnumbers.append(i)
    for i in range(m1,m2+1):
        if not (i in listofvalidnumbers):
            listofvalidnumbers.append(i)

listofinvalidvalues=[]
errorrate=0
for line in content2:
    line=line.split(",")
    for number in line:
        number=int(number)
        if not number in listofvalidnumbers:
            errorrate+=number
            listofinvalidvalues.append(number)

print("answer part 1:",errorrate) # answer part 1: 20058

with open("16.txt") as fh:
    content3=fh.read()

content3=content3.split("nearby tickets:")
content4=content3[1].split("\n")
if content4[0]=="":
    content4=content4[1:]

listofvalidtickets=[]
for line in content4:
    line2=line.split(",")
    dummy=1
    for number in line2:
        if int(number) in listofinvalidvalues:
            dummy=0
    if dummy==1:
        listofvalidtickets.append(line)

content5=content3[0]
myticket=content5.split("your ticket:")[1].replace("\n","")
listofvalidtickets.insert(0,myticket)

myList=[]
for i in range(len(listofvalidtickets[0].split(","))):
    littlelist=[]
    for ticket in listofvalidtickets:
        ticket=ticket.split(",")
        littlelist.append(int(ticket[i]))
    myList.append(littlelist)

content6=content3[0]
content6=content6.split("\n\nyour ticket:")[0].split("\n")
numberofpositions=len(content6)
positionsinorder={}
orderedvalidnumbers=[]
for line in content6:
    line=line.split(": ")
    positionsinorder[line[0]]=-1
    line2=line[1].split(" or ")
    
    littlelist=[]
    for x in line2:
        x=x.split("-")
        for number in range(int(x[0]),int(x[1])+1):
            littlelist.append(number)
    orderedvalidnumbers.append(littlelist)

listofindexes={}
for i in range(numberofpositions):
    listofindexes[i]=[]

for i in range(numberofpositions):
    List=myList[i]
    for j in range(numberofpositions):
        checklist=orderedvalidnumbers[j]  
        dummy=1
        for number in List:
            if not number in checklist:
                dummy=0
        if dummy==1:
            A=listofindexes[i]
            A.append(j)
            listofindexes[i]=A

possibilities=[]
for i in listofindexes:
    possibilities.append(len(listofindexes[i]))

remaining=[]
for i in range(numberofpositions):
    remaining.append(i)

for i in range(numberofpositions):
    index=possibilities.index(i+1)
    # position=list(positionsinorder.keys())[i]
    thelist=listofindexes[index]
    for number in thelist:
        if number in remaining:
            position=list(positionsinorder.keys())[number]
            positionsinorder[position]=index
            remaining.remove(number)

product=1
# multiply value for all positions which contain 'departure'
for i in range(numberofpositions):
    position=list(positionsinorder.keys())[i]
    if "departure" in position:
        index=positionsinorder[position]
        ticket=myticket.split(",")
        product*= int(ticket[index])

print("answer part 2:",product)      # answer part 2: 366871907221

print(listofindexes)