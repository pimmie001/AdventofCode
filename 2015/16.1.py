with open("16.txt") as fh:
    content = fh.read().split("\n")

with open("16info.txt") as fh:
    content2 = fh.read().split("\n")

info = {}
for x in content2:
    x = x.split()
    info[x[0].replace(":","")] = int(x[1])


for i in range(len(content)):
    x = content[i][7:].split(",")
    x = content[i].split(":",1)[1].replace(" ","").split(",")

    correct = True
    for y in x:
        y = y.split(":")
        type = y[0]
        number = int(y[1])
        if info[type] != number:
            correct = False
            break

    if correct: 
        print("Part 1: ",i + 1)    
        

### part 2

for i in range(len(content)):
    x = content[i][7:].split(",")
    x = content[i].split(":",1)[1].replace(" ","").split(",")

    correct = True
    for y in x:
        y = y.split(":")
        type = y[0]
        number = int(y[1])
        
        if "cats" in type or "trees" in type:
            if info[type] >= number:
                correct = False
                break
        elif "pomeranians" in type or "goldfish" in type: 
            if info[type] <= number:
                correct = False
                break
        else: 
            if info[type] != number:
                correct = False
                break

    if correct: 
        print("Part 2: ",i + 1)  

