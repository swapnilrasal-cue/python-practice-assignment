import random

def gameCowAndBull(user_input,number):
    cows = 0
    bulls = 0
    for i in range(len(number)):
        if number[i] == user_input[i]:
            cows += 1
        else:
            bulls += 1
             
    print(f"number of cows are : {cows} and bulls are {bulls}")
    return cows    
        
number = str(random.randint(1111,9999))
print(number)
no_of_guess = 0

x = True
while x:
    user_input = input("Guess a four digit number between 1111 to 9999 : ")
    print(user_input)

    if user_input == 'exit':
        break
    
    elif len(user_input) < 4 or len(user_input) > 4:
        print("Number should not be less than or greater than 4 digit ")
        break 
    
    cow_bull_count = gameCowAndBull(user_input,number)
    no_of_guess = no_of_guess + 1
    print(no_of_guess)
    
    if cow_bull_count == 4:
        x = False
        print(f"You win the game after {no_of_guess} guess ! The number was {number}")
        break 
    else:
        print("Your guess isn't quite right, try again.")        
        

