fh=open("3.txt","r")
abc=fh.readlines()
ab=[]
for x in abc:
    x=x.replace("\n","")
    ab.append(x)

a=ab[1:]



x=0
count=0
for y in a:
    x+=7
    xx=x%len(y)
    if y[xx]=="#":
        count+=1




x=0
count=0
i=1
for y in a:
    if i%2==1:
        i+=1
        continue
    else:
        i+=1
        x+=1
        xx=x%len(y)
        if y[xx]=="#":
            count+=1



yeet=[82,242,71,67,24]

multi=82*242*71*67*24
print(multi)