with open ('10.txt') as fh:
    input = fh.read().split()
input = list(map(int, input))

owndevice = max(input) + 3
input.extend((0, owndevice))
input.sort()

# use some sort of backwards induction, numbers get very messy
DICK = {owndevice:1}
for i in range(len(input)-2, -1, -1):
    n = input[i]
    followers = []
    for j in range(i+1, min(len(input), i+4)):
        n2 = input[j]
        if n2 - n <= 3:
            followers.append(n2)
    tot = 0
    for m in followers:
        tot += DICK[m]
    DICK[n] = tot

print(DICK[0]) # 1157018619904