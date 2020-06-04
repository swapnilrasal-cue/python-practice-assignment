import sys

def checkDivisor(number):
    divisors = []
    for i in range(1,number+1):
        if number % i == 0:
            divisors.append(i)
    print(divisors)

try:
    number = int(input("Enter Number : "))
    checkDivisor(number)
except:
    print("\nPlease Enter Number Only")
    sys.exit(1)