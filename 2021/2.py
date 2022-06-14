with open ('2.txt') as fh:
    content = fh.read().split('\n')


# part 1

x = 0 # horizontal position
y = 0 # depth

for i in content:
    j = i.split()
    if j[0] == 'forward': x += int(j[1])
    elif j[0] == 'down': y += int(j[1])
    elif j[0] == 'up': y -= int(j[1])


print(x*y) # 1488669


# part 2
aim = 0
horizon = 0
depth = 0

for i in content:
    j = i.split()
    if j[0] == 'forward': 
        horizon += int(j[1])
        depth += aim * int(j[1])
    elif j[0] == 'down': aim += int(j[1])
    elif j[0] == 'up': aim -= int(j[1])

print(horizon*depth) # 1176514794