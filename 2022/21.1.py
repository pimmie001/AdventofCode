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

print(f('root')) # part 1: 194058098264286
