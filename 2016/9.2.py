with open('9.txt') as fh:
    string = fh.read()


i = len(string) - 1
memo = {}
while i >= 0:
    char = string[i]

    if not (char in '()x' or char.isnumeric()):
        memo[i] = 1

    else:
        end = i
        memo[i] = 0

        while True:
            i -= 1
            memo[i] = 0
            char = string[i]
            if char == '(':
                start = i
                break

        a, b = string[start+1:end].split('x')
        a, b = int(a), int(b)

        for x in range(end+1, end+a+1):
            memo[x] *= b

    i -= 1


print(sum(memo.values())) # 11797310782
