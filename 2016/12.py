with open("12.txt") as fh:
    instructions = fh.read().split("\n")

A = {}
i = 0
while i < len(instructions):
    x = instructions[i].split()
    if x[0] == "cpy":
        if x[1].isnumeric():    
            A[x[2]] = int(x[1])
        else: 
            A[x[2]] = A[x[1]]
    elif x[0] == "inc":
        A[x[1]] += 1
    elif x[0] == "dec":
        A[x[1]] -= 1
    elif x[0] == "jnz":
        dum = False
        if x[1].isnumeric():
            if int(x[1]) != 0: dum = True
        else: 
            if A.get(x[1]) != 0: dum = True
        if dum:
            i += int(x[2]) - 1
    
    i += 1

print(A)