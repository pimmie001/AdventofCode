def minmax(a):
    a=a.split()
    a1=a[0]     # min-max
    a11=a1.split("-")
    minimum=a11[0]
    maximum=a11[1]
    minimum=minimum.replace("'","")
    return [minimum,maximum]

def letter(a):
    a=a.split()
    a=a[1]
    a=a.replace(":","")
    return a
    
def password(a):
    a=a.split()
    a=a[2]
    a=a.replace("'","")
    return a

file = open("2.txt","r")
content=file.readlines()
file.close()

content2=[]
for i in content:
    i=i.strip("\n")
    content2.append(i)

validcount=0
a=content2[0]

for x in range(len(content2)):
    y=content2[x]
    y=str(y)
    minimum=minmax(y)[0]
    maximum=minmax(y)[1]
    let=letter(y)
    passw=password(y)
    count=passw.count(let)
    if count>=int(minimum) and count<=int(maximum):
        validcount+=1
   
    
print(validcount)



