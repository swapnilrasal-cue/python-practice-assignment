number1 = input("Enter number 1 : ")
number2 = input("Enter number 2 : ")
number3 = input("Enter number 3 : ")

def findMax(a,b,c):
    if a > b and a > c:
        print(a,"is greater ")
    elif b > a and b > c:
        print(b,"is greater")
    elif c > a and c > b:
        print(c,"is greater")

findMax(number1,number2,number3)