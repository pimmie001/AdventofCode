import gurobipy as gp
from gurobipy import GRB


with open('21.txt') as fh:
    content = fh.read().split('\n')


set_of_monkeys = set()
dic = {}
for line in content:
    a,b = line.split(': ')

    set_of_monkeys.add(a)

    if '*' in b:
        b1, b2 = b.split(' * ')
        dic[a] = ('*', b1, b2)
    elif '/' in b:
        b1, b2 = b.split(' / ')
        dic[a] = ('/', b1, b2)
    elif '+' in b:
        b1, b2 = b.split(' + ')
        dic[a] = ('+', b1, b2)
    elif '-' in b:
        b1, b2 = b.split(' - ')
        dic[a] = ('-', b1, b2)
    else:
        dic[a] = (int(b), None, None)


## setup model
m = gp.Model('model')
m.modelsense = GRB.MINIMIZE


## create variables
vars = []
vars_dict = {}
i = 0
for a in set_of_monkeys:
    x = m.addVar(lb = float('-inf'), obj = (a == 'humn'), name = f'x_{a}')
    vars.append(x)
    vars_dict[a] = i
    i += 1


## constraints
for a in dic:
    if a == 'root':
        b1, b2 = dic[a][1:]
        m.addConstr(vars[vars_dict[b1]] == vars[vars_dict[b2]])
    elif a == 'humn':
        pass
    else:
        v, b1, b2 = dic[a]
        if v == '*':
            m.addConstr(vars[vars_dict[a]] == vars[vars_dict[b1]] * vars[vars_dict[b2]])
        elif v == '/':
            vars[vars_dict[b1]]
            m.addConstr(vars[vars_dict[a]] * vars[vars_dict[b2]] == vars[vars_dict[b1]])
        elif v == '+':
            m.addConstr(vars[vars_dict[a]] == vars[vars_dict[b1]] + vars[vars_dict[b2]])
        elif v == '-':
            m.addConstr(vars[vars_dict[a]] == vars[vars_dict[b1]] - vars[vars_dict[b2]])
        else:
            m.addConstr(vars[vars_dict[a]] == int(v))


## solve
m.setParam('NonConvex', 2)
m.setParam('OutputFlag', False)
m.optimize()
print(int(m.ObjVal)) # part 2: 3592056845086
