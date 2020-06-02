import re

def validatePasswords(passwords_list):
    valid_passwords = []
    pattern = re.compile("^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$")
    print('\n','-' * 70)

    for password in passwords_list:
        result = pattern.findall(password)
        if result :
            valid_passwords.append(password)
        
    print("\nValid Passwords Are :",valid_passwords)
    print('\n','-' * 70)
        
passwords_list = [x for x in input('\nEnter the PASSWORDS to Validate :').split(',') if 6 < len(x) < 12]
validatePasswords(passwords_list)