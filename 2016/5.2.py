import hashlib as hl

ID = "cxdnnyjw"
P = {}
test = []       # so numbers dont get replaced 

count = 0
i = 0
while count < 8:
    string = ID + str(i)
    hexa = hl.md5(string.encode()).hexdigest()
    
    if hexa[:5] == "00000":
        if hexa[5].isnumeric() and int(hexa[5]) < 8 and int(hexa[5]) not in test:
            P[int(hexa[5])] = hexa[6]
            count += 1
            test.append(int(hexa[5]))

    i += 1

password = ""
for i in range(8):
    password += P[i]

print(password)     # 999828ec