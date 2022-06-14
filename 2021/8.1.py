with open('8.txt') as fh:
    content = fh.read().split("\n")

A = {1:2, 4:4, 7:3, 8:7}
y = A.values()

count = 0
for x in content:
    x2 = x.split(' | ')[1].split(' ')
    for x3 in x2:
        if len(x3) in y:
            count += 1

print(count) # part 1: 534
