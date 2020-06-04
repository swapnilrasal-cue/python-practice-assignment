import sys
try:
    number = int(input("Enter Number : "))
    check = int(input("Enter Number to divide by: "))

except:
    print("\nPlease Enter Number Only")
    sys.exit(1)
        
if number % 4 == 0:
    print(number,"is multiple of 4")

if number % 2 == 0:
    print(number, " is Even Number")
else:
    print(number," is Odd Number")
    
    
if number % check == 0:
    print(number,"is divisible by ",check)

else:
    print(number,"is NOT divisible by ",check)