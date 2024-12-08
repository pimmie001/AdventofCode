with open("7.txt") as fh:
    content = fh.read().split('\n')


A = [] # list of final numbers
B = [] # list of list of numbers used in equation
for x in content:
    a, b = x.split(':')
    A.append(int(a))
    B.append([int(y) for y in b.split()])


def is_valid(a, b):
    """
    Checks if numbers in b can make value a by only using + and * and going right to left.
    Right to left is used to use popping numbers --> requires b to be reversed.
    """

    if len(b) == 1:
        return a == b[0]

    n = b.pop()
    m = b.pop()
    return is_valid(a, b + [n+m]) or is_valid(a, b + [n*m]) 


total = 0
for i in range(len(A)):
    if is_valid(A[i], B[i][::-1]):
        total += A[i]
print(total) # part 1: 4364915411363
