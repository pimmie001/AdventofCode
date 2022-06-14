import math
def findinverse(number,m):    # should return value x such that number*x '=' 1 (mod m)
    if m==1:
        return 1
    number%=m
    i=1
    while True:                 # kleinste integer i zodat i*number/ m een rest van 1 overhoud
        if (i*number) % m==1:
            return i
        i+=1

with open("13.txt") as fh:
    content=fh.read().split("\n")[1]
content=content.split(",")

ni=[]                   
for x in content:
    if x=="x":
        continue
    else:
        ni.append(int(x))

listofindexes=[]        
for number in ni:
    number=str(number)
    x=content.index(number)
    listofindexes.append(x)

bi=[]                   
for i in range(len(ni)):
    index=-listofindexes[i]
    mod=ni[i]
    while index<0:
        index+=mod
    bi.append(index)

N=1
for number in ni:
    N*=number

Ni=[]
for i in range(len(ni)):
    x=N//ni[i]
    Ni.append(x)

xi=[]
for i in range(len(Ni)):
    number=Ni[i]
    mod=ni[i]
    y=findinverse(number,mod)
    xi.append(y)

P=[]
for i in range(len(Ni)):
    x=bi[i]*Ni[i]*xi[i]
    P.append(x)

S=0
for number in P:
    S+=number

finalanswer=S%N

print("\nbi is:",bi)
print("ni is:",ni)
print("N is:",N)
print("Ni is:",Ni)
print("xi is:",xi)
print("P is:",P)
print("S is: {}\n".format(S))
print("final answer is: {}\n".format(finalanswer))
# 939490236001473

# i=7
# print("bi: {}, Ni: {}, xi: {}".format(bi[i],Ni[i],xi[i]))

# input lesley: 37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,601,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,23,x,x,x,x,x,29,x,443,x,x,x,x,x,x,x,x,x,x,x,x,13
