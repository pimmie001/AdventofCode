def f(x):
    A = {}
    for y in x:
        A[y] = A.get(y,0) + 1
    return max(A, key = A.get), min(A, key = A.get)

with open("6.txt") as fh:
    content = fh.read().split("\n")

n = len(content[0])
password = ""
password2 = ""

for i in range(n):
    x = ""
    for j in range(len(content)):
        x += content[j][i]
    password += f(x)[0]
    password2 += f(x)[1]

print(password)     # part 1
print(password2)    # part 2