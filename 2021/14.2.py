with open('14.txt') as fh:
    content = fh.read().split("\n\n")
poly = content[0]
instructions = content[1].split('\n')

D = {}
letters = []
for x in instructions:
    y = x.split(' -> ')
    D[y[0]] = y[1]

    if y[1] not in letters: letters.append(y[1])
    if y[0][0] not in letters: letters.append(y[0][0])
    if y[0][1] not in letters: letters.append(y[0][1])

count = {} # example: {AB:1, BC: 3}
for i in letters:
    for j in letters:
        count[i+j] = 0
for i in range(len(poly) - 1):
    x = poly[i] + poly[i+1]
    count[x] += 1



def insert(count, D = D):
    newcount = count.copy()

    for pair in count:
        n = count[pair]
        if n > 0:
            newletter = D[pair]
            a = pair[0] + newletter
            b = newletter + pair[1]

            newcount[a] += n
            newcount[b] += n
            newcount[pair] -= n    

    return newcount


def countletters(count, letter):
    # vaklue is 1 too low if string would start and end with the letter
    result1 = 0
    result2 = 0
    for key in count:
        if key[0] == letter:
            result1 += count[key] 
        if key[1] == letter:
            result2 += count[key]
    return max(result1, result2)


n = 40
for i in range(n):
    count = insert(count, D)

allcounts = []
for letter in letters:
    allcounts.append(countletters(count, letter))
allcounts.sort()

print(allcounts[-1] - allcounts[0])


## First used a function that only returned result1. this could have an error of at most 1 --> 5 possibilities
## Taking the maximum of result1, result2 seems to do the trick
## 4439442043739 is the right answer