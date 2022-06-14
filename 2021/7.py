import numpy as np

with open('7.txt') as fh:
    content = fh.read().split(',')
input = np.array(content, dtype = int)

mini = min(input)
maxi = max(input)

x = np.zeros((maxi - mini + 1), dtype = int)
for i in range(mini, maxi + 1):
    x[i] = sum((abs(input - i)))

print(min(x)) # part 1: 344605

### part 2
y = np.zeros((maxi - mini + 1), dtype = int)
for i in range(mini, maxi + 1):
    d = abs(input - i) # the difference (length)
    y[i] = sum(d*(d+1)/2) 

print(min(y)) # part 2: 93699985