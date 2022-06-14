# cardspublickey=5764801
# doorspublickey=17807724

cardspublickey=5290733
doorspublickey=15231938

subject_number=7
other_number=20201227


def formula(a,b,n): # solves f(f(f(x)))  solve recursive f(f(f(x))) n times. f(x)=a % b
    return ((a ** n) % ((a ** (n - 1))*b)) % b

# cardloop=1
# while True:
#     value=formula(subject_number,other_number,cardloop)
#     if value == cardspublickey:
#         break
#     print(cardloop)
#     cardloop+=1
    
doorloop=1
while True:
    value=formula(subject_number,other_number,doorloop)
    if value == doorspublickey:
        break
    print(doorloop)
    doorloop+=1
print(doorloop)


# cardloop=0
# value=1
# while value!=cardspublickey:
#     value=1
#     print(cardloop)
#     cardloop+=1
#     for i in range(cardloop):
#         value*=7
#         value%=20201227
# print(cardloop)

# doorloop=0
# value=1
# while value!=doorspublickey:
#     value=1
#     doorloop+=1
#     for i in range(doorloop):
#         value*=7
#         value%=20201227
# print(doorloop)

# if cardloop<=doorloop:
#     encrypkey=1
#     for i in range(cardloop):
#         encrypkey*=doorspublickey
#         encrypkey%=20201227
# else:
#     encrypkey=1
#     for i in range(doorloop):
#         encrypkey*=cardspublickey
#         encrypkey%=20201227
# print(encrypkey)