import random
 
a = {"name":"Waffle meal", 'price':10}
b = {"name":"Biscuit", 'price':6}
c = {"name":"Sweet Bread", 'price':5}
d = {"name":"Con Leche Muffins", 'price':6} 
e = {"name":"Apple Pie", 'price':4}

sug_items = [a,b,c,d,e]

sugg = str(input('Would you like a suggestion for more items? y\\n '))
if sugg == 'y':
    print("Items: {0} " .format(random.choice(sug_items)))
if sugg == 'n':
    print("ok lets continue on with your purchase")