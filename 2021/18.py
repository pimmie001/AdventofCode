def canexplode(A):
    left = False
    # right = False

    parcount = 0
    for i in range(len(A)):
        x = A[i]
        if x == '[':
            parcount += 1
        elif x == ']':
            parcount -= 1
        elif x.isnumeric():
            left = True
        
        if parcount == 5:
            for j in range(i + 1, len(A)):
                if A[j] == ']':
                    for k in range(j+1, len(A)):
                        if A[k].isnumeric():
                            return (True, left, True)
            return (True, left, False)

    return (False)


def explode(A, left, right):
    if not canexplode(A): return A

    B = A
    # find indexes of the exploding shit:

    if left:
        parcount = 0
        for i in range(len(A)):
            x = A[i]
            if x.isnumeric():
                leftindex = i
            elif x == '[':
                parcount += 1
            elif x == ']': 
                parcount -= 1

            if parcount == 5:
                break

    if right:
        parcount = 0
        for i in range(len(A)):
            x = A[i]
            if x == '[':
                parcount += 1
            elif x == ']':
                parcount -= 1
            
            if parcount == 5:
                for j in range(i+1, len(A)):
                    if A[j] == ']':
                        for k in range(j+1, len(A)):
                            if A[k].isnumeric:
                                rightindex = k
    
    # if left:
    #     print(leftindex)
    if right:
        print(rightindex)






A = '[[6,[5,[4,[3,2]]]],1]'

result = canexplode(A)
if result[0]:
    explode(A, result[1], result[2])

# print(A[8])
print(A[20])