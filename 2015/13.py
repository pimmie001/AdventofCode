import itertools as it

with open("13.txt") as fh:
    content = fh.read().split("\n")

happiness = {}
people = []
for x in content: 
    x = x.replace(".","").split()
    person = x[0]
    if person not in people: people.append(person)
    target = x[-1]
    happy = -int(x[3]) if x[2] == "lose" else int(x[3])
    happiness[(person,target)] = happy



allpermutations = list(it.permutations(people, len(people))) 
Allhappiness = []
for arrangement in allpermutations:
    h = 0
    for i in range(len(arrangement)):
        if i == len(arrangement)-1:
            h += happiness[ (arrangement[i], arrangement[0]) ]
            h += happiness[ (arrangement[i], arrangement[i-1]) ]
        else: 
            h += happiness[ (arrangement[i], arrangement[i+1]) ]
            h += happiness[ (arrangement[i], arrangement[i-1]) ]
    Allhappiness.append(h)

print("Anser part 1: ",max(Allhappiness))


### Part 2

for person in people:
    happiness[("me",person)] = happiness[(person,"me")] = 0
people.append("me")

allpermutations = list(it.permutations(people, len(people))) 
Allhappiness = []
for arrangement in allpermutations:
    h = 0
    for i in range(len(arrangement)):
        if i == len(arrangement)-1:
            h += happiness[ (arrangement[i], arrangement[0]) ]
            h += happiness[ (arrangement[i], arrangement[i-1]) ]
        else: 
            h += happiness[ (arrangement[i], arrangement[i+1]) ]
            h += happiness[ (arrangement[i], arrangement[i-1]) ]
    Allhappiness.append(h)

print("Anser part 2: ",max(Allhappiness))
