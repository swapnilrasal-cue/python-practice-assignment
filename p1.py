import datetime
import sys
def calculate(age,n):
    now = datetime.datetime.now()
    years = (now.year - age) + 100
    print(f"\n In years {years} you will become 100 years old" * n)

try:    
    name = input("\nEnter your name :")
    age = int(input("\nEnter your age :"))
    no_of_copies = int(input("\nEnter number of copies you want to get :"))
except:
    print("Enter Valid Details")
    sys.exit(1)

calculate(age,no_of_copies)