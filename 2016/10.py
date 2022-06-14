def give(bot):
    reclow, rechigh = C[bot]
    low, high = sorted(Bots[bot])
    return low, high, reclow, rechigh


def check(Bots):
    for bot in Bots.keys():
        if "bot" in bot:
            if len(Bots[bot]) == 2:
                return False
    return True

with open("10.txt") as fh:
    instructions = fh.read().split("\n")

C = {}
Bots = {}

for x in instructions:
    x = x.split()
    # print(x)

    if x[0] == "value": 
        arr = Bots.get("bot"+x[-1],[])
        arr.append(int(x[1]))
        Bots["bot"+x[-1]] = arr
    else: 
        C["bot"+x[1]] = (x[5] + x[6]).replace(" ",""), (x[-2] + x[-1]).replace(" ","")


ToCheck = [17,61]       


while not check(Bots):
    for bot in Bots.keys():
        if len(Bots[bot]) == 2:
            if sorted(Bots[bot]) == sorted(ToCheck):
                print(bot)

            low, high, reclow, rechigh = give(bot)
            L, H = Bots.get(reclow, []), Bots.get(rechigh, [])
            L.append(low)
            H.append(high)
            Bots[reclow] = L
            Bots[rechigh] = H
            Bots[bot] = []
            break       # to prevent "dictionary changed during iteration" error

# Bot 161



### Part 2
product = 1
outs = [0, 1, 2]
for x in outs:
    product *= Bots["output"+str(x)][0]
print(product)  # 133163