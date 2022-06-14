import string
alphabet_string = string.ascii_lowercase
alphabet = list(alphabet_string)
vowels=["a", "e", "i", "o", "u"]
forbidden=["ab", "cd", "pq", "xy"]

fh=open("5.txt","r")
content=fh.read()
fh.close()
strings=content.split()

validcount=0

for i in range(len(strings)):
    string=strings[i]
    vowelcount=0
    for vowel in vowels:
        vowelcount+= string.count(vowel)
    if vowelcount < 3:
        continue

    dummy=0
    for forbiddenstring in forbidden:
        if string.count(forbiddenstring)>0:
            dummy=1
    if dummy==1:
        continue

    dummy2=0
    for j in alphabet:
        doubleletter=j+j
        tripleletter=j+j+j
        if string.count(doubleletter)>0:
            dummy2=1
    if dummy2==1:
        validcount+=1


print(validcount)


