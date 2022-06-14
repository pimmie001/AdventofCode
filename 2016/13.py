import numpy as np

n,m = 50,50
favnum = 1352

A = np.zeros((n,m))
for x in range(m):
    for y in range(n):
        if bin(x*x + 3*x + 2*x*y + y + y*y + favnum).count("1") % 2 == 1: A[(y,x)] = 1 
        

def length(maze, start, stop):
    # setup
    n,m = np.shape(maze)
    xstart,ystart = start
    xstop,ystop = stop
    B = np.zeros((n,m))

    # steps
    B[ystart,xstart] = 1 
    loopcount = 1
    while B[ystop,xstop] == 0:
        C = np.copy(B)
        for x in range(m):
            for y in range(n):
                if maze[y,x] == B[y,x] == 0:    # must not be a wall and must not have a number already
                    for i,j in [(1,0), (-1,0), (0,1), (0,-1)]:
                        try: 
                            if B[y+j,x+i] > 0:
                                C[y,x] = B[y+j,x+i] + 1
                        except: pass
        B = np.copy(C)

        loopcount += 1
        if loopcount > n*m:
            print("NO")
            return -1

    return int(np.amax(B)) - 1, B


print(length(A, (1,1),(31,39))[0])
# 90


### Part 2 

B = length(A, (1,1),(31,39))[1]
count = 0
for x in B:
    for y in x:
        if 1 <= y <= 51:      # 51 since we already start at 1 and then have 50 more steps (to 51)
            count += 1

print(count) 
# 135