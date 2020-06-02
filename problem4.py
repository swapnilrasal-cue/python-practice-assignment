import sys

def numDivBy5(user_input):
    items = []
    try:
        for binaryNumber in user_input:
            x = int(binaryNumber, 2)
            if not x%5:
                items.append(binaryNumber)
    except:
        print("\nPlease Enter Binay Numbers Only .\n")
        sys.exit(1)
    
    print("\nNumbers Divisible by 5 :",','.join(items),'\n','-' * 50)

user_input = [x for x in input('\nEnter the Binary Numbers Separated By comma :').split(',')]
numDivBy5(user_input)