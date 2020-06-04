def checkPrime(n):
    if n > 2:
        c = [x for x in range(2,n) if n % x == 0]
        if len(c) == 0:
            print("prime number")
        else:
            print("Not a prime number")
    else:
        print("Not a prime number")

try:
    user_input = int(input("Enter Number : "))

except:
    print("Enter number only")
    
checkPrime(user_input)