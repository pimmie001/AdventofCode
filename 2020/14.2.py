import itertools
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

def getalldifferences(A):
    result=[]
    for L in range(0, len(A)+1):
        for subset in itertools.combinations(A, L):
            total=0
            for i in range(len(subset)):
                total+=subset[i]
            result.append(total)       
    result=sorted(result)
    return result

def sumofallcobinations(result):
    A=""
    B=""
    for i in range(len(result)):
        if result[i]=="X":
            A+="0"
            B+="1"
        else:
            A+=result[i]
            B+="0"
    magic=result.count("X")
    return 2**magic*bintodec(int(A))+2**(magic-1)*bintodec(int(B))

def allevalues(result):
    A=""
    B=""
    for i in range(len(result)):
        if result[i]=="X":
            A+="0"
            B+="X"
        else:
            A+=result[i]
            B+="0"
    a=bintodec(A)
    xcount=B.count("X")
    positions=[0]*len(result)
    C=[]                    #lijst van alle getallen waarop x staat

    for i in range(len(B)):
        if B[i]=="X":
            positions[i]=1
    
    for i in range(len(positions)):
        if positions[i]==1:          # dus er stond een x op deze positie
            C.append(2**(len(positions)-1-i))
    C=sorted(C)
    alleverschillen=[]
    for i in range(len(C)-1):
        for j in range(i+1,len(C)):
            alleverschillen.append(C[i]+C[j])

    alleverschillen=getalldifferences(C)
    allevalues=[]
    for number in alleverschillen:
        x=number+a
        allevalues.append(x)

    return allevalues

def getresult(address,mask):
    result=""
    for i in range(len(address)):
        if mask[i]=="0":
            result+=address[i]
        elif mask[i]=="1":
            result+="1"
        elif mask[i]=="X":
            result+="X"
    return result

fh=open("14.txt")
content=fh.read().split("\n")
fh.close()

dictionary={}
currentmask=""
for instruction in content:
    instruction=instruction.replace(" ","").split("=")
    part1=instruction[0]
    part2=instruction[1]
    
    if part1=="mask":
        currentmask=part2
    else:
        address=part1.replace(']',"").replace("mem[","")
        thevalue=part2
        address=dectobin(int(address))
        string=""
        for i in range(len(currentmask)-len(address)):
            string+="0"
        address=string+address
        result=getresult(address,currentmask)
        
        allvalues=allevalues(result)
        
        for number in allvalues:
            dictionary[number]=thevalue

sumofvalues=0
B=list(dictionary.values())
for x in B:
    sumofvalues+=int(x)
print(sumofvalues)  # 4288986482164
