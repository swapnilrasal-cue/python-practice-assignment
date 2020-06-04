user_input = str(input("enter a word :"))
reverse_string = user_input[::-1]

if user_input == reverse_string:
    print("Palindrome")
else:
    print("Not Palindrome")
