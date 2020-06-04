import json

def enterBirthdate(user_input):
    with open('birthday_dict.json','r') as open_file:
        data = json.load(open_file)
        birthday_dict = data
        print(birthday_dict)

    if user_input == 'n':
        print("Goodbye")
    
    elif user_input == 'y':
        name = input("Enter Name : ")
        birth_date = input("Enter Name : ")
        birthday_dict[name]=birth_date
        with open("birthday_dict.json", "w") as f:
            json.dump(birthday_dict, f)
            print("saved successfully")
            print(birthday_dict)
    
if __name__ == "__main__":
    user_input = input("Do you want to Enter New Birthday Record Press y to enter and n to exit : ")
    enterBirthdate(user_input)
