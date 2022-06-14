fh=open("7.txt")
content2=fh.read()
fh.close()
content=content2.split("\n")

dictionary={}
for line in content:
    line=line.replace("bags",",").replace("bag",",").replace("contain ","").replace(" , ",",").replace(" ,.","").replace(" ,, ",",")
    line=line.replace(" ,, ",",").replace(" ,","").replace("no other","no_other").split(",")
    bag=line[0]
    contains=line[1:]
    howmany=[]
    A=[]
    B=[]
    for x in contains:
        if "no_other" in x: 
            A.append(x)
            B.append(1)
        else:
            number=int(x[0])
            y=x[2:]
            A.append(y)
            B.append(number)
    dictionary[bag]=[A,B]

def howmanybagsinside(bag):
    count=0
    bags=dictionary[bag][0]
    numbers=dictionary[bag][1]
    for i in range(len(bags)):
        number=numbers[i]
        bag=bags[i]
        if bag == "no_other":
            return 0
        count+= number + number*howmanybagsinside(bag)
    return count

print(howmanybagsinside("shiny gold"))      # 220149
