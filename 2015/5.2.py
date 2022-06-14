import string
alphabet_string = string.ascii_lowercase
alphabet = list(alphabet_string)

fh=open("5.txt","r")
content=fh.read()
fh.close()
strings=content.split()

validcount=0

for string in strings:
    dummy=0
    for i in alphabet:
        for j in alphabet:
            substring=i+j
            if string.count(substring)>=2:
                dummy=1

    dummy2=0
    for letter in alphabet:
        for i in range(len(string)-2):
            if string[i]==letter and string[i+2]==letter:
                dummy2=1
    
    if dummy==1 and dummy2==1:
        validcount+=1

print(validcount)
            
        