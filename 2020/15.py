with open("15.txt") as fh:
    content=fh.read().split(",")

dictionary={}
i=1
for number in content:
    number=int(number)
    dictionary[number]=[1,[i]]
    i+=1
lastspoken=int(content[-1])
count=len(content)      # how many turns already passed

n=3000000
for turn in range(count+1,n+1):
    if dictionary[lastspoken][0] == 1:
        number = 0
    else:
        number = dictionary[number][1][1] - dictionary[number][1][0]
    
    if number in dictionary:
        dictionary[number]=[dictionary[number][0]+1,[dictionary[number][1][-1],turn]]
    else:
        dictionary[number]=[1,[turn]]
    lastspoken=number

print(lastspoken)

# answer part 1: 1665
# answer part 2: 16439