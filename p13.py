import random

def getFebonacciSerires(n):
    i = 1
    j = 1
    if n == 0:
        fibonaci_series = []
    elif n == 1 :
        fibonaci_series = [1]
    elif n == 2 :
        fibonaci_series = [1,1]
    elif n > 2:
        fibonaci_series = [1,1]                         
        for x in range(2, n):
            k = i + j
            fibonaci_series.append(k)
            i = j
            j = k
    print(fibonaci_series)
        
try:    
    user_input = int(input("Enter Number upto you want to print febonacci series :")) 
except:
    print("Please Enter Number Only")
    
getFebonacciSerires(user_input)