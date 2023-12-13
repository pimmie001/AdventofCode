with open('13.txt') as fh:
    content = fh.read().split("\n\n")
    patterns = [x.split('\n') for x in content]


def mirrorx(pattern, x):
    """Checks if there is a vertical mirror where x is the number of columns left of the mirror"""

    n = len(pattern) # nr of rows
    m = len(pattern[0]) # nr of columns
    xright = m - x # number of columns right of the mirror

    for x2 in range(min(x, xright)):
        for y in range(n):
            if pattern[y][x-x2-1] != pattern[y][x+x2]:
                return False
    return True


def mirrory(pattern, y):
    """Checks if there is a horizontal mirror where y is the number of rows above the mirror"""

    n = len(pattern) # nr of rows
    m = len(pattern[0]) # nr of columns
    yunder = n - y # nr of rows below mirror

    for y2 in range(min(y, yunder)):
        for x in range(m):
            if pattern[y-y2-1][x] != pattern[y+y2][x]:
                return False
    return True


vertical = []
horizontal = []
for pattern in patterns:
    for x in range(len(pattern[0])):
        if mirrorx(pattern, x):
            vertical.append(x)
    for y in range(len(pattern)):
        if mirrory(pattern, y):
            horizontal.append(y)

total = 0
for x in vertical:
    total += x
for y in horizontal:
    total += 100*y
print(total) # part 1: 30705


### part 2
def get_new_patterns(pattern):
    """Given a pattern, generate new patterns"""

    n = len(pattern)
    m = len(pattern[0])

    new_patterns = []
    for y in range(n):
        for x in range(m):
            new_pattern = pattern.copy()
            if new_pattern[y][x] == '#':
                new_pattern[y] = new_pattern[y][:x] + '.' + new_pattern[y][x+1:]
            else:
                new_pattern[y] = new_pattern[y][:x] + '#' + new_pattern[y][x+1:]
            new_patterns.append(new_pattern)

    return new_patterns


def get_score(pattern):
    """Get (new) score of pattern"""

    # first find previous mirror line
    oldx = []
    oldy = []
    for x in range(len(pattern[0])):
        if mirrorx(pattern, x):
            oldx.append(x)
    for y in range(len(pattern)):
        if mirrory(pattern, y):
            oldy.append(y)

    for pat in get_new_patterns(pattern):
        for x in range(len(pat[0])):
                if x in oldx:
                    continue # must be differnt line
                if mirrorx(pat, x):
                    return x
        for y in range(len(pat)):
            if y in oldy:
                continue # must be differnt line
            if mirrory(pat, y):
                return 100*y

total = 0
for pattern in patterns:
    total += get_score(pattern)
print(total) # part 2: 44615
