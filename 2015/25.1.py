def sum(end,start=0):
    # returns sum_{i=start}^end i
    return (end*(end+1) - start*(start-1))//2

def number(x,y):
    # returns number corresponding to row = x and column = y
    result = sum(end=y)     # number in 1,y position
    result += sum(start = y, end = x+y-2)    # add extra for row position
    return result

def next(n = 0):
    if n == 0:
        return 20151125
    return (n * 252533) % 33554393


##### input: 2947, 3029
row = 2947
col = 3029

magic_number = number(row,col)

n = 0
for i in range(magic_number):
    n = next(n)
print(n)
