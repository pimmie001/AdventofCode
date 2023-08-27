with open('21.txt') as fh:
    input = fh.read().split('\n')

dic = {}
for line in input:
    a,b = line.split(': ')
    
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
        dic[a] = int(b)


def f(x, memo={}):
    # computes value giving starting values in memo

    if x in memo:
        return memo[x]

    value = dic[x]

    if type(value) == int:
        result = value
    elif value[0] == '*':
        result = f(value[1], memo) * f(value[2], memo)
    elif value[0] == '/':
        result = f(value[1], memo) / f(value[2], memo)
    elif value[0] == '+':
        result = f(value[1], memo) + f(value[2], memo)
    elif value[0] == '-':
        result = f(value[1], memo) - f(value[2], memo)

    memo[x] = result
    return result


### return true/false if root is matched, and return the difference of the numbers
match = ['qpct', 'dthc'] # numbers that need to match 
def root_match(humn):
    memo = {'humn': humn}

    qpct = f(match[0], memo)
    dthc = f(match[1], memo)
    if qpct == dthc:
        return True, 0
    else: 
        return False, qpct - dthc


### 1. try go get humn close by using difference
humn1 = 0 # will increase in difference
humn2 = 0 # will decrease in difference
i = 0
while i < 1000:
    success, difference1 = root_match(humn1)
    success, difference2 = root_match(humn2)

    humn1 += difference1//100
    humn2 -= difference2//100

    i += 1


### 2. determine wether humn1 or humn2 was the closest
if abs(difference1) < abs(difference2):
    humn = humn1
else:
    humn = humn2


### 3. add and substract one each iteration
success = False
add = 0
while not success:
    success, _ = root_match(humn + add)
    if success:
        print(humn + add)
        break

    success, _ = root_match(humn - add)
    if success:
        print(humn - add)
        break

    add += 1

### answer part 2: 3592056845086
