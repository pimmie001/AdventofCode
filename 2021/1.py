import numpy as np

with open ('1.txt') as fh:
    content = fh.read().split('\n')


# part 1
x = np.array(content, dtype = float)
print(sum(np.diff(x)>0)) # 1548


# part 2
n = len(x) - 2
X = np.zeros(n)
for i in range(n):
    X[i] = np.sum(x[i:i+3])

print(sum(np.diff(X)>0)) # 1589

