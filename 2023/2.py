import re

with open('2.txt') as fh:
    content = fh.read().split('\n')


allowed = {'red':12, 'green':13, 'blue':14}

def valid(A):
    for x in A:
        n, color = x.split(' ')
        if int(n) > allowed[color]:
            return False
    return True


count = 0
for id,line in enumerate(content):
    line = line.split(': ')[1]
    A = re.split(', |; ', line)

    count += (id+1) * valid(A)

print(count) # part 1: 2720



def power(A):
    minimum = {'red':0, 'green':0, 'blue':0}
    for x in A:
        y = x.split(', ')
        for z in y:
            n, color = z.split(' ')
            minimum[color] = max(minimum[color], int(n))

    prod = 1
    for color in minimum:
        prod *= minimum[color]
    return prod


total = 0
for id,line in enumerate(content):
    A = line.split(': ')[1].split('; ')

    total += power(A)

print(total) # part 2: 71535
