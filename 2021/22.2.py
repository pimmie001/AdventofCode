def nn(x):
    return max(0, x)


def overlappingarea(A,B):
    """finds overlapping area of B in A
    A and B should be given as A = xmin,xmax,ymin,ymax"""
    x1min, x1max = A[0], A[1]
    y1min, y1max = A[2], A[3]
    x2min, x2max = B[0], B[1]
    y2min, y2max = B[2], B[3]

    olapx = nn(min(x1max, x2max) - max(x1min, x2min))
    olapy = nn(min(y1max, y2max) - max(y1min, y2min))
    
    return olapx * olapy


def overlappingvolume(A,B):
    """finds overlapping volume of B in A
    A and B should be given as A = xmin,xmax,ymin,ymax,zmin,zmax"""

    x1min, x1max = A[0], A[1]
    y1min, y1max = A[2], A[3]
    z1min, z1max = A[4], A[5]
    x2min, x2max = B[0], B[1]
    y2min, y2max = B[2], B[3]
    z2min, z2max = B[4], B[5]

    # olapx = nn(min(x1max, x2max) - max(x1min, x2min))
    # olapy = nn(min(y1max, y2max) - max(y1min, y2min))
    # olapz = nn(min(z1max, z2max) - max(z1min, z2min))

    x = [max(x1min, x2min), min(x1max, x2max)]
    y = [max(y1min, y2min), min(y1max, y2max)]
    z = [max(z1min, z2min), min(z1max, z2max)]
    
    if x[0] < x[1] and y[0] < y[1] and z[0] < z[1]:
        return x + y + z
    else:
        return [0]*6

def overlap(A):
    # finds overlapping values of A for all in A
    B = A[0]
    for i in range(1, len(A)):
        B = overlappingvolume(B, A[i])
    return B

def vol(A):
    return (A[1] - A[0]) * (A[3] - A[2]) * (A[5] - A[4])




def union(A):
    if len(A) == 1: return vol(A[0])

    return union(A[:-1]) + union(A[-1]) - intersect(A[:-1], A[-1])








A = (0,10,0,10,0,1)
B = (5,15,0,11,0,1)
C = (3,7,-4,2,0,1)

Big = [A,B,C]



# A = (0, 10, 0, 10,1,2) 
# B = (8, 11, -2, 7,1,2)
# C = (-2, 12,-2,2, 1,2)

# print(vol(overlap([A,B,C])))












with open('22.2.txt') as f:
    content = f.read().split('\n')





# instructions = []
# for i in content:
#     j = i.split()
#     word = j[0]
#     j = j[1].split(',')
#     xrange = j[0].replace('x=','').split('..')
#     yrange = j[1].replace('y=','').split('..')
#     zrange = j[2].replace('z=','').split('..')

#     if word == 'on':
#         instructions.append((True, int(xrange[0]), int(xrange[1]), int(yrange[0]), int(yrange[1]), int(zrange[0]), int(zrange[1])))
#     else:
#         instructions.append((False, int(xrange[0]), int(xrange[1]), int(yrange[0]), int(yrange[1]), int(zrange[0]), int(zrange[1])))


# allon = 0
# for i in range(len(instructions)):
#     x = instructions[i]
#     if x[0]:
#         allon += vol(x[1:])
#         # substract correction terms, substracts too much
#         for j in range(i+1, len(instructions)):
#             y = instructions[j]
#             if y[0]:
#                 allon -= vol(overlappingvolume(x[1:], y[1:]))



# grid = {}
# for i in instructions:
#     if i[0]:
#         for x in range(i[1], i[2] + 1):
#             for y in range(i[3], i[4] + 1):
#                 for z in range(i[5], i[6] + 1):
#                     grid[x,y,z] = 1





















# # idea: make boxes and cut these boxes if things get turned off (into for example, 3 smaller boxes)
# # a lot of work and most likely not efficient

# def nn(x):
#     return max(0, x)


# def cut(A,B): # DOES NOT WORK AT ALL
#     x1min, x1max = A[0], A[1]
#     y1min, y1max = A[2], A[3]
#     x2min, x2max = B[0], B[1]
#     y2min, y2max = B[2], B[3]

#     C = [] # list of cuts to be considered
#     C.append((x1min,x2min,y1min,y2min))
#     C.append((x2min,x2max,y1min,y2min))
#     C.append((x2max,x1max,y1min,y2min))
#     C.append((x2max,x1max,y2min,y2max))
#     C.append((x2max,x1max,y2max,y1max))
#     C.append((x2min,x2max,y2max,y1max))
#     C.append((x1min,x2min,y2max,y1max))
#     C.append((x1min,x2min,y2min,y2max))

#     C2 = []
#     for c in C:
#         if c[0] < c[1] and c[2] < c[3]:
#             C2.append(c)


#     return C2



# A = (0, 10, 0, 10)
# B = (8, 11, -2, 7)


# print(cut(A,B))