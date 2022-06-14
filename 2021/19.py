import numpy as np

with open('19.txt') as fh:
    content = fh.read().split('\n\n')

A = {}

for x in content:
    y = x.split('\n')
    firstline = y[0].split(' ')
    scanner = int(firstline[-2])

    a = []
    for z in y[1:]:
        b = []
        l = z.split(',')
        for n in l:
            b.append(int(n))

        a.append(b)

    A[scanner] = a

print(A)


def getallrotations(a):
    a = np.array(a)
    A = []
    rx = np.array([[1,0,0],[0,0,-1],[0,1,0]])
    ry = np.array([[0,0,1],[0,1,0],[1,0,0]])
    rz = np.array([[0,-1,0],[1,0,0],[0,0,1]])
    size = [1,2,3,4] 
    size = [0,1,2,3]

    for x in size:
        for y in size:
            for z in size:
                A.append(a @ (np.linalg.matrix_power(rx,x)) @ (np.linalg.matrix_power(ry,y)) @ (np.linalg.matrix_power(rz,z)))
    
    return A

x = [-1,-1,1]

A = getallrotations(x)
print(A)
print(len(A))