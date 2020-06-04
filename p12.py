import random

def getFirstAndLast(a):
    res = a[::len(a)-1]
    print(res)
    
a = random.sample(range(100),5) 
print(a)
getFirstAndLast(a)