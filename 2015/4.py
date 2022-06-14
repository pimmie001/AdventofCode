import hashlib as hl

string="iwrupvqb"     #puzzle input

i=1
while True:
    str2=str(i)
    fullstring=string+str2

    result=hl.md5(fullstring.encode()).hexdigest()
    first5=result[:5]

    if first5=="00000": 
        print("the answer is:",i)
        break
    
    i+=1
# 346386


### part 2 (almost identical)

import hashlib as hl

string="iwrupvqb"     #puzzle input

i=1
while True:
    str2=str(i)
    fullstring=string+str2

    result=hl.md5(fullstring.encode()).hexdigest()
    first6=result[:6]

    if first6=="000000": 
        print("the answer is:",i)
        break
    
    i+=1
# 9958218