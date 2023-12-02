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



