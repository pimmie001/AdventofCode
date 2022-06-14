fh=open("11.txt")
content=fh.read()
fh.close
matrix=content.split("\n")
newmatrix=matrix.copy()

def seatsinvision(x,y,matrix):
    seatcount=0
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(1,max(len(matrix),len(matrix[0]))):
                if i==j==0:
                    break
                # print("{},{}".format(k*i,k*j))
                if y+i*k<0 or y+i*k>=len(matrix):
                    break
                if x+j*k<0 or x+j*k>=len(matrix[0]):
                    break

                if matrix[k*i+y][k*j+x]=="L":
                    break
                elif matrix[k*i+y][k*j+x]=="#":
                    seatcount+=1
                    break
                
    return seatcount

while True:
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            underboundy=max(-1,-y)
            underboundx=max(-1,-x)
            upperboundy=min(len(matrix)-y,2)
            upperboundx=min(len(matrix[0])-x,2)
            if matrix[y][x]==".":
                continue

            elif matrix[y][x]=="L":
                seats=seatsinvision(x,y,matrix)
                if seats==0:
                    string=newmatrix[y]
                    part1=string[:x]
                    part2=string[x+1:]
                    newstring=part1+"#"+part2
                    newmatrix[y]=newstring

            elif matrix[y][x]=="#":
                seats=seatsinvision(x,y,matrix)
                if seats>=5:
                    string=newmatrix[y]
                    part1=string[:x]
                    part2=string[x+1:]
                    newstring=part1+"L"+part2
                    newmatrix[y]=newstring
                
    if matrix==newmatrix:
        break
    matrix=newmatrix.copy()

seatcount=0
for y in matrix:
    for x in y:
        if x=="#":
            seatcount+=1
print(seatcount)