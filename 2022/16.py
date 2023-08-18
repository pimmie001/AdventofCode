############################################################################################
########################################## PART 1 ##########################################
############################################################################################

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




############################################################################################
########################################## PART 2 ##########################################
############################################################################################

import gurobipy as gp
from gurobipy import GRB

### read/prepare data

with open('16.txt') as fh:
    input = fh.read().split('\n')


valves = [] # list of all valves
flows = {} # list of all flows
adj_list = {} # adjacency list

for line in input:
    line = line.replace(',', '')
    line = line.split(' ')

    valve = line[1]
    valves.append(valve)

    flow = int(line[4].split('=')[1][:-1])
    flows[valve] = flow

    leads_to = line[9:]
    adj_list[valve] = leads_to



minutes = range(26) # for part 2


### ILP model
model = gp.Model('part 2')
model.ModelSense = GRB.MAXIMIZE


## variables
yvars = []
yvars_dict = {}
count = 0
for i in minutes:
    for j in valves:
        y = model.addVar(vtype = GRB.BINARY, obj = flows[j], name = f'y^{i}_{j}') # = 1 if valve j is open at minute i
        yvars.append(y)
        yvars_dict[(i,j)] = count
        count += 1

xvars = []
xvars_dict = {}
count = 0
for i in minutes:
    for j in valves:
        x = model.addVar(vtype = GRB.BINARY, obj = 0, name = f'x^{i}_{j}') # 1 if we are at valve j at minute i
        xvars.append(x)
        xvars_dict[(i,j)] = count
        count += 1

pvars = []
pvars_dict = {}
count = 0
for i in minutes:
    for j in valves:
        p = model.addVar(vtype = GRB.BINARY, obj = 0, name = f'p^{i}_{j}') # same as x but for the elephant
        pvars.append(p)
        pvars_dict[(i,j)] = count
        count += 1

zvars = []
zvars_dict = {}
count = 0
for i in minutes:
    for j1 in valves:
        for j2 in valves:
            z = model.addVar(vtype = GRB.BINARY, obj = 0, name = f'z^{i}_{j1},{j2}') # 1 if we go from j1 to j2 at minute i (j1 != j2); 1 if we open valve j1 at minute i (j1 == j2)
            zvars.append(z)
            zvars_dict[(i,j1,j2)] = count
            count += 1

mvars = []
mvars_dict = {}
count = 0
for i in minutes:
    for j1 in valves:
        for j2 in valves:
            m = model.addVar(vtype = GRB.BINARY, obj = 0, name = f'm^{i}_{j1},{j2}') # same as z but for elephant
            mvars.append(m)
            mvars_dict[(i,j1,j2)] = count
            count += 1

### constraints
# 1. valve can only be open if it was already open or if we opened it before
for i in minutes:
    for j in valves:
        if i == 0: # valves are closed at time 0
            model.addConstr(yvars[yvars_dict[(i,j)]] == 0)
        else: # only if it was already open or if we opened it previous minute
            model.addConstr(yvars[yvars_dict[(i,j)]] <= yvars[yvars_dict[(i-1,j)]] + zvars[zvars_dict[(i-1,j,j)]] + mvars[mvars_dict[(i-1,j,j)]]) # 0 if it is not possible
            model.addConstr(3 * yvars[yvars_dict[(i,j)]] >= yvars[yvars_dict[(i-1,j)]] + zvars[zvars_dict[(i-1,j,j)]] + mvars[mvars_dict[(i-1,j,j)]]) # set to 1 if it is possible


# 2.1 start at 'AA'
for j in valves:
    if j == 'AA':
        model.addConstr(xvars[xvars_dict[(0,j)]] == 1)
        model.addConstr(pvars[pvars_dict[(0,j)]] == 1)
    else:
        model.addConstr(xvars[xvars_dict[(0,j)]] == 0)
        model.addConstr(pvars[pvars_dict[(0,j)]] == 0)


# 2.2 go to location we moved previous minute
for i in minutes[1:]:
    for j in valves:
        model.addConstr(xvars[xvars_dict[(i,j)]] == sum([zvars[zvars_dict[(i-1,x,j)]] for x in valves]))
        model.addConstr(pvars[pvars_dict[(i,j)]] == sum([mvars[mvars_dict[(i-1,x,j)]] for x in valves]))

# 2.3 we are at exactly one location each minute (not needed but gives better LP bound)
for i in minutes:
    model.addConstr(sum([xvars[xvars_dict[i,x]] for x in valves]) == 1)
    model.addConstr(sum([pvars[pvars_dict[i,x]] for x in valves]) == 1)


# 3.1 do exactly one action each minute if we are that location (if we are not at that location: zero actions)
for i in minutes:
    for j in valves:
        model.addConstr(sum([zvars[zvars_dict[i,j,x]] for x in valves]) == xvars[xvars_dict[(i,j)]])
        model.addConstr(sum([mvars[mvars_dict[i,j,x]] for x in valves]) == pvars[pvars_dict[(i,j)]])

# 3.2 can only go through valves that are adjacent
for i in minutes:
    for j1 in valves:
        for j2 in valves:
            if j1 != j2 and j2 not in adj_list[j1]: # can stay at the same location or go to its neighbor
                model.addConstr(zvars[zvars_dict[(i,j1,j2)]] == 0)
                model.addConstr(mvars[mvars_dict[(i,j1,j2)]] == 0)


### solving
model.optimize() # 2283 (takes about 130 seconds)





################################################
############ part 1 with ILP model #############
################################################
# not needed for part 1 since function above works better
# but was used as a starting point for the model of part 2


# minutes = range(30) # for part 1


# ### ILP model
# model = gp.Model('part 1')
# model.ModelSense = GRB.MAXIMIZE


# ## variables
# yvars = []
# yvars_dict = {}
# count = 0
# for i in minutes:
#     for j in valves:
#         y = model.addVar(vtype = GRB.BINARY, obj = flows[j], name = f'y^{i}_{j}') # = 1 if valve j is open at minute i
#         yvars.append(y)
#         yvars_dict[(i,j)] = count
#         count += 1

# xvars = []
# xvars_dict = {}
# count = 0
# for i in minutes:
#     for j in valves:
#         x = model.addVar(vtype = GRB.BINARY, obj = 0, name = f'x^{i}_{j}') # 1 if we are at valve j at minute i
#         xvars.append(x)
#         xvars_dict[(i,j)] = count
#         count += 1

# zvars = []
# zvars_dict = {}
# count = 0
# for i in minutes:
#     for j1 in valves:
#         for j2 in valves:
#             z = model.addVar(vtype = GRB.BINARY, obj = 0, name = f'z^{i}_{j1},{j2}') # 1 if we go from j1 to j2 at minute i (j1 != j2); 1 if we open valve j1 at minute i (j1 == j2)
#             zvars.append(z)
#             zvars_dict[(i,j1,j2)] = count
#             count += 1

# # constraints
# # 1. valve can only be open if it was already open or if we opened it before
# for i in minutes:
#     for j in valves:
#         if i == 0: # valves are closed at time 0
#             model.addConstr(yvars[yvars_dict[(i,j)]] == 0)
#         else: # only if it was already open or if we opened it previous minute
#             model.addConstr(yvars[yvars_dict[(i,j)]] <= yvars[yvars_dict[(i-1,j)]] + zvars[zvars_dict[(i-1,j,j)]]) # 0 if it is not possible
#             model.addConstr(2 * yvars[yvars_dict[(i,j)]] >= yvars[yvars_dict[(i-1,j)]] + zvars[zvars_dict[(i-1,j,j)]]) # set to 1 if it is possible


# # 2.1 start at 'AA'
# for j in valves:
#     if j == 'AA':
#         model.addConstr(xvars[xvars_dict[(0,j)]] == 1)
#     else:
#         model.addConstr(xvars[xvars_dict[(0,j)]] == 0)


# # 2.2 go to location we moved previous minute
# for i in minutes[1:]:
#     for j in valves:
#         model.addConstr(xvars[xvars_dict[(i,j)]] == sum([zvars[zvars_dict[(i-1,x,j)]] for x in valves]))

# # 2.3 we are at exactly one location each minute (not needed but gives better LP bound)
# for i in minutes:
#     model.addConstr(sum([xvars[xvars_dict[i,x]] for x in valves]) == 1)


# # 3.1 do exactly one action each minute if we are that location (if we are not at that location: zero actions)
# for i in minutes:
#     for j in valves:
#         model.addConstr(sum([zvars[zvars_dict[i,j,x]] for x in valves]) == xvars[xvars_dict[(i,j)]])

# # 3.2 can only go through valves that are adjacent
# for i in minutes:
#     for j1 in valves:
#         for j2 in valves:
#             if j1 != j2 and j2 not in adj_list[j1]: # can stay at the same location or go to its neighbor
#                 model.addConstr(zvars[zvars_dict[(i,j1,j2)]] == 0)


# ### solving
# model.optimize() # 1724 (takes about 17 seconds)
