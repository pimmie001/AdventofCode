import string
alphabet = list(string.ascii_lowercase)

def place(letter):
    return alphabet.index(letter)
def letter(place):
    return alphabet[place % 26]

tofind = "NorthPole"

with open("4.txt") as file:
    content = file.read().split("\n")

for x in content: 
    x = x.split("[")[0]
    x = x.split("-")
    sectorID = int(x[-1])
    y = ""
    for i in range(len(x)-1):
        y += x[i]
        y += " "

    z = ""
    for l in y:
        if l == " ":
            z += " "
        else: 
            z += letter(place(l) + sectorID)

    # print(z)
    if tofind.lower() in z:
        print(sectorID)     # 324