fh=open("8.txt")
content=fh.read()
fh.close
instructions=content.split("\n")

accumulator=0
listofinstructionsdone=[]

i=0
while not(i in listofinstructionsdone):
    line=instructions[i]
    line=line.split()
    number=int(line[1])
    instruction=line[0]
    if instruction=="nop":
        listofinstructionsdone.append(i)
        i+=1
        continue
    elif instruction=="acc":
        accumulator+=number
        listofinstructionsdone.append(i)
        i+=1
        continue
    elif instruction=="jmp":
        listofinstructionsdone.append(i)
        i+=number
        continue

print(accumulator)