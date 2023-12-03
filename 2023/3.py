with open('3.txt') as fh:
    content = fh.read().split('\n')

content = [x+'.' for x in content] # add extra . for edge cases

n,m = len(content), len(content[0])


## find all numbers and coordinates

numbers = []
coordinates = []

prev_numeric = False
number = ''

for y in range(n):
    for x in range(m):
        char = content[y][x]

        if char.isnumeric():
            number += char

            if not prev_numeric:
                x_start = x
                y_coor = y

            prev_numeric = True

        else:
            x_end = (x-1)

            if number:
                numbers.append(int(number))
                coordinates.append((x_start, x_end, y_coor))

            number = ''
            prev_numeric = False



## function that determines if number is part number
def valid(coordinates):
    x_start, x_end, y_coor = coordinates

    for x in range(x_start-1, x_end+2):
        for y in range(y_coor-1, y_coor+2):
            if x < 0 or y < 0 or x >= m or y >= n:
                continue
            if content[y][x] != '.' and not content[y][x].isnumeric():
                return True
    return False


## get total
total = 0
for i in range(len(numbers)):
    if valid(coordinates[i]):
        total += numbers[i]
print(total) # part 1: 520019



###### part 2

## find coordinates gear
coordinates_gear = []
for y in range(n):
    for x in range(m):
        char = content[y][x]
        if char == '*':
            coordinates_gear.append((x,y))


## find gear ratio
def gear_ratio(x_g, y_g):
    A = []
    for i in range(len(numbers)):
        x_start, x_end, y_coor = coordinates[i]

        adjacents = []
        for x in range(x_start-1, x_end+2):
            for y in range(y_coor-1, y_coor+2):
                adjacents.append((x,y))

        if (x_g, y_g) in adjacents:
            A.append(numbers[i])

    if len(A) < 2:
        return 0
    return A[0] * A[1]


## get total
total2 = 0
for (x_g, y_g) in coordinates_gear:
    total2 += gear_ratio(x_g, y_g)
print(total2) # part 2: 75519888
