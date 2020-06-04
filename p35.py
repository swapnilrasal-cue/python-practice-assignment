import json
from collections import Counter

def countMonts():
    months = []
    with open('birthday_dict.json','r') as open_file:
        data = json.load(open_file)

    for x in data.values():
        months.append(x.split("-")[1])
   
    print(Counter(months))

if __name__ == "__main__":
    countMonts()