with open('19.txt') as fh:
    A, B = fh.read().split('\n\n')
    values_list = B.split('\n')

# worksflows
workflows = {}
A = A.split('\n')
for x in A:
    x = x.split('{')
    workflows[x[0]] = x[1][:-1]


def evaluate(workflow, values):
    instructions = workflows[workflow].split(',')

    for instruction in instructions[:-1]:
        condition, value_if_true = instruction.split(':')
        if '<' in condition:
            var, val = condition.split('<')
            if values[var] < int(val):
                return value_if_true
        else: # >
            var, val = condition.split('>')
            if values[var] > int(val):
                return value_if_true

    return instructions[-1]

def get_values(values_string):
    """given the values, evaluate the workflow and return sum of values if accepted and 0 else"""

    ## make a dict of the values
    values = {}
    for x in values_string[1:-1].split(','):
        var, val = x.split('=')
        values[var] = int(val)

    ## main loop
    accepted = None
    current_workflow = 'in'
    while accepted is None:
        current_workflow = evaluate(current_workflow, values)
        if current_workflow == 'A':
            accepted = True
        if current_workflow == 'R':
            accepted = False

    if accepted:
        return sum(values.values())
    else:
        return 0


total = 0
for values_string in values_list:
    total += get_values(values_string)
print(total)
