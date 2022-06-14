file=open("1.txt","r") 
numbers=file.readlines()
file.close()
list2=[]

for number in numbers:
    number=number.strip("\n")
    number=number.strip(" ' ")
    # print(number)
    list2.append(number)
    


for i in list2:
    for j in list2:
        for k in list2:
            if int(i)+int(j)+int(k)==2020:
                x=int(i)
                y=int(j)
                z=int(k)
                break

print("The numbers are: ")
print(x)
print(y)
print(z)
print("The product of these numbers is",x*y*z)
