def aba(x):
    if x[0] == x[2] and x[0] != x[1]: return True
    return False

def valid(A,B):
    for x in A:
        for y in B:
            if x[0] == y[1] and x[1] == y[0]:
                return True
    return False



with open("7.txt") as fh:
    content = fh.read().split("\n")

count = 0
for x in content: 
    bracketmode = False
    A = []
    B = []
    i = 0
    while i < len(x)-2:
        if x[i] == "[":
            bracketmode = True
        elif x[i] == "]":
            bracketmode = False
        else:
            y = x[i:i+3]
            if aba(y) and not bracketmode:
                A.append(y)
            elif aba(y) and bracketmode:
                B.append(y)
        i += 1

    if valid(A,B): count += 1

print(count)    # 367 wrong
