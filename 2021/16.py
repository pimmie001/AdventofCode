with open('16.txt') as fh:
    hexastring = fh.read()




def decode(hexastring):
    hexa = [str(x) for x in range(10)]
    hexa.extend((('A','B','C','D','E','F')))
    result = ""
    for x in hexastring:
        y = bin(hexa.index(x))[2:]
        y = '0'*(4-len(y)) + y 
        result += y
    return result



def version(string):
    if string == '':
        print('wtk')
        return 0

    total = 0
    V = int(string[:3], 2) # version
    T = int(string[3:6], 2) # type ID

    total += V

    if T == 4:
        remainder = string[6:]
        V += int(remainder[:3], 2)

        # concat = ''

        # while True:
        #     concat += remainder[1:5]
        #     if remainder[0] == '0': break
        #     remainder = remainder[5:]      
        # total += int(concat, 2)


    else:
        I = int(string[6], 2)
        if I == 0: # L = total length
            L = int(string[7:7+15], 2)
            remainder = string[7+15:]
            remainder = remainder[:L]

            subs = getsubs(remainder, L)
            for sub in subs:
                total += version(sub)

        elif I == 1: # L = number of packets
            L = int(string[7:7+11], 2)
            remainder = string[7+11:]

            for i in range(L):
                sub = remainder[i*11:(i+1)*11]
                total += version(sub)

    return total


def getsubs(remainder, L):
    subs = []
    howmany = L//11
    extra = L - howmany*11
    
    for i in range(howmany-1):
        sub = remainder[i*11:(i+1)*11]
        subs.append(sub)

    subs.append(remainder[-(11+extra):])

    return subs






hexastring = '38006F45291200'


string = decode(hexastring)

a = version(string)

print(a)



