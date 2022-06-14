from numpy import binary_repr as dectobin

def bintodec(n):
    n=str(n)
    decimal=0
    i=len(n)-1
    for x in n:
        if x=="1":
            decimal+=2**i
        i-=1
    return decimal

def newvalue(value,mask): # does the thing with the mask    
    binresult=""
    for i in range(len(mask)):
        if mask[i]=="X":
            binresult+=value[i]
        elif mask[i]=="0":
            binresult+="0"
        elif mask[i]=="1":
            binresult+="1"
    # returns value in decimal
    return bintodec((binresult.lstrip("0")))

with open("14.txt") as fh:
    instructions=fh.read().split("\n")

currentmask=""
dictionary={}

for instruction in instructions:
    instruction=instruction.split("=")
    part1=instruction[0].replace(" ","")
    part2=instruction[1].replace(" ","")

    if part1=="mask":
        currentmask=part2
    else:
        key=int(part1.replace("]","").split("[")[1])
        value=int(part2)
        value=str(dectobin(value))
        zerosneeded=36-len(value)
        string=""
        for i in range(zerosneeded):
            string+="0"
        value=string+value
        
        value2=newvalue(value,currentmask)
        dictionary[key]=value2
        
listofvalues=list(dictionary.values())
total=0
for number in listofvalues:
    total+= number
print(total)