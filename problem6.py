str = input("\nInput a string : ")
no_of_uppercase_leters=no_of_lowercase_leters=0
for char in str:
    if char.isupper():
        no_of_uppercase_leters += 1
    elif char.islower():
        no_of_lowercase_leters += 1
    else:
        pass
    
print("-" * 70)    
print(f"\nThere are {no_of_uppercase_leters} UPPERCASE LETTERS and {no_of_lowercase_leters} LOWERCASE LETTERS.\n")
print("-" * 70)