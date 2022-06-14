file=open("1.txt","r") 
numbers=file.readlines()
file.close()
list2=[]

for number in numbers:
    number=number.strip("\n")
    number=number.strip(" ' ")
    list2.append(number)
    
for i in list2:
    for j in list2:
        if int(i)+int(j)==2020:
            x=int(i)
            y=int(j)
            break

print("The numbers are: ")
print(x)
print(y)
print("The product of these numbers is",x*y)
