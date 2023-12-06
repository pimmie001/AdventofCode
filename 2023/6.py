import numpy as np

## example
# times = [7, 15, 30]
# distances = [9, 40, 200]

## own input
times = [48, 93, 84, 66]
distances = [261, 1192, 1019, 1063]


def count_ways(time, dist):
    # given time and dist, count number of ways it can win
    count = 0
    for i in range(time+1):
        remaining_time = time - i
        travel_distance = remaining_time * i
        if travel_distance > dist:
            count += 1
    return count


product = 1
for i in range(len(times)):
    product *= count_ways(times[i], distances[i])
print(product) # part 1: 1312850


### part 2
new_time = int(''.join([str(t) for t in times]))
new_distance = int(''.join([str(d) for d in distances]))

def quadratic_formula(a,b,c):
    # returns solutions of quadratic equation
    x1 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

# solve (time - hold) * hold == new_distance equivalent to -hold**2 + time*hold - new_distance == 0
x1, x2 = sorted(quadratic_formula(-1, new_time, -new_distance))

print(int(np.floor(x2) - np.ceil(x1) + 1)) # part 2: 36749103
