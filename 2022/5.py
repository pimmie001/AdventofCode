import re
from copy import deepcopy

with open('5.txt') as fh:
    layout, instructions = fh.read().split('\n\n')
layout=layout.split('\n')
instructions = instructions.split('\n')


n = 9
A = [[] for x in range(n)]

# create initial setup:
for line in layout[-2::-1]:
    i = 0
    for j in range(0, n):
        test = line[i:i+3]
        if line[i:i+3] == ' '*3:
            pass
        else:
            A[j].append(line[i+1])
        i += 4
A2 = deepcopy(A)


def move(A, times, a, b):
    # part 1
    for i in range(times):
        item = A[a].pop()
        A[b].append(item)


def move2(A, amount, a, b):
    # part 2
    items = A[a][-amount:]
    A[a] = A[a][:-amount]
    A[b].extend(items)



for line in instructions:
    x = re.findall('[0-9]+', line)
    move(A, int(x[0]), int(x[1])-1, int(x[2])-1)
    move2(A2, int(x[0]), int(x[1])-1, int(x[2])-1)


string = ''
string2 = ''
for i in range(n):
    string += A[i][-1]
    string2 += A2[i][-1]
print(string) # part 1: PTWLTDSJV
print(string2) # part 2: WZMFVGGZP
