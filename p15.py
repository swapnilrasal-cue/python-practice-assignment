def reverseWordsOfString(user_input):
    list_of_words = list(reversed(user_input.split()))
    reversed_string = " ".join(list_of_words)
    print(reversed_string)
        

user_input = input("Enter a String")
reverseWordsOfString(user_input)