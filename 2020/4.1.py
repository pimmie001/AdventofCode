with open("4.txt","r") as file:
    content=file.read()
content2=content.split("\n\n")
validcount=0

for passport in content2:
    
    vector=[0]*7
    if passport.count("byr") == 1:
        vector[0]=1
    if passport.count("iyr") == 1:
        vector[1]=1
    if passport.count("eyr") == 1:
        vector[2]=1
    if passport.count("hgt") == 1:
        vector[3]=1
    if passport.count("hcl") == 1:
        vector[4]=1
    if passport.count("ecl") == 1:
        vector[5]=1
    if passport.count("pid") == 1:
        vector[6]=1

    vectorcount=0
    for x in vector:
        if x==1:
            vectorcount+=1
    
    if vectorcount==7:
        validcount+=1
        
print(validcount)