import random

def guess():
   
    MINIMUM = 0
    MAXIMUM = 100
    NUMBER = random.randint(MINIMUM, MAXIMUM)
    # MID = int((MINIMUM + MAXIMUM / 2))
    TRY = 0
    RUNNING = True
    ANSWER = None

    while RUNNING:
        print(f"Is it {NUMBER}?")
        print("""
              If ROBOT guess is Lower than your number type 'lower'.
              If ROBOT guess is equal to your number type 'correct'.
              If ROBOT guess is Higher than your number type 'higher'.
              """)
        
        ANSWER = input("> ")
        
        
        if "lower" in ANSWER.lower() :
            NUMBER += random.randint(1, 4)
            
        
        elif "higher" in ANSWER.lower() :
            NUMBER -= random.randint(1, 4)
        
        elif "correct" in ANSWER.lower() :
            print("Correct Guess")
            print(f"ROBOT guess the your Number in {TRY} tries.")
            RUNNING = False
        
        TRY += 1 
        
        
        # if "lower" not in ANSWER.lower() and "higher" not in ANSWER.lower() and "correct" not in ANSWER.lower():
        #     print("Please Select valid Option")
        
        # elif "higher" in ANSWER.lower() :
        #     MINIMUM = 0
        #     MAXIMUM = MID - 1 
        #     MID = int((MINIMUM + MAXIMUM / 2))
        
        # elif "lower" in ANSWER.lower() :
        #     MAXIMUM = 100
        #     MINIMUM = MID + 1
        #     # print(MINIMUM)
        #     MID = int((MAXIMUM + MINIMUM / 2))
        
        # elif "correct" in ANSWER.lower() :
        #     print("Correct Guess")
        #     print(f"ROBOT guess the your Number in {TRY} tries.")
        #     RUNNING = False
        
        # TRY += 1 
        
    
print("YOUR GAME STARTS NOW !")
if __name__ == "__main__":
    print("Guess One number Between 0 to 99 :> ")
    guess()