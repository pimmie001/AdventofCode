def removeparentheses(equation):
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

    answer=solve(newequation)
    finalequation=before+str(answer)+after
    return finalequation
   
def solve(equation):
    if "(" in equation:
        return solve(removeparentheses(equation))

    eq=equation.split()
    k=len(eq)
    while len(eq)>=3:
        part1=eq[:3]
        part2=eq[3:]
        op1=int(part1[0])
        operator=part1[1]
        op2=int(part1[2])
        if operator=="+":
            number=op1+op2
            eq=part2
            eq.insert(0,str(number))

        elif operator=="*":
            number=op1*op2
            eq=part2
            eq.insert(0,str(number))
    return int(eq[0])

with open("18.txt") as fh:
    content=fh.read().split("\n")

total=0
for equation in content:
    total+=solve(equation)
print(total)    # 67800526776934
