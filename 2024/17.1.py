### input
register = {
    "A": 59590048,
    "B": 0,
    "C": 0
    }
program = 2,4,1,5,7,5,0,3,1,6,4,3,5,5,3,0


### solution
def get_operand(x):
    if x < 4:
        return x
    if x < 7:
        return register[{4:"A", 5:"B", 6:"C"}[x]]
    raise ValueError(f"Erro: x equals {x}")


pointer = 0
output = []
while pointer < len(program):
    jump = True

    opcode = program[pointer]
    literal_operand = program[pointer + 1]
    combo_operand = get_operand(program[pointer + 1])

    if opcode == 0:
        register["A"] = register["A"] // (2 ** combo_operand)
    elif opcode == 1:
        register["B"] = register["B"] ^ literal_operand 
    elif opcode == 2:
        register["B"] = combo_operand % 8
    elif opcode == 3:
        if register["A"]:
            pointer = literal_operand
            jump = False
    elif opcode == 4:
        register["B"] = register["B"] ^ register["C"]
    elif opcode == 5:
        output.append(combo_operand % 8)
    elif opcode == 6:
        register["B"] = register["A"] // (2 ** combo_operand)
    elif opcode == 7:
        register["C"] = register["A"] // (2 ** combo_operand)

    if jump:
        pointer += 2

print(",".join([str(x) for x in output])) # part 1: 6,5,7,4,5,7,3,1,0
