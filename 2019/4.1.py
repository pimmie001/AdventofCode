puzzle_input = [178416,676461]

def valid(password):
    password=str(password)
    for i in range(len(password)-1):
        if password[i+1]<password[i]:
            return False
    for i in range(len(password)-1):
        if password[i+1]==password[i]:
            return True
    return False

count=0
for number in range(puzzle_input[0],puzzle_input[1]+1):
    if valid(number):
        count+=1
print(count)    # answer part 1: 1650


