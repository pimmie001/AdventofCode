def sort(A):
    # Sorts dictionary based on values, ties are broken alfabetically on keys
    B = []
    keys = list(A.keys())

    for key in keys:
        C = B.copy()
        if len(B) == 0:
            C.append((key,A[key]))
        else: 
            for i in range(len(B)):
                if A[key] < B[i][1] or (A[key] == B[i][1] and sorted([key, B[i][0]])[1] == key):  # or: tiebreakers alfabetically
                    C.insert(i, (key, A[key]))
                    break
            if i == len(C) - 1:         # if none of them were smaller it is the largers, therefore append (at the end of the list)
                C.append((key,A[key]))
        B = C.copy()

    return B

def valid(checksum, B):
    # removing unnecceary items
    while len(checksum) < len(B):
        for i in range(len(B)):
            if B[i][0] not in checksum:
                B.pop(i)
                break
    # checking the right order
    n = len(checksum)
    for i in range(n):
        if checksum[i] != B[n-i-1][0]:
            return False
    return True


with open("4.txt") as file:
    content = file.read().split("\n")

count = 0
for x in content:
    x = x.split("[")
    checksum = x[1][:-1]
    x = x[0].split("-")
    sectorID = int(x[-1])
    x = x[:-1]

    D = {}
    for y in x:
        for z in y:
            D[z] = D.get(z,0) + 1
    
    B = sort(D)
    if valid(checksum,B): count += sectorID


print(count) # 245102