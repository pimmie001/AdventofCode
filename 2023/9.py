import numpy as np 
import re


with open('9.txt') as fh:
    content = fh.read().split('\n')

histories = [np.array(re.findall(r'-?\d+', line), dtype=int) for line in content]


def get_value(history):

    ## find all layers
    layers = [history]
    while np.any(layers[-1]):
        diff = np.diff(layers[-1])
        layers.append(diff)


    ## given layers, find the value
    right_values = [0]
    for i in range(len(layers)-1):
        new_val = layers[-i-2][-1] + right_values[-1]
        right_values.append(new_val)


    ## get value for part 2
    left_values = [0]
    for i in range(len(layers)-1):
        new_val = layers[-i-2][0] - left_values[-1]
        left_values.append(new_val)


    return right_values[-1], left_values[-1]


total = 0
total2 = 0
for history in histories:
    values = get_value(history)
    total += values[0]
    total2 += values[1]
print(total) # part 1: 1637452029
print(total2) # part 2: 908