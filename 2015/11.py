import string
alfabeth = list(string.ascii_lowercase)
increasingstraight = []
for i in range(len(alfabeth) -2):
    string = alfabeth[i] + alfabeth[i+1] + alfabeth[i+2]
    increasingstraight.append(string)


def valid(password):
    if "i" in password or "o" in password or "l" in password:
        # print("illegal letter")
        return False

    doublecount = 0
    for letter in alfabeth:
        double = letter + letter
        if double in password:
            doublecount += 1
    if doublecount < 2:
        # print("no doubles")
        return False
    
    for x in increasingstraight:
        if x in password:
            return True

    return False

def next(password):
    i = len(password) - 1

    while True:
        if password[i] != "z":
            index = alfabeth.index(password[i]) + 1 # returns index of the next letter in alfabeth
            password =  password[:i] + alfabeth[index] + password[i+1:]
            return password
        else:
            password = password[:i] + "a" + password[i+1:]
            i -= 1


password = "cqjxjnds"

while not valid(password):
    password = next(password)

print("Answer part 1: :",password)

### Part 2 
password = next(password)
while not valid(password):
    password = next(password)

print("Answer part 2: :",password)


