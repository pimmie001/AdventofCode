import numpy as np
from collections import deque


with open('20.txt') as fh:
    content = fh.read().split('\n')

# create modules
modules = {}
for line in content:
    start, end = line.split(' -> ')
    
    if start == 'broadcaster':
        modules[start] = ('broadcaster'), end.split(', ')
    else:
        modules[start[1:]] = start[0], end.split(', ') # type, next

# setup memory for flip flops
memo = {}
for module in modules:
    module_type, _ = modules[module]
    if module_type == '%':
        memo[module] = 0 # default is false

# setup memory for conjuctions
def get_incoming(module):
    incoming = []
    for mod in modules:
        if module in modules[mod][1]:
            incoming.append(mod)
    return incoming

for module in modules:
    module_type, _ = modules[module]
    if module_type == '&':
        M = {mod:0 for mod in get_incoming(module)}
        memo[module] = M


def pust_button(memo):
    # Pushes button one time

    queue = deque([('broadcaster', 0, 'button')]) # module, pulse (0=low, 1=high), previous module
    pulses = np.array([0, 0]) # keep track of how many low/high pulses
    while queue:
        current_module, current_pulse, prev_module = queue.popleft()
        pulses[current_pulse] += 1

        if current_module in modules:
            module_type, next_modules = modules[current_module]
        else:
            module_type, next_modules = None, []

        if module_type == 'broadcaster':
            for next_mod in next_modules:
                queue.append((next_mod, current_pulse, current_module))

        elif module_type == '%':
            if current_pulse == 0: # do if low pulse
                if memo[current_module] == 0:
                    memo[current_module] = 1
                    for next_mod in next_modules:
                        queue.append((next_mod, 1, current_module)) # send high pulse

                elif memo[current_module] == 1:
                    memo[current_module] = 0
                    for next_mod in next_modules:
                        queue.append((next_mod, 0, current_module)) # send low pulse

        elif module_type == '&':
            memo[current_module][prev_module] = current_pulse # update memory
            for next_mod in next_modules:
                queue.append((next_mod, 1 - all(memo[current_module].values()), current_module))

    return pulses



k = 1000
pulses = np.array([0, 0])
for i in range(k):
    pulses += pust_button(memo)

print(pulses[0] * pulses[1]) # part 1: 684125385 