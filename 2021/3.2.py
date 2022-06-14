import numpy as np

with open ('3.txt') as fh:
    input = fh.read().split('\n')

n = len(input[0])
m = len(input)

x = np.zeros((m,n))
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '1':
            x[i,j] = 1

y = x.copy()
z = x.copy()


i = 0 
while np.size(y) + np.size(z) > 2*n:
    if np.size(y) > n:
        # find MCV  
        m = len(y)
        j = 0
        for ii in range(len(y)):
            if y[ii, i] == 1:
                j += 1

        if 2*j >= m:
            MCV = 1 
        else: 
            MCV = 0

        # remove/ keep
        ind = np.where(y[:,i] == MCV)
        y = y[ind, :][0]


    if np.size(z) > n:
        # find MCV  
        m = len(z)
        j = 0
        for ii in range(len(z)):
            if z[ii, i] == 1:
                j += 1

        if 2*j < m: # change inequality
            MCV = 1 
        else: 
            MCV = 0

        # remove/ keep
        ind = np.where(z[:,i] == MCV)
        z = z[ind, :][0]

    i += 1


# calculate binary values 
b1 = ''
b2 = ''
for i in y[0]:
    b1 += str(int(i))
for i in z[0]:
    b2 += str(int(i))


print(int(b1,2) * int(b2,2)) # 1613181

