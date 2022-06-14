fh=open("10.txt")
listofadapters=fh.read().split()
fh.close

for x in range(len(listofadapters)):
    listofadapters[x]=int(listofadapters[x])
listofadapters.append(0)
listofadapters.sort()
listofadapters.append(listofadapters[-1]+3)

count1,count2,count3=0,0,0
for i in range(len(listofadapters)-1):
    difference=listofadapters[i+1]-listofadapters[i]
    if difference==1:
        count1+=1
    elif difference==2:
        count2+=1
    elif difference==3:
        count3+=1

print(count1*count3) # 2046
