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

    if vectorcount==7:      # alle vereiste velden zijn er
    
        fields=passport.split()
        
        dummy=1

        for field in fields:
            field=field.split(":")
            field1=field[0]
            field2=field[1]
            
            if field1=="byr":
                if not(len(field2)==4 and int(field2)>=1920 and int(field2)<=2002):
                    dummy=0
                    
            elif field1=="iyr":
                if not(len(field2)==4 and int(field2)>=2010 and int(field2)<=2020):
                    dummy=0
            
            elif field1=="eyr":
                if not(len(field2)==4 and int(field2)>=2020 and int(field2)<=2030):
                    dummy=0
    
            elif field1=="hgt":
                unit=field2[-2:]
                if unit!="cm" and unit!="in":
                    dummy=0
                else:
                    height=int(field2[:-2])
                    if unit=="cm":
                        if not(height>=150 and height<=193):
                            dummy=0
                    elif unit=="in":
                        if not(height>=59 and height<=76):
                            dummy=0
            
            elif field1=="hcl":
                allowedlist=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
                colorcode=field2[1:]
                if field2[0]=="#" and len(colorcode)==6:
                    pass
                    for substring in colorcode:
                        if not(substring in allowedlist):
                            dummy=0
                else: 
                    dummy=0
                
            elif field1=="ecl":
                allowedlist=["amb","blu","brn","gry","grn","hzl","oth"]
                if not(field2 in allowedlist):
                    dummy=0

            elif field1=="pid":
                allowedlist=["0","1","2","3","4","5","6","7","8","9"]
                if len(field2)!=9:
                    dummy=0
                else: 
                    for digit in field2:
                        if not(digit in allowedlist):
                            dummy=0

        if dummy==1:
            validcount+=1  
             
print(validcount)
