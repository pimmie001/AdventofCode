import itertools as it

def playerwins(player, boss):
    player_turn = 1
    while player[0] > 0 and boss[0] > 0:
        if player_turn:
            boss[0] -= max(1, player[1]-boss[2])
        else:
            player[0] -= max(1, boss[1]-player[2])
        player_turn = 1 - player_turn 

    return True if boss[0] <= 0 else False

# input
boss_stats = [103, 9, 2]   # hit points, damage , armor
player_health = 100


with open("21.txt") as fh:
    content = fh.read().split("\n\n")
weapons = content[0]
armor   = content[1]
rings   = content[2]

weapon_stats = {}
weapons = weapons.split("\n")
for i in range(1,len(weapons)):
    line = weapons[i]    
    line = line.split()
    weapon_stats[line[0]] = int(line[1]), int(line[2]), int(line[3])

armor_stats = {"Nothing": (0,0,0)}
armor = armor.split("\n")
for i in range(1,len(armor)):
    line = armor[i]    
    line = line.split()
    armor_stats[line[0]] = int(line[1]), int(line[2]), int(line[3])

allrings = []
ring_stats = {"Nothing": (0,0,0)}
rings = rings.replace(" +","").split("\n")
for i in range(1, len(rings)):
    line = rings[i]
    line = line.split()
    ring_stats[line[0]] = int(line[1]), int(line[2]), int(line[3])

    allrings.append(line[0])

for x in list(it.combinations(allrings, 2)):
    ring1 = x[0]
    ring2 = x[1]
    ringstats1 = ring_stats[ring1]
    ringstats2 = ring_stats[ring2]
    totalcost = ringstats1[0] + ringstats2[0]
    totaldamage = ringstats1[1] + ringstats2[1]
    totalarmor = ringstats1[2] + ringstats2[2]

    ring_stats[x] = (totalcost, totaldamage, totalarmor)


Costs = []
Costloss = [] ## 
for weapon in weapon_stats:
    for armor in armor_stats:
        for ring in ring_stats:
            cost = weapon_stats[weapon][0] + armor_stats[armor][0] + ring_stats[ring][0]
            dam = weapon_stats[weapon][1] + armor_stats[armor][1] + ring_stats[ring][1]
            ar = weapon_stats[weapon][2] + armor_stats[armor][2] + ring_stats[ring][2]
            player_stats = [player_health, dam, ar]
            boss = boss_stats.copy()
            if playerwins(player_stats, boss):
                Costs.append(cost)
            else: ##
                Costloss.append(cost) 

print(min(Costs))
print(max(Costloss)) ## 
