# From 8.1: 
def dectobin(a, bits=16):
    b = ""
    for i in range(bits-1,-1,-1):
        if a >= 2**i:
            b += "1" 
            a -= 2**i
        else:
            b += "0"
    return b

with open("17.txt") as fh:
    input = fh.read().split("\n")

L = 150


combinations = []
for i in range(2**len(input)):
    combinations.append(dectobin(i, len(input)))

containers = [] ##
count = 0
for combination in combinations:
    c = 0 ##
    total = 0 
    for i in range(len(combination)):
        if combination[i] == "1":
            total += int(input[i])
            c += 1 ##
    if total == L:
        count += 1
        containers.append(c) ##

print(count)
print(containers.count(min(containers))) ##