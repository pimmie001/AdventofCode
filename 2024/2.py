import numpy as np

A = []

with open("2.txt") as fh:
    for line in fh:
        A.append(list(map(int, line.split())))


def is_valid(x):
    return (np.all(np.diff(x) > 0) and np.diff(x).max() <= 3) or (np.all(np.diff(x) < 0) and np.diff(x).min() >= -3)


count = 0
for x in A:
    count += is_valid(x)
print(count) # part 1: 379


### part 2
count2 = 0
for x in A:
    for i in range(len(x)):
        y = x.copy()
        y.pop(i)
        if is_valid(y):
            count2 += 1
            break
print(count2) # part 2: 430
