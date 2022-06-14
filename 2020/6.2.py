import string
alphabet_string = string.ascii_lowercase
alphabet = list(alphabet_string)

fh=open("6.txt","r")
content=fh.read()
fh.close
groups=content.split("\n\n")

totalcount=0
for i in range(len(groups)):
    vector = [1]*26
    group=groups[i].split("\n")     #[abc],[a,b,c] of [ab,ac]
    for x in group:
        for letter in alphabet:
            if not(letter in x):
                vector[alphabet.index(letter)]=0
    for x in vector:
        totalcount+=x
        
print(totalcount)