fh=open("9.txt")
listofnumbers=fh.read().split()
fh.close

for i in range(len(listofnumbers)):         
    listofnumbers[i]=int(listofnumbers[i])

def valid(validlist,number):
    for i in validlist:
        for j in validlist:
            if i==j:
                continue
            if i+j==number:
                return True
    return False

preamble = 25                           # change to 25
for i in range(preamble,len(listofnumbers)):
    validlist=listofnumbers[i-preamble:i]
    number=listofnumbers[i]
    if not valid(validlist,number):
        wrongnumber=number
        print(number)               

# part 2
for i in range(listofnumbers.index(wrongnumber)):
    list2=[]
    j=i
    total=0
    while total<wrongnumber:
        number=listofnumbers[j]
        list2.append(number)
        total+=number
        if total==wrongnumber:
            thelist=list2
            break
        j+=1

thelist.sort()
print(thelist[0]+thelist[-1])