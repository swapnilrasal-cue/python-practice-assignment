# validatedPasswords = []
# num = [x for x in input('\nEnter the PASSWORDS to Validate :').split(',')]
# print('-' * 70)
# print("\nPASSWORDS Are : " ,num ,'\n')

# def checkLength(x):
#     if  6 < len(x) < 12:
#         if 
#         validatedPasswords.append(x)
#         print(validatedPasswords)
        
        

# for x in num:
#     checkLength(x)
    
import re

validatedPasswords = []
num = [x for x in input('\nEnter the PASSWORDS to Validate :').split(',')]
print('-' * 70)
print("\nPASSWORDS Are : " ,num ,'\n')
for p in num:
    x = True
    while x:
        if (len(p)<6 or len(p)>12):
            break
        elif not re.search("[a-z]",p):
            break
        elif not re.search("[0-9]",p):
            break
        elif not re.search("[A-Z]",p):
            break
        elif not re.search("[$#@]",p):
            break
        elif re.search("\s",p):
            break
        else:
            # print(p ,end=',')
            validatedPasswords.append(p)
            x=False
            break
print('-' * 70)
print("\nValid Passwords : ",validatedPasswords,'\n')
print('-' * 70)
if x:
    print("Not a Valid Password")    