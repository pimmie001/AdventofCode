import itertools as it

def sort(route):
    Locations = route.split(" to ")
    Locations = sorted(Locations)
    return Locations[0]+" to "+Locations[1]


with open("9.txt") as fh:
    content = fh.read().split("\n")


Costs = {}
Locations = []
Allcosts = []
for x in content:
    y = x.split(" = ")
    Costs[sort(y[0])] = int(y[1])

    z = y[0].split(" to ")
    for i in z:
        if i not in Locations:
            Locations.append(i)

allroutes = list(it.permutations(Locations))
for route in allroutes:
    cost = 0
    for i in range(len(route) - 1):
        R = route[i]+" to "+route[i+1]
        cost += Costs[sort(R)]
    Allcosts.append(cost)



print("Part 1: minimum distance is: ",min(Allcosts))
print("Part 2: maximum distance is: ",max(Allcosts))
# print(allroutes)









