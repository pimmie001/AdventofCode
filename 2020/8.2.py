fh=open("8.txt")
content=fh.read()
fh.close
instructions=content.split("\n")

dummy=0
for k in range(len(instructions)):
    instruction=instructions[k]
    instructions2=instructions.copy()
    instruction=instruction.split()
    operator=instruction[0]
    number=instruction[1]
    if operator=="acc":
        continue
    elif operator=="nop":
        instructions2[k]="jmp {}".format(number)
    elif operator=="jmp":
        instructions2[k]="nop {}".format(number)
    
    accumulator=0
    listofinstructionsdone=[]
    i=0
    dummy=1
    while i<len(instructions2):
        line=instructions2[i]
        line=line.split()
        number=int(line[1])
        instruction=line[0]        

        if i in listofinstructionsdone:
            dummy=0
            break

        if instruction=="nop":
            listofinstructionsdone.append(i)
            i+=1
        elif instruction=="acc":
            accumulator+= number
            listofinstructionsdone.append(i)
            i+=1
        elif instruction=="jmp":
            listofinstructionsdone.append(i)
            if number==0:
                i+=1
            else:
                i+=number

    if dummy==1:
        print(accumulator)
        break