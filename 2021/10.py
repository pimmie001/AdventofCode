with open('10.txt') as fh:
    input = fh.read().split('\n')

A = {')':3, ']':57, '}':1197, '>':25137}
openpars =  ['(', '[', '{', '<']
closepars = list(A.keys())

count = 0
shouldremove = [] # for part 2
for i in range(len(input)):
# for line in input:
    pars = []
    for x in input[i]: 
        if x in openpars:
            pars.append(x)
        if x in closepars:
            if openpars[closepars.index(x)] is not pars[-1]:
                count += A[x]
                shouldremove.append(i)
                break
            else: 
                pars.pop(-1)


print(f'part 1: {count}\n') # 394647

### part 2
incomplete = []
for i in range(len(input)):
    if i not in shouldremove:
        incomplete.append(input[i])

# almost same as part 1 but now put the missing brackets into a array
bigthing = []
for i in range(len(incomplete)):
    pars = []
    for x in incomplete[i]:
        if x in openpars:
            pars.append(x)
        if x in closepars:
            pars.pop(-1) # as they are never broeken
    bigthing.append(''.join(pars))


# reverse the things
bigthing2 = []
for line in bigthing:
    intermediate = []
    for i in reversed(range(len(line))):
        # x = line[i]
        # print(x)
        if line[i] == '{': intermediate.append('}')
        if line[i] == '<': intermediate.append('>')
        if line[i] == '(': intermediate.append(')')
        if line[i] == '[': intermediate.append(']')
    bigthing2.append(''.join(intermediate))


def score(line):
    sc = 0
    for x in line:
        sc *= 5
        if x == ')': sc += 1
        if x == ']': sc += 2
        if x == '}': sc += 3
        if x == '>': sc += 4
    return sc 


allscores = []
for line in bigthing2:
    allscores.append(score(line))
allscores.sort()

print(allscores[len(allscores)//2]) # 2380061249