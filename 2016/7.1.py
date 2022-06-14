def abba(x):
    if x[0] == x[2]: return False
    if x[0] == x[3] and x[1] == x[2]: return True
    return False

def valid(A):
    dummy = False
    bracketmode = False

    for i in range(len(A)-3):
        if A[i] == "[": bracketmode = True
        elif A[i] == "]": bracketmode = False

        part = A[i:i+4]
        if abba(part) and bracketmode:
            return False
        if abba(part): dummy = True

    return dummy

with open("7.txt") as fh:
    content = fh.read().split("\n")

count = 0
for x in content: 
    if valid(x): count += 1

print(count)