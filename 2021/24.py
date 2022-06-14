with open('24.txt') as fh:
    instructions = fh.read().split('\n')


splitted = []
A = []
first = False
for ins in instructions:
    if 'inp' in ins:
        if first:
            splitted.append(A)
            A = []
            A.append(ins)
        else: 
            first = True
            A.append(ins)
    else:
        A.append(ins)
splitted.append(A)


def valid(instructions, model_number, A = {}):
    model_number = str(model_number)
    if '0' in model_number:
        print('\n0 in model number!!!!!\n')
        return [False]

    A = A.copy()
    letters = 'wxyz'
    for l in letters:
        if l not in A:
            A[l] = 0

    inpcount = 0
    for instruction in instructions:
        ins = instruction.split()
        if ins[0] == 'inp':
            A[ins[1]] = int(model_number[inpcount])
            inpcount += 1

        elif ins[0] == 'add':
            if ins[2] in letters:
                A[ins[1]] += A[ins[2]]
            else: 
                A[ins[1]] += int(ins[2])

        elif ins[0] == 'mul':
            if ins[2] in letters:
                A[ins[1]] *= A[ins[2]]
            else: 
                A[ins[1]] *= int(ins[2])

        elif ins[0] == 'div': # divide and round towards 0 
            if ins[2] in letters:
                A[ins[1]] =  int(A[ins[1]] / A[ins[2]])
            else: 
                A[ins[1]] = int(A[ins[1]] / int(ins[2]))

        elif ins[0] == 'mod':
            if ins[2] in letters:
                A[ins[1]] %= A[ins[2]]
            else: 
                A[ins[1]] %= int(ins[2])

        elif ins[0] == 'eql':
            if ins[2] in letters:
                A[ins[1]] = 1 if A[ins[1]] == A[ins[2]] else 0
            else:
                A[ins[1]] = 1 if A[ins[1]] == int(ins[2]) else 0

        else: print('something went wrong')

    return A['z']
    # return (True, A['z']) if A['z'] == 0 else [False]



A = {i:[] for i in range(len(splitted))}
B = {i:[] for i in range(len(splitted))}


i = 0
part = splitted[i]
for w in range(9,0,-1): # reverse so highest number gets the place
    result = valid(part, w) # value of z 
    if result not in A[i]:
        A[i].append(result)
        B[i].append(w)
A[i].sort()

for i in range(1, len(splitted) - 6):
    part = splitted[i]
    # A[i] = A[i-1].copy()
    for z in A[i-1]:
        for w in range(9,0,-1):
            result = valid(part, w, A = {'z':z})
            if result not in A[i]:
                A[i].append(result)
                B[i].append(w)

    print(len(A[i]))




























# n = int('9'*14)
# while True:
#     r = valid(instructions, n)
#     if r[0]:
#         print(n)
#         break
#     n -= 1


















# # find largest 14 digit number that satisfies z = 0 in the end
# # idea is to use backwards induction to limit some of the digits
# rev = instructions[::-1]

# index = 1

# letters = 'wxyz'
# L = {l:0 for l in letters}
# print(L)    
# for instruction in rev:
#     ins = instruction.split(' ')

#     if ins[0] == 'add':
#         if ins[2] in letters:
#                 L[ins[2]] -=  L[ins[1]]
#         else:
#             L[ins[1]] -= int(ins[2])

#     elif ins[0] == 'mul':
#         if ins[2] in letters:
#             if L[ins[1]] != 0:
#                 L[ins[2]] /=  L[ins[1]]
#         elif ins[2] != '0':
#             L[ins[1]] /= int(ins[2])
#         else: L[ins[1]] = 0 ################

#     elif ins[0] == 'div':
#         if ins[2] in letters:
#             L[ins[2]] *= L[ins[1]]
#         else:
#             L[ins[1]] *= int(ins[2])

#     elif ins[0] == 'eql':
#         if ins[2] in letters:
#             if L[ins[1]] == 1:
#                 L[ins[2]] = L[ins[1]]
#         else:
#             if L[ins[1]] == 1:
#                 L[ins[1]] = int(ins[2])


#     else:
#         print(ins[0])

#     print(L)






















# def valid(instructions, model_number):
#     model_number = str(model_number)
#     if '0' in model_number:
#         return False
    
#     A = {}
#     for l in ('w', 'x', 'y', 'z'):
#         A[l] = 0

#     inpcount = 0
#     for instruction in instructions:
#         ins = instruction.split(' ')
#         if ins[0] == 'inp':
#             A[ins[1]] = int(model_number[inpcount])
#             inpcount += 1
#         elif ins[0] == 'add':
#             A[ins[1]] += int(ins[2]) if ins[2].replace('-','').isnumeric() else A[ins[2]]
#         elif ins[0] == 'mul':
#             A[ins[1]] *= int(ins[2]) if ins[2].replace('-','').isnumeric() else A[ins[2]]
#         elif ins[0] == 'div':
#             A[ins[1]] /= int(ins[2]) if ins[2].replace('-','').isnumeric() else  A[ins[2]]
#         elif ins[0] == 'mod':
#             A[ins[1]] %= int(ins[2]) if ins[2].replace('-','').isnumeric() else  A[ins[2]]
#         elif ins[0] == 'eql':
#             if ins[2].replace('-','').isnumeric():
#                 A[ins[1]] = 1 if A[ins[1]] == int(ins[2]) else 0
#             else:
#                 A[ins[1]] = 1 if A[ins[1]] == A[ins[2]] else 0

#     return True if A['z'] == 0 else False



# model_number = 13579246899999
# model_number = 99999999999999
# while True:
#     if valid(instructions, model_number):
#         print(model_number)
#         break
#     model_number -= 1


