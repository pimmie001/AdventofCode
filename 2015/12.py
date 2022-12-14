import re

with open("12.txt") as fh:
    content = fh.read()

A = [int(x) for x in re.findall('[-0-9]+', content)]
print(sum(A)) # part 1: 111754


### part 2:

total = 0
def count(A):
    global total

    if type(A) == list:
        for x in A:
            count(x)

    elif type(A) == dict:
        if 'red' not in A and 'red' not in A.values():
            for x in A:
                count(x)
                count(A[x])

    elif type(A) == int:
        total += A


A = eval(content)
count(A)
print(total) # part 2: 65402
