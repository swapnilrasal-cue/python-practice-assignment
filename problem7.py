import re

def validatePasswords(passwords_list):
    valid_passwords = []
    invalid_passwords = []
    pattern = "^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    print('\n','-' * 70)

    for password in passwords_list:
        result = re.findall(pattern, password)
        if result and len(password) <= 12:
            valid_passwords.append(password)
        else:
            invalid_passwords.append(password)
        
    print("\nValid Passwords Are :",valid_passwords)
    print("\nInValid Passwords Are :",invalid_passwords)
    print('\n','-' * 70)
        
passwords_list = [x for x in input('\nEnter the PASSWORDS to Validate :').split(',')]
validatePasswords(passwords_list)