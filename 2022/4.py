import re
import numpy as np

with open('4.txt') as fh:
    content = fh.read().split('\n')

total = 0
total2 = 0 
for line in content:
    x = re.split('[,-]', line)
    x = np.array(x, dtype=int)

    if (x[0] <= x[2] and x[1] >= x[3]) or (x[0] >= x[2] and x[1] <= x[3]):
        total += 1

    if not (x[1] < x[2] or x[0] > x[3]):
        total2 += 1

print(total) # part 1: 477
print(total2) # part 2: 830
