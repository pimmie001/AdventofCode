with open('1.txt') as fh:
    content = fh.read().split('\n\n')

A = []
for string in content:
    lst = string.split('\n')
    total = 0
    for x in lst:
        total += int(x)
    A.append(total)

print(max(A)) # part 1: 67633


B = sorted(A)
print(sum(B[-3:])) # part 2: 199628