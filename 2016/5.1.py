import hashlib as hl

ID = "cxdnnyjw"
password = ""

i = 0
while len(password) < 8:
    string = ID + str(i)
    hexa = hl.md5(string.encode()).hexdigest()
    
    if hexa[:5] == "00000":
        password += hexa[5]

    i += 1

print(password)             # f77a0e6e
