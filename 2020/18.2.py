def removeparentheses(equation): # from part 1 hopefully still works
    before=""
    i=0
    while True:
        if equation[i]=="(":
            indexopen=i
            break
        before+=equation[i]
        i+=1
    
    count=1
    i=indexopen+1
    while True:
        if equation[i]==")":
            count-=1
        elif equation[i]=="(":
            count+=1
        if count == 0:
            indexclosed=i
            break
        i+=1

    newequation=""
    for i in range(indexopen+1,indexclosed):
        newequation+=equation[i]
    after=""
    for i in range(indexclosed+1,len(equation)):
        after+=equation[i]

    answer=solveplus(newequation)
    finalequation=before+str(answer)+after
    return finalequation

def solveplus(equation):
    if "(" in equation:
        return solveplus(removeparentheses(equation))
    
    equation=equation.split(" ")

    if "+" in equation:
        i=0
        for op in equation:
            if op=="+":
                firstplus=i
                break
            i+=1
        operand1=equation[firstplus-1]
        operand2=equation[firstplus+1]
        
        begin=""
        for i in range(firstplus-1):
            begin+=equation[i]+" "
        end=""
        for i in range(firstplus+2,len(equation)):
            end+=equation[i]+" "
        number=str(int(operand1)+int(operand2))+" "

        newequation=begin+number+end
        return solveplus(newequation)

    while "" in equation:
        equation.remove("")
    if "*" in equation:
        operand1=equation[0]
        operand2=equation[2]
        number=str(int(operand1)*int(operand2))+" "
        end=""
        for i in range(3,len(equation)):
            end+=equation[i]+" "
        newequation=number+end
        return solveplus(newequation)
        
    return int(equation[0])

with open("18.txt") as fh:
    content=fh.read().split("\n")

total=0
for equation in content:
    total+=solveplus(equation)
print(total)    # 340789638435483
