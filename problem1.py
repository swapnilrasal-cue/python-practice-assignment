import math

class Formula():
    
    def __init__(self):
        self.C = 50
        self.H = 30
        
    def Calculate(self,D):
        # print(D)
        li = []
        Q = ((2 * self.C * D)/self.H)
        answer = round(math.sqrt(Q))        
        print(answer,end=',')
                
a = Formula()

str = str(input("Enter comma separated integers: "))
list = str.split (",")

for i in list:
    b = int(i)
    a.Calculate(b)    

