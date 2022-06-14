input = "1113122113"

n = 50

for k in range(n):
    i = 0
    output = ""
    while i < len(input):
        number = input[i]

        count = 0
        j = i 
        while j < len(input):
            if input[j] == number:
                count += 1
                j += 1
            else:
                break
        
        output += str(count) + number
        i += count
        
    input = output

print(len(output))

# 360154    for n = 40
# 5103798   for n = 50