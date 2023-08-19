import re
import gurobipy as gp
from gurobipy import GRB


with open('19.txt') as fh:
    content = fh.read().split('\n')

blueprints = []
for x in content:
    numbers = re.findall(r'\d+', x)[1:] # first number is blueprint number
    blueprints.append([int(y) for y in numbers])


def model(costs):
    materials = [0,1,2,3] # ore, clay, obsidian, geode
    minutes = range(1, 25)

    ### ILP model
    m = gp.Model('model')
    m.ModelSense = GRB.MAXIMIZE


    ## variables
    xvars = []
    yvars = []
    zvars = []

    Dict = {}
    count = 0
    for i in minutes:
        for mat in materials: ###############! UB???
            x = m.addVar(obj = (i == 24 and mat == 3), ub = 1000, name = f'x^{i}_{mat}') # number of available materials at time i
            xvars.append(x)

            y = m.addVar(name = f'y^{i}_{mat}') # number of robots at begin of time i
            yvars.append(y)

            z = m.addVar(vtype = GRB.BINARY, name = f'z^{i}_{mat}') # number of robots of type j we build at time i
            zvars.append(z)

            Dict[i,mat] = count
            count += 1


    ## constraints
    # 1.1 we have one ore at time 1 and no other materials
    for mat in materials:
        m.addConstr(xvars[Dict[1,mat]] == (mat == 0))

    # 1.2 ore at the end of minute i is ore at time i-1 + amount of robots at time i minus amount that we use to build robots
    for i in minutes[1:]:
        m.addConstr(xvars[Dict[i,0]] == xvars[Dict[i-1,0]] + yvars[Dict[i,0]] - costs[0] * zvars[Dict[i,0]] \
                    - costs[1] * zvars[Dict[i,1]] - costs[2] * zvars[Dict[i,2]] - costs[4] * zvars[Dict[i,3]]) # ore
        m.addConstr(xvars[Dict[i,1]] == xvars[Dict[i-1,1]] + yvars[Dict[i,1]] - costs[3] * zvars[Dict[i,2]]) # clay
        m.addConstr(xvars[Dict[i,2]] == xvars[Dict[i-1,2]] + yvars[Dict[i,2]] - costs[5] * zvars[Dict[i,3]]) # obsidian
        m.addConstr(xvars[Dict[i,3]] == xvars[Dict[i-1,3]] + yvars[Dict[i,3]]) # geode


    # 2.1 we have an ore robot at time 1 and no other robots
    for mat in materials:
        m.addConstr(yvars[Dict[1,mat]] == (mat == 0))

    # 2.2 at time i we have the robots at time i-1 and the robots we made at i-1
    for i in minutes[1:]:
        for mat in materials:
            m.addConstr(yvars[Dict[i,mat]] == yvars[Dict[i-1,mat]] + zvars[Dict[i-1,mat]])


    # 3.1 at time 1 we dont build anything
    for mat in materials:
        m.addConstr(zvars[Dict[1,mat]] == 0)

    # 3.2 if z^i_j is 1, should have enough material at time i-1 #! not needed since x^i_j >= 0 ?
    for i in minutes[1:]:
        m.addConstr(xvars[Dict[i-1,0]] >= costs[0] * zvars[Dict[i,0]] + costs[1] * zvars[Dict[i,1]] \
                    + costs[2] * zvars[Dict[i,2]] + costs[4] * zvars[Dict[i,3]]) # enough ore
        m.addConstr(xvars[Dict[i-1,1]] >= costs[3] * zvars[Dict[i,2]]) # enough clay
        m.addConstr(xvars[Dict[i-1,2]] >= costs[5] * zvars[Dict[i,3]]) # enough obsidian

    # 3.3 at most build one robot
    for i in minutes:
        m.addConstr(sum([zvars[Dict[i,mat]] for mat in materials]) <= 1)


    ### solve model
    m.setParam('OutputFlag', False)
    m.optimize()

    return m.ObjVal


### answer
total = 0
for i in range(len(blueprints)):
    total += (i+1) * model(blueprints[i])
print(total) # 1395




###### function to show solution (for debugging)

# import numpy as np
# import pandas as pd

# def print_vars(vars, Dict):
#     arr = np.zeros(shape = (4, 24), dtype = object)
#     for i in range(24):
#         for mat in range(4):
#             # print(arr)
#             # print('sdjlf', vars[Dict[i+1,mat]])
#             arr[mat, i] = round(vars[Dict[i+1,mat]])
#     print(pd.DataFrame(arr), '\n')