import sys
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

user_input = str(input("Enter comma separated integers: "))
list_inputs = user_input.split (",")
try:
 
    for i in list_inputs:
        b = int(i)
        a.Calculate(b)        
except:
    print("Please Enter Integers Only")
    sys.exit(1)

else:
    print("Successfully Completed")

