import itertools

with open("24.txt") as fh:
    input = fh.read().split("\n")
for i in range(len(input)): input[i] = int(input[i])

######
n = 4           # '3' for part 1 and '4' for part 2
######

weight = sum(input)//n
Groups = []

i = 1
while True:
    combis = list(itertools.combinations(input,i))
    for x in combis:
        if sum(x) == weight:
            Groups.append(x)

    if Groups != []:
        break
    i += 1

QE = []
for x in Groups:
    product = 1
    for y in x:
        product *= y
    QE.append(product)

print(min(QE))