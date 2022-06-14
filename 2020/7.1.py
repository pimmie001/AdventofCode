def hasshinygold(bag): # prints true if the bag itself or any of the bags in the bag (and the bags in that bag...) contains a shiny gold bag
    contains=dictionary[bag]
    boolian=False
    for x in contains:
        if boolian==True:       # zodat de boolian niet word vervangen door false als in de 2e bag niet de golden zit maar de eerste wel
            return True
        if x == "shiny gold":
            return True
        elif x != "no other":
                boolian = hasshinygold(x)
    return False or boolian 
   
fh=open("7.txt")
content2=fh.read()
fh.close()
content=content2.split("\n")

listofnumbers=[]
listofbags=[]
listofinstructions=[]

for letter in content2:
    try:
        number=int(letter)
        if not(number in listofnumbers):
            listofnumbers.append(number)
    except:
        continue
maxnumber=max(listofnumbers)    

for line in content:
    line=line.replace("bags",",").replace("bag",",").replace("contain ","").replace(" , ",",").replace(" ,.","").replace(" ,, ",",")
    for i in range(1,maxnumber+1):
        line=line.replace(str(i),"")
    line=line.replace(", ",",")
    bags=line.split(",")
    for bag in bags:
        if not(bag in listofbags):
            listofbags.append(bag)
    listofinstructions.append(line)

dictionary={}
for line in listofinstructions:
    line=line.split(",")
    bag=line[0]
    bag2=line[1:]
    dictionary[bag]=bag2

shinycount=0
for bag in dictionary:
    if hasshinygold(bag):
        shinycount+=1

print(shinycount)   # 126