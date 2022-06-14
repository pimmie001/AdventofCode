def f(x):
    i = 0
    result = ""
    while i < len(x):
        y = x[i]
        if y == "(":
            start = i
            while x[i] != ")": 
                i += 1
            instruction = x[start+1:i]
            a,b = instruction.split("x")
            z = x[i+1:i+1+int(a)]
            i += int(a)
            for j in range(int(b)):
                result += z
            
        else: result += y

        i += 1
    
    # print((result))
    return len(result)


with open("9.txt") as fh: x = fh.read()

print(f(x)) # 152851
