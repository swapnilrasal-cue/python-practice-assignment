def countNumAndDigits(user_input):
    no_of_digits = no_of_alphabets = 0
    for c in user_input:
        if c.isdigit():
            no_of_digits += 1
        elif c.isalpha():
            no_of_alphabets += 1
        else:
            pass
    
    print("-" * 70)    
    print(f"\nThere are {no_of_alphabets} LETTERS and {no_of_digits} DIGITS.\n")
    print("-" * 70)
    
user_input = input("\nInput a string : ")
countNumAndDigits(user_input)
