with open("22.txt") as fh:
    content=fh.read().split("\n\n")

P1=content[0].split("\n")[1:]
P2=content[1].split("\n")[1:]
for i in range(len(P1)):
    P1[i]=int(P1[i])
for i in range(len(P2)):
    P2[i]=int(P2[i])

def play(P1,P2):    # return 1 if player 1 wins, 0 if player 2 wins 
    previousdecks1=[]
    previousdecks2=[]
    while True:
        if P1 in previousdecks1:         # om oneindige games te stoppen
            return [1, P1]
        if P2 in previousdecks2:
            return [1, P1]
        previousdecks1.append(P1.copy())        # kopie zodat de decks niet automatisch updaten
        previousdecks2.append(P2.copy())

        card1=P1[0]
        card2=P2[0]
        P1.remove(card1)
        P2.remove(card2)
        if len(P1)>=card1 and len(P2)>=card2:
            A=P1[:card1]
            B=P2[:card2]
            if play(A,B)[0] == 1:      #  kopie maken omdat je het originele deck niet wilt veranderen
                W="1"           # 1 en 2 in string geven winnaars aan in een ronde, 1 en 2 als int geven winnaars aan van (sub)games
            else:
                W="2"
        else: 
            if card1>card2:
                W="1"
            else: 
                W="2"

        if W=="1":
            P1.append(card1)
            P1.append(card2)
        elif W=="2":
            P2.append(card2)
            P2.append(card1)
        
        if len(P1)==0:
            return [2, P2]           
        elif len(P2)==0:
            return [1, P1]

winner,winnerdeck=play(P1.copy(),P2.copy())
score=0
for i in range(1,len(winnerdeck)+1):
    score+= winnerdeck[-i]*i
print("player",winner,"won with score:",score)
# answer is 34031