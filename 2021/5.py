from sre_constants import NEGATE
import numpy as np
import re

with open ('5.txt') as fh:
    input = fh.read().split('\n')

x = np.empty((len(input), 4), dtype = object)

for i in range(len(input)):
    x[i, :] = re.split(' -> |,', input[i])
x = x.astype(int)

y = np.zeros((np.amax(x) + 1, np.amax(x) + 1), dtype = int)
for i in range(np.shape(x)[0]):
    x1, y1, x2, y2 = x[i,:]
    if x1 == x2:
        ymin = min(y1,y2)
        ymax = max(y1,y2)
        y[x1, ymin:ymax+1] += 1
    elif y1 == y2:
        xmin = min(x1,x2)
        xmax = max(x1,x2)
        y[xmin:xmax+1, y1] += 1

print(np.sum(y >= 2)) # 5294


### part 2

for i in range(np.shape(x)[0]):
    x1, y1, x2, y2 = x[i,:]
    if (x1 != x2) and (y1 != y2): # now only consider diagnal lines
        nopoints = abs(x1 - x2) + 1 # number of points
        for j in range(nopoints):
            if x1 < x2:
                if y1 < y2:
                    y[x1 + j, y1 + j] += 1
                elif y1 > y2:
                    y[x1 + j, y1 - j] += 1
            
            elif x1 > x2:
                if y1 < y2: 
                    y[x2 +j, y2 - j] += 1
                elif y1 > y2:
                    y[x2 + j, y2 + j] += 1

print(np.sum(y >= 2)) # 21698