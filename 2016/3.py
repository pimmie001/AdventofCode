def valid(A):
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if A[i] + A[j] <= A[3-i-j]:
                return False
    return True

with open("3.txt") as fh:
    content = fh.read().split("\n")

count = 0
for x in content:
    x = x.split()
    for i in range(len(x)): x[i] = int(x[i])
    if valid(x): count += 1

print("Part 1: ",count)

#### Part 2

count2 = 0
for i in range(3):

    y = []
    j = 0
    while j < len(content):
        y.append(int(content[j].split()[i]))

        if j % 3 == 2:
            if valid(y): count2 += 1
            y = []

        j += 1
    

print("Part 2: ",count2)