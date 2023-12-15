with open('15.txt') as fh:
    string = fh.read()

# string = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7' # example

total = 0
for substring in string.split(','):
    val = 0
    for char in substring:
        val += ord(char)
        val *= 17
        val %= 256
    total += val
print(total) # part 1: 505379


##### part 2

## functions
def get_box(intruction):
    val = 0
    for char in intruction:
        val += ord(char)
        val *= 17
        val %= 256
    return val


def evaluate_instruction(instruction, boxes, lengths):
    if '-' in instruction:
        label = instruction[:-1]
        box = get_box(label)

        if label in boxes[box]:
            boxes[box].remove(label)

    else:
        label, length = instruction.split('=')
        box = get_box(label)

        if label in boxes[box]:
            boxes[box][boxes[box].index(label)] = label
            lengths[label] = length
        else:
            boxes[box].append(label)
            lengths[label] = length

    return


## evaluate instructions
lengths = {}
boxes = {i:[] for i in range(256)}

for instruction in string.split(','):
    evaluate_instruction(instruction, boxes, lengths)


## extract solution
grand_total = 0
for box in range(256):
    for i,label in enumerate(boxes[box]):
        grand_total += (box+1) * (i+1) * int(lengths[label])
print(grand_total) # part 2: 263211
