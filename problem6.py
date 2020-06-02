def countUpperAndLower(user_input):
    no_of_uppercase_leters=no_of_lowercase_leters=0
    for c in user_input:
        if c.isupper():
            no_of_uppercase_leters += 1
        elif c.islower():
            no_of_lowercase_leters += 1
        else:
            pass    
    
    print("-" * 70)    
    print(f"\nThere are {no_of_uppercase_leters} UPPERCASE LETTERS and {no_of_lowercase_leters} LOWERCASE LETTERS.\n")
    print("-" * 70)
    
user_input = input("\nInput a string : ")
countUpperAndLower(user_input)