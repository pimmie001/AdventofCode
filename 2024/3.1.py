with open("3.txt") as fh:
    s = fh.read()


A = []
i = 0
look_for_mul = True

while i < len(s):

    if look_for_mul:
        if s[i:i+4] == 'mul(':
            a = ''
            i += 4
            look_for_mul = False
        else:
            i += 1

    else:
        char = s[i]

        if char == ')':
            A.append(a)
            look_for_mul = True

        elif char.isnumeric() or char == ',':
            a += char

        else:
            look_for_mul = True

        i += 1


total = 0
for a in A:
    x = a.split(',')
    total += int(x[0]) * int(x[1])
print(total) # part 1: 178538786

