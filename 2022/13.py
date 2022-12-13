with open('13.txt') as fh:
    input = fh.read().split('\n\n')


def right_order(A1, A2):
    a1 = len(A1)
    a2 = len(A2)

    for i in range(max(a1, a2)):
        if i >= a2:
            return False
        elif i >= a1:
            return True

        x1 = A1[i]
        x2 = A2[i]

        if type(x1) == type(x2) == int:
            if x1 < x2:
                return True
            elif x1 > x2:
                return False

        elif type(x1) == type(x2) == list:
            result = right_order(x1, x2)
            if result is not None:
                return result 

        elif type(x1) == int:
            result = right_order([x1], x2)
            if result is not None:
                return result 

        elif type(x2) == int:
            result = right_order(x1, [x2])
            if result is not None:
                return result 

    return None


result = 0
index = 0
for line in input:
    index += 1

    A1, A2 = line.split('\n')
    A1 = eval(A1)
    A2 = eval(A2)

    if right_order(A1, A2):
        result += index

print(result) # part 1: 5760


### part 2:

def is_sorted(items):
    # checks if items are sorted and returns index of wrong position if not sorted
    for i in range(len(items)-1):
        if not right_order(items[i], items[i+1]):
            return False, i
    return True, None


with open('13.txt') as fh:
    input = fh.read().replace('\n\n', '\n').split('\n')

items = []
for line in input:
    A = eval(line)
    items.append(A)
items.extend([[[2]], [[6]]])


# bubble sort
while True:
    sorted, i  = is_sorted(items)
    if sorted:
        break
    items[i], items[i+1] = items[i+1], items[i] # swap items if not sorted

print((items.index([[2]])+1) * (items.index([[6]])+1)) # 26670
