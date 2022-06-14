fh=open("11.txt")
content=fh.read()
fh.close
matrix=content.split("\n")
newmatrix=matrix.copy()

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
                dummy=1
                for i in range(underboundy,upperboundy):
                    for j in range(underboundx,upperboundx):
                        if matrix[y+i][x+j]=="#":
                            dummy=0          
                if dummy==1:
                    string=newmatrix[y]
                    part1=string[:x]
                    part2=string[x+1:]
                    newstring=part1+"#"+part2
                    newmatrix[y]=newstring

            elif matrix[y][x]=="#":
                adjacentseatcount=-1
                for i in range(underboundy,upperboundy):
                    for j in range(underboundx,upperboundx):
                        if matrix[y+i][x+j]=="#":
                            adjacentseatcount+=1
                if adjacentseatcount>=4:
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


