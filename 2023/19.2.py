import re


### read and make worksflows
with open('19.txt') as fh:
    A, B = fh.read().split('\n\n')

workflows = {}
A = A.split('\n')
for x in A:
    x = x.split('{')
    workflows[x[0]] = x[1][:-1]

# set format (variable, sign (< or >), number, variable if true)
for x in workflows:
    string = workflows[x]
    conditions = string.split(',')

    new_value = []
    for con in conditions[:-1]:
        var,num,dest = re.split(">|<|:", con)
        if '<' in con:
            new_value.append((var,'<',int(num),dest))
        else:
            new_value.append((var,'>',int(num),dest))

    new_value.append(conditions[-1])
    workflows[x] = new_value

# remove uneccesary conditions ( eg (m>1548:A, A)  -->  (A) )
for x in workflows:
    conditions = workflows[x]

    while len(conditions) > 1:
        if conditions[-1] == conditions[-2][-1]:
            conditions.pop(-2)
        else:
            break



### find values that needs to be evaluated (for every variable)

## strip function
def strip(conditions, evaluation_dict):
    # given conditions, adds values we need to evaluate to evaluation_dict

    for (var, sign, num, _) in conditions[:-1]:
        if sign == '<':
            evaluation_dict[var].append(num-1)
        else:
            evaluation_dict[var].append(num)


## find values
evaluation_dict = {var:[0, 4000] for var in 'xmas'}
for x in workflows:
    strip(workflows[x], evaluation_dict)

# sort and remove duplicates
for var in 'xmas': 
    evaluation_dict[var] = sorted(set(evaluation_dict[var]))



### functions to evaluate condition
def _evaluate(workflow, values):
    instructions = workflows[workflow]

    for (var, sign, num, new) in instructions[:-1]:
        if sign == '<':
            if values[var] < num:
                return new
        else: # >
            if values[var] > num:
                return new

    return instructions[-1]

def evaluate(values):
    """given the values, evaluate the workflow and return successful"""

    ## main loop
    current_workflow = 'in'
    while True:
        current_workflow = _evaluate(current_workflow, values)
        if current_workflow in ['A', 'R']:
            break

    return current_workflow == 'A'



### main loop
lengths = [len(x) for x in evaluation_dict.values()] # [510, 497, 537, 488]

total = 0
for i,x in enumerate(evaluation_dict['x']):
    if i == 0:
        continue
    for j,m in enumerate(evaluation_dict['m']):
        if j == 0:
            continue
        for k,a in enumerate(evaluation_dict['a']):
            if k == 0:
                continue
            for l,s in enumerate(evaluation_dict['s']):
                if l == 0:
                    continue

                if evaluate({'x':x, 'm':m, 'a':a, 's':s}):
                    prod = 1
                    for (var, ind) in [('x',i), ('m',j), ('a',k), ('s',l)]:
                        prod *= (evaluation_dict[var][ind] - evaluation_dict[var][ind-1])
                    total += prod

print(total) # part 2: 116738260946855
