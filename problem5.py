str = input("\nInput a string : ")
no_of_digits=no_of_alphabets=0
for char in str:
    if char.isdigit():
        no_of_digits += 1
    elif char.isalpha():
        no_of_alphabets += 1
    else:
        pass
    
print("-" * 70)    
print(f"\nThere are {no_of_alphabets} LETTERS and {no_of_digits} DIGITS.\n")
print("-" * 70)