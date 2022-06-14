def allin(a,b):
    # checks if all letters a are in b
    for letter in a:
        if letter not in b:
            return False
    return True


### alle makkelijke
def find1(input):
    input = input.split(' ')
    for x in input:
        if len(x) == 2:
            return x

def find4(input):
    input = input.split(' ')
    for x in input:
        if len(x) == 4:
            return x

def find7(input):
    input = input.split(' ')
    for x in input:
        if len(x) == 3:
            return x

def find8(input):
    input = input.split(' ')
    for x in input:
        if len(x) == 7:
            return x


### iets moeilijkere
def find6(input, one):
    input = input.split(' ')
    for x in input:
        if len(x) == 6 and (one[0] not in x or one[1] not in x):
            return x

def find3(input, one):
    input = input.split(' ')
    for x in input:
        if len(x) == 5 and one[0] in x and one[1] in x:
            return x

def find0(input, four, six):
    input = input.split(' ')
    for x in input:
        if len(x) == 6 and x != six and not allin(four, x):
            return x

def find9(input, zero, six):
    input = input.split(' ')
    for x in input:
        if len(x) == 6 and x != zero and x != six:
            return x

def find5(input, three, six):
    input = input.split( ' ')
    for x in input:
        if len(x) == 5 and x != three and allin(x, six):
            return x

def find2(input, three, five):
    input = input.split(' ')
    for x in input:
        if len(x) == 5 and x != three and x != five:
            return x


## alles in 1
def findall(input):
    one = find1(input)
    four = find4(input)
    seven = find7(input)
    eight = find8(input)

    six = find6(input, one)
    three = find3(input, one)
    zero = find0(input, four, six)
    nine = find9(input, zero, six)
    five = find5(input, three, six)
    two = find2(input, three, five)

    return (zero, one, two, three, four, five, six, seven, eight, nine)


# de values vinden
def findvalue(input, input2):
    A = findall(input)

    result = ''
    input2 = input2.split(' ')
    for x in input2:
        for i in range(len(A)):
            if allin(x, A[i]) and len(x) == len(A[i]): 
                result += str(i)
    
    return int(result)


#### nu voor mijn input
with open('8.txt') as fh:
    content = fh.read().split("\n")


total = 0
for x in content:
    x = x.split(' | ')
    total += findvalue(x[0], x[1])
print(total) # 1070188
