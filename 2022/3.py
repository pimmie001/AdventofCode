import string
alp = list(string.ascii_lowercase)
ALP = list(string.ascii_uppercase)

with open('3.txt') as fh:
    content = fh.read().split('\n')

priorities = []
for line in content:
    n = len(line)//2
    half1, half2 = line[:n], line[n:]

    letter = list(set(half1).intersection(half2))[0]

    if letter in alp:
        priorities.append(1 + alp.index(letter))
    else:
        priorities.append(27 + ALP.index(letter))

print(sum(priorities)) # part 1: 8018



groups = []
for i in range(len(content)):
    if i % 3 == 0:
        if i != 0:
            groups.append(lines)
        lines = []
    lines.append(content[i])
groups.append(lines)


total = 0
for group in groups:
    a,b,c = group

    letter = list(set(a).intersection(b).intersection(c))[0]

    if letter in alp:
        total += 1 + alp.index(letter)
    else:
        total += 27 + ALP.index(letter)

print(total) # part 2: 2518