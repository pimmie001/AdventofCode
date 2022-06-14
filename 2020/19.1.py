with open("19.txt") as fh:
    content=fh.read().split("\n\n")
ruleslist=content[0].split("\n")
messages=content[1].split("\n")

letters={}
A={}
for i in range(len(ruleslist)):
    letters[i]=[]
    A[i]=[]

knownlist=[]
rules=[]
for rule in ruleslist:
    rule=rule.split(":")
    rule[0]=int(rule[0])
    i=rule[0]
    rules.append(rule[1])
    if "a" in rule[1]:
        letters[i]=["a"]
        knownlist.append(i)
    if "b" in rule[1]:
        letters[i]=["b"]
        knownlist.append(i)

    for s in rule[1]:
        try:
            s=int(s)
            B=A[i]
            if s not in B:
                B.append(s)
            B=sorted(B)
            A[i]=B
        except:
            pass

for key in A:
    if key in knownlist:
        continue
    values=A[key]
    dummy=1
    for number in values:
        if not number in knownlist:
            dummy=0

    if dummy==1:
        rule=rules[key]
        answer=""
        if "|" in rule:
            rule=rule.split("|")
            

# print(A)
# print(letters)

