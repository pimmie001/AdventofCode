with open("17.txt") as fh:
    content=fh.read().split("\n")

size=8       
A=[]        # A[z][y][x]
for x in range(-size,size+1):
    K=[]
    for y in range(-size,size+1):
        L=[0]*(size*2+1)
        K.append(L)
    A.append(K)
        
for i in range(len(content)):
    for j in range(len(content[0])):
        X=content[i][j]
        if X=="#":
            A[size//2][size//2][size//2]=1

def neighbourcount(A,x,y,z):
    result=0
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                if i==j==k==0:
                    continue
                try:
                    if A[z+i][y+j][x+k]==1:
                        result+=1
                except:
                    continue
    return result

for loop in range(1):   
    B=A.copy()
    for x in range(size,size+1):
        for y in range(size,size+1):
            for z in range(size,size+1):
                activecount=neighbourcount(A,x,y,z)
                # activecount=0
                # for i in range(-1,2):
                #     for j in range(-1,2):
                #         for k in range(-1,2):
                #             if i==j==k==0:  # niet zichzelf meetellen
                #                 continue 
                #             try:
                #                 if A[z+k][y+j][x+i]==1:
                #                     activecount+=1
                #             except:
                #                 pass

                if A[z][y][x]==1:       # active
                    if activecount!=2 and activecount!=3:
                        B[z][y][x]=0
                elif A[z][y][x]==0:     # unactive
                    if activecount==3:
                        B[z][y][x]=1
    A=B.copy()                 


# totalcount=0
# for z in A:
#     for y in z:
#         for x in y:
#             if x==1:
#                 totalcount+=1
# print(totalcount)

print(B)
