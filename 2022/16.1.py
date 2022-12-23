import numpy as np

### 1. read/prepare data

with open('16.txt') as fh:
    input = fh.read().split('\n')


num2name = {}
name2num = {}
i = 0
for line in input:
    line = line.replace(',', '')
    line = line.split(' ')
    valve = line[1]

    num2name[i] = valve
    name2num[valve] = i
    i += 1


flows = {}
paths = {}
valves = []
interesting_valves = []

for line in input:
    line = line.replace(',', '')
    line = line.split(' ')

    valve = line[1]
    flow = int(line[4].split('=')[1][:-1])
    leads_to = line[9:]

    valves.append(valve)
    if flow > 0:
        interesting_valves.append(valve)

    flows[valve] = flow
    paths[valve] = line[9:]



### 2. Find all shortest paths between all pairs


# Create distance matrix
n = len(valves)
A = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif num2name[j] in paths[num2name[i]]:
            A[i,j] = 1
        else:
            A[i,j] = np.inf


def floyd(A):
    # floyd-warshall-algorithm (shortest path)
    n = len(A[0])
    dp = np.zeros((n+1,n,n))
    dp[0,:,:] = np.copy(A)
    p = np.ones((n,n))
    p = (p * np.arange(1, n +1)).T

    for k in range(1, n+1):
        for i in range(n):
            for j in range(n):
                if dp[k-1,i,k-1] + dp[k-1,k-1,j] < dp[k-1,i,j]:
                    dp[k,i,j] = dp[k-1,i,k-1] + dp[k-1,k-1,j] 
                    p[i,j] = k
                else:
                    dp[k,i,j] = dp[k-1,i,j]

    return dp



dp = floyd(A)
sp_length = dp[-1, :, :]



### 3. solve actual problem (part 1)

def current_pressure(active):
    total = 0
    for v in active:
        total += flows[v]
    return total


def f(state, memo={}):
    if state in memo:
        return memo[state]

    total_pressure, time, location, active = state

    # base cases:
    if time == 31:
        return total_pressure
    if time > 31:
        return 0


    current_pres = current_pressure(active) # current pressure added each minute

    result = total_pressure + (31-time) * current_pres # if not moved to another valve

    for valve in interesting_valves: # move to another intersting valve
        if valve in active:
            continue

        time_cost = sp_length[name2num[location], name2num[valve]] + 1

        new_pressure = total_pressure + time_cost * current_pres
        new_time = time + time_cost
        new_active = active + (valve,)
        new_state = new_pressure, new_time, valve, new_active

        result = max(result, f(new_state, memo))

    memo[state] = result
    return result



total_pressure = 0
time = 1
location = 'AA'
active = ()

state = total_pressure, time, location, active

print(f(state)) # part 1: 1724
