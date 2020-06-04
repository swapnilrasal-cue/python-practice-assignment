birthday_dict = {"swapnil rasal" : "31-01-1997",
                 "bhanu rasal" : "15-02-1964",
                 "prajakta nandavadekar" : "27-01-1997"
                 }

def findBirthdate(user_input):
    print(f"{user_input}'s birthday is on ",birthday_dict[user_input])

print("Welcome to the birthday dictionary. We know the birthdays of : ")

for birthday in birthday_dict:
    print(birthday,"\n")

user_input = input("Who's birthday do you want to look up? ")
findBirthdate(user_input)
