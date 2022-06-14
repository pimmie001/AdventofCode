def AND(a,b):
    c = "0"*16
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            c = c[:i] + "1" + c[i+1:]
            # c[i] = '1'
    return c

def OR(a,b):
    c = "0"*16
    for i in range(len(a)):
        if a[i] == '1' or b[i] == '1':
            c = c[:i] + "1" + c[i+1:]
    return c

def NOT(a):
    b = "0"*16
    for i in range(len(a)):
        if a[i] == '0':
            b = b[:i] + "1" + b[i+1:]
            #b[i] = '1'
        else:
            b = b[:i] + "0" + b[i+1:]
    return b

def LSHIFT(a,n):
    b = ""
    for i in range(n,len(a)):
        b += a[i]
    b += "0"*n
    return b

def RSHIFT(a,n):
    b = "0"*n
    for i in range(len(a)-n):
        b += a[i]
    return b

def bintodec(a,bits=16):
    b = 0
    for i in range(len(a)):
        if a[i] == "1": 
            b += 2**(bits-i-1)
    return b

def dectobin(a,bits=16):
    b = ""
    for i in range(bits-1,-1,-1):
        if a >= 2**i:
            b += "1" 
            a -= 2**i
        else:
            b += "0"
    return b



D = {}

with open("7.1.txt") as fh:
    content = fh.read().split("\n")


# content = ["NOT x -> h"]
while len(content) > 1:
    ### print(len(content))


    for line in content:

        target = line.split("->")[0]
        target = target.replace("NOT","").replace("AND","").replace("RSHIFT","").replace("LSHIFT","").replace("OR","")
        sources = target.split(" ")
        sources = list( filter(lambda name: name.strip(), sources) )
        
        dummy = False
        

        for x in sources:
            try:
             x = int(x)
            except:
                pass

            if D.get(x) == None and (not isinstance(x,int)):
                dummy = True
        
            

        if dummy:
            continue
        else: 
            content.pop(content.index(line))


            line = line.replace(" ","")

            if "AND" in line:
                line = line.split("AND")
                v1 = line[0]
                line = line[1]
                line = line.split("->")
                v2 = line[0] 
                t = line[1]

                ### meest random if statement omdat ik iets over het hoofd had gezien en niet alles wilde aanpassen
                if "1" in v1:
                    n1 = dectobin(1)
                else: 
                    n1 = dectobin(D[v1])

                n2 = dectobin(D[v2])

                D[t] = bintodec( AND(n1,n2) )

            elif "OR" in line:
                line = line.split("OR")
                v1 = line[0]
                line = line[1]
                line = line.split("->")
                v2 = line[0] 
                t = line[1]
                n1 = dectobin(D[v1])
                n2 = dectobin(D[v2])

                D[t] = bintodec( OR(n1,n2) )

            elif "LSHIFT" in line:
                line = line.split("LSHIFT")
                v1 = line[0]
                line = line[1].split("->")
                shift = int(line[0])
                t = line[1]
                n1 = dectobin(D[v1])
                
                D[t] = bintodec( LSHIFT(n1, shift))

            elif "RSHIFT" in line:
                line = line.split("RSHIFT")
                v1 = line[0]
                line = line[1].split("->")
                shift = int(line[0])
                t = line[1]
                n1 = dectobin(D[v1])
                
                D[t] = bintodec( RSHIFT(n1, shift))

            elif "NOT" in line:
                line = line.split("NOT")[1].split("->")
                v1 = line[0]
                t = line[1]
                n1 = dectobin(D[v1])

                D[t] = bintodec( NOT(n1))

            else: 
                line = line.split("->")
                n1 = int( line[0] )
                t = line[1]

                D[t] = n1

D['a'] = D['lx']

print(D['a'])

