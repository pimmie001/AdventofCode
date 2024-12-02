A = []
B = []

with open("1.txt") as fh:
    content = fh.read().split('\n')

for line in content:
    a,b = line.split()
    A.append(int(a))
    B.append(int(b))

A.sort()
B.sort()

total = sum([abs(A[i]-B[i]) for i in range(len(A))])
print(total) # part 1: 2367773


total2 = 0
for n in A:
    total2 += n * B.count(n)
print(total2)
