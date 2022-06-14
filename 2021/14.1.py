from typing import Counter

with open('14.txt') as fh:
    content = fh.read().split("\n\n")

poly = content[0]
instructions = content[1].split('\n')

D = {}
for x in instructions:
    y = x.split(' -> ')
    D[y[0]] = y[1]

def add(string):
    A = []
    for i in range(len(string) - 1):
        letter = D[string[i]+string[i+1]]
        A.append(letter)

    newstring = string[0]
    for i in range(len(string) - 1):
        newstring += A[i]
        newstring += string[i+1]

    return newstring


n = 10
for i in range(n):
    poly = add(poly)

C = Counter(poly)
values = C.values()
print(max(values) - min(values)) # 3555

print(len(poly))