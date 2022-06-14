import numpy as np

with open ('3.txt') as fh:
    input = fh.read().split('\n')


n = len(input[0])
m = len(input)

x = np.zeros(n)
for z in input:
    for i in range(n):
        if int(z[i]) == 1:
            x[i] += 1


joe = (x >= m/2).astype(int)
joe2 = (x < m/2).astype(int)

joejoe = "".join(map(str, joe))
joejoe2 = "".join(map(str, joe2))


print(int(joejoe,2) * int(joejoe2,2))


# print(int(b1, 2) * int(b2, 2)) # 3958484




