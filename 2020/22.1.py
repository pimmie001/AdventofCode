with open("22.txt") as fh:
    content=fh.read().split("\n\n")

P1=content[0].split("\n")[1:]
P2=content[1].split("\n")[1:]
for i in range(len(P1)):
    P1[i]=int(P1[i])
for i in range(len(P2)):
    P2[i]=int(P2[i])

def play(P1,P2):
    while len(P1)>0 and len(P2)>0:
        card1=P1[0]
        card2=P2[0]
        P1.remove(card1)
        P2.remove(card2)
        if card1>card2:
            P1.append(card1)
            P1.append(card2)
        else: 
            P2.append(card2)
            P2.append(card1)


    if len(P1)==0:
        return 2, P2
    else: 
        return 1, P1

winner,winnerdeck=play(P1,P2)
score=0
for i in range(1,len(winnerdeck)+1):
    score+= winnerdeck[-i]*i
print("player",winner,"won with score:",score)