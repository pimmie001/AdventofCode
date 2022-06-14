with open("2.txt") as file:
    intcode=file.read().split(",")
for i in range(len(intcode)):
    intcode[i]=int(intcode[i])
intcode[1]=12   # given
intcode[2]=2

def Intcode(intcode):
    i=0
    while True:
        number=intcode[i]
        if number == 1:
            source1=intcode[i+1]
            source2=intcode[i+2]
            n1=intcode[source1]
            n2=intcode[source2]
            target=intcode[i+3]
            intcode[target]=n1+n2
            i+=4
        elif number == 2:
            source1=intcode[i+1]
            source2=intcode[i+2]
            n1=intcode[source1]
            n2=intcode[source2]
            target=intcode[i+3]
            intcode[target]=n1*n2
            i+=4
        elif number == 99:
            return intcode[0]

print(Intcode(intcode))       # answer part 1: 3306701


# part 2: find noun and verb s.t. intcode[0] = 19690720
with open("2.txt") as file:
    intcode2=file.read().split(",")
for i in range(len(intcode2)):
    intcode2[i]=int(intcode2[i])

for i in range(0,100):
    for j in range(0,100):
        copy=intcode2.copy()
        copy[1]=i
        copy[2]=j
        if Intcode(copy) == 19690720:
            noun=i
            verb=j
            break
print(100*noun + verb)      # answer part 2: 7621
        




