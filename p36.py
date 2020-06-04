from bokeh.plotting import figure, show, output_file
import json
from collections import Counter

def countMonths():
    months = []
    with open('birthday_dict.json','r') as open_file:
        data = json.load(open_file)

    for x in data.values():
        months.append(x.split("-")[1])

    return Counter(months)

def getKeyList(dict): 
    Key_list = [] 
    for key in dict.keys(): 
        Key_list.append(key) 
          
    return Key_list

def getValueList(dict): 
    Key_list = [] 
    for key in dict.values(): 
        Key_list.append(key) 
          
    return Key_list


output_file("plot.html")
x_categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


month = countMonths()
mon = getKeyList(month)
no_of_frequency = getValueList(month) 

p = figure(x_range=x_categories)
p.vbar(x=mon, top=no_of_frequency, width=0.5)

show(p)