puzzle_input = [178416,676461]

def valid(password):
    password=str(password)
    for i in range(len(password)-1):
        if password[i+1]<password[i]:
            return False
    for i in range(len(password)-1):
        if i == 0:
            if password[i]==password[i+1] and password[i+2]!=password[i]:
                return True
        elif i==len(password)-2:
            if password[i]==password[i+1] and password[i-1]!=password[i]:
                return True
        else:
            if password[i]==password[i+1] and password[i]!=password[i+2] and password[i]!=password[i-1]:
                return True
    return False

count=0
for number in range(puzzle_input[0],puzzle_input[1]+1):
    if valid(number):
        count+=1
print(count)    # answer part 2: 1129