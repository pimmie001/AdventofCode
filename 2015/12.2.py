with open("12.txt") as fh:
    input = fh.read()



def mysplit(string, sep):
    result = []
    
    sub = ''
    parcount = 0
    parcount2 = 0
    needfirst = False
    needsecond = False
    for i in range(len(string)):
        x = string[i]
        
        if x == sep and (parcount == 0 or not needfirst) and (parcount2 == 0 or not needsecond):
            result.append(sub)
            sub = ''
            needfirst = False
            needsecond = False
        elif x == '[' and not needfirst and not needsecond:
            parcount += 1
            needfirst = True
            needsecond = False
        elif x == '{' and not needfirst and not needsecond:
            parcount2 += 1
            needfirst = False
            needsecond = True

        elif x == ']' and not needsecond:
            parcount -= 1

        elif x == '}' and not needfirst:
            parcount2 -= 1

        # else:
        sub += x

    result.append(sub)
    return result


def countit(string, struct = False):
    string = string[1:-1]
    if struct: 
        # A = string.split(':')
        A = mysplit(string, ':')
        if 'red' in A: 
            return 0
    else: 
        A = mysplit(string, ',')
        # A = string.split(',')


    result = 0
    for x in A:
        if x.isnumeric():
            result += int(x)
        elif x.strip('-').isnumeric():
            result -= int(x.strip('-'))
        elif '{' in x:
            result += countit(x, True)
        elif '[' in x:
            result += countit(x)

    return result




input = '[3,6,{red: 4, yellow:199}, [9,-3]]'

tocheck = []

i = 0
while i < len(input):
    x = input[i]

    if x == '{':
        begin = i
        parcount = 1
        
        while True:
            i += 1
            y = input[i]
            if y == '}':
                parcount -= 1
            elif y == '{':
                parcount += 1

            if parcount == 0:
                end = i
                tocheck.append(input[begin:end+1])
                break

    elif x == '[':
        begin = i
        parcount = 1
        
        while True:
            i += 1
            y = input[i]
            if y == ']':
                parcount -= 1
            elif y == '[':
                parcount += 1

            if parcount == 0:
                end = i
                tocheck.append(input[begin:end+1])
                break
    else: 
        i += 1




grandtotal = 0
for line in tocheck:
    if line[0] == '{':
        grandtotal += countit(line, True)
    else:
        grandtotal += countit(line)

print(grandtotal)