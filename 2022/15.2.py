import re
import time

with open('15.txt') as fh:
    input = fh.read().split('\n')

sensors = {}
for line in input:
    n = [int(x) for x in re.findall('[-0-9]+', line)]
    sensors[n[0],n[1]] = n[2], n[3]


def combine_intervals(intervals, i=0):
    # intervals should be sorted (on first element)
    # assumes integer coordinates, [(0,3), (4, 6)] --> [(0, 6)]

    while i < len(intervals)-1:
        a, b = intervals[i]
        c, d = intervals[i+1]

        if b+1 >= c: 
            return combine_intervals([*intervals[:i], (a, max(b,d)), *intervals[i+2:]], i)
        else:
            i += 1

    return intervals


border = 0, 4000000
def check(y):
    A = [] 
    for a in sensors:

        b = sensors[a]
        dist = abs(a[0]-b[0]) + abs(a[1]-b[1])
        dist_y = dist - abs(y - a[1])

        if dist_y >= 0:
            C = -dist_y+a[0], dist_y+a[0]
            A.append((max(border[0], C[0]), min(border[1], C[1])))


    A.sort(key = lambda x: x[0])
    intervals = combine_intervals(A)

    if len(intervals) > 1:
        x = intervals[0][1]+1
        print(border[1]*x + y)


start = time.time()
for y in range(border[1]+1):
    check(y) # 11558423398893
end = time.time() - start
print(end) # takes about 2 min 