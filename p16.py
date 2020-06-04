import string
import random

def generatePassword(type_of_password):
    if type_of_password == 'weak':
        print("weak password")
        size = 6  
        chars = string.ascii_letters + string.digits 
        return ''.join(random.choice(chars) for _ in range(size))
    elif type_of_password == 'strong':
        print("strong password")
        size = 12  
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation 
        return ''.join(random.choice(chars) for _ in range(size))

    else:
        print("invalid choice")
        
user_input = input("Which type of password you want to generate ? weak or strong ? :")
print(generatePassword(user_input))