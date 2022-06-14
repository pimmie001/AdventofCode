fh=open("3.txt","r")
abc=fh.readlines()
ab=[]
count=0
for x in abc:
    x=x.replace("\n","")
    ab.append(x)

a=ab[1:]

x=0
for y in a:
    x+=3
    xx=x%len(y)
    if y[xx]=="#":
        count+=1
      
print(count)
