import random
import sys

random_number = random.randint(1,9)
# print(random_number)
count = 0
x = True
while x:
    user_input = input("Guess one number between 1 to 9 including 1 and 9 if you want to exit then type exit : ")        
    if user_input == 'exit':
        print("Good bye ..")
        sys.exit(1)
    
    user_input = int(user_input)
    count += 1
    
    if user_input == random_number:
        print("Exactly right")
        print(f"you have guess the number in {count} times")
    elif user_input > random_number:
        print("too high guess")
    elif user_input < random_number:
        print("too low guess")


