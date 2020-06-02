import sys

def divisibleBy7(n):
    divBy7 = [i for i in range(0, n) if (i % 7 == 0)]
    print('-' * 70)
    print('\nThe Numbers Divisible By 7 Are : -\n')
    print(divBy7, '\n')
    print('-' * 70)

try :    
    user_input = int(input("\nEnter the Number upto you want to Check :"))
except ValueError:
    print("\nPlease Enter Number Only.")
    sys.exit(1)
    
divisibleBy7(user_input)