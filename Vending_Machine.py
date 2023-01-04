#Utility App
'''Your task is to create a Vending Machine program using the Python programming language. 
The program should demonstrate your knowledge of programming and make use of the techniques 
introduced over the course of the module.'''

import random

#Printing art & text
title = '''
    ___       __                   _ _       
   / __\__ _ / _| ___  /\   /\___ (_) | __ _ 
  / /  / _` | |_ / _ \ \ \ / / _ \| | |/ _` |
 / /__| (_| |  _|  __/  \ V / (_) | | | (_| |
 \____/\__,_|_|  \___|   \_/ \___/|_|_|\__,_|'''
vending_machine = ''' ____________________________________________
|############################################|
|#|                           |##############|
|#|  =====  ..--''`  |~~``|   |##|````````|##|
|#|  |   |  \     |  :    |   |##| Exact  |##|
|#|  |___|   /___ |  | ___|   |##| Change |##|
|#|  /=__\  ./.__\   |/,__\   |##| Only   |##|
|#|  \__//   \__//    \__//   |##|________|##|
|#|===========================|##############|
|#|```````````````````````````|##############|
|#| =.._      +++     //////  |##############|
|#| \/  \     | |     \    \  |#|`````````|##|
|#|  \___\    |_|     /___ /  |#| _______ |##|
|#|  / __\\\\  /|_|\   // __\   |#| |1|2|3| |##|
|#|  \__//-  \|_//   -\__//   |#| |4|5|6| |##|
|#|===========================|#| |7|8|9| |##|
|#|```````````````````````````|#| ``````` |##|
|#| ..--    ______   .--._.   |#|[=======]|##|
|#| \   \   |    |   |    |   |#|  _   _  |##|
|#|  \___\  : ___:   | ___|   |#| ||| ( ) |##|
|#|  / __\  |/ __\   // __\   |#| |||  `  |##|
|#|  \__//   \__//  /_\__//   |#|  ~      |##|
|#|===========================|#|_________|##|
|#|```````````````````````````|##############|
|############################################|
|#|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|####|`````|###|
|#|__________|PUSH|___________|####|\|||/|###|
|############################################|
 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\///////////////////////
 |_________________________________________|'''
menu = '''

\t  ))                          ((
\t |~~|  Drinks & Snacks Menu  |~~|
\tC|__|                        |__|]\n\n'''
dash1 = '''--------------------- *:･ﾟ✧ *:･ﾟ------------------------'''

thankyou = '''\n   ;)( ;                ___       _            _   _ 
  :----:     o8Oo./    | __|_ _  (_)___ _  _  | | | |
 C|====| ._o8o8o8Oo_.  | _|| ' \ | / _ \ || | |_| |_|
  |    |  \========/   |___|_||_|/ \___/\_, | (_) (_)
  `----'   `------\'            |__/     |__/ \n'''
code = '''\n  ___                _      ___         _         _    _ 
 |_ _|_ _  _ __ _  _| |_   / __|___  __| |___    ( `\/'*)
  | || ' \| '_ \ || |  _| | (__/ _ \/ _` / -_)    \   */' 
 |___|_||_| .__/\_,_|\__|  \___\___/\__,_\___|     `\/'  
          |_|                                 '''
payment = '''\n  ___                         _       _    _
 | _ \__ _ _  _ _ __  ___ _ _| |_    ( `\/'*)
 |  _/ _` | || | '  \/ -_) ' \  _|    \   */' 
 |_| \__,_|\_, |_|_|_\___|_||_\__|     `\/' 
           |__/                   \n'''
itemst = '''\n  ___ _                     _    _
 |_ _| |_ ___ _ __  ___    ( `\/'*)
  | ||  _/ -_) '  \(_-<     \   */'
 |___|\__\___|_|_|_/__/      `\/' 
                       \n'''

#The list of items that are available [Dictionary]
items_available = [
    { "code":0, "name":"Caffe Latte", 'price':20,}, {"code": 1, "name":"Frappe", 'price':23,}, 
    {"code": 2, "name":"Cappuccino", 'price':20,}, {"code": 3, "name":"Double Espresso",'price':23,}, 
    {"code": 4, "name":"Macha Latte", 'price':15,}, {"code": 5, "name":"Strawberry & Cream",'price':15,}, 
    {"code": 6, "name":"Breakfast Sandwich", 'price':15,}, {"code": 7, "name":"Croissant", 'price':9,}, 
    {"code": 8, "name":"Macarons", 'price':10,}, {"code": 9, "name":"Cupcake", 'price':7,} ]

sug_items = [
    {"code":0, "name":"Waffle meal", 'price':10},{"code":1, "name":"Biscuit", 'price':6},{"code":2, "name":"Sweet Bread", 'price':5},
    {"code":3, "name":"Con Leche Muffins", 'price':6}, {"code":4,"name":"Apple Pie", 'price':4}]

#For machine, total, create_receipt functions
items = []
receipt = """
\t******** RECEIPT *******\n
\t  PRODUCT --> PRICE
"""
total = 0
run = True

#For adding all the prices together
def total(items):
    total = 0

    for i in items:
        total += i["price"]

    return total
#For printing of receipt
def create_receipt(items, receipt):
   #For receipt
    for i in items:
        receipt += f"""
            {i["name"]} --- {i['price']}
        """
   #For total receipt
    receipt += f"""
          Total ==== {total(items)} """
    return receipt

#THE START OF THE MAIN CODE
def start():
#Name of the Vending Machine
    print(title)
#Vending Machine Art
    print(vending_machine)
   #Introduction to Vending machine
    print('\n\t   Welcome to Cafe Voila <3')
    print('\t A cafe in a vending machine \n')
    print('Everything you can buy at a cafe is now in a machine!')
   #No specific currency ex. dollars
    print("\tThe coffee can get a bit pricy :)\n")
   #Printing of Menu Title
    print(dash1 + menu)
   #Printing of Menu using a for loop
    for i in items_available:
        print(f"[{i['code']}] Items: {i['name']} - Price: {i['price']}\n")
    print(dash1+code)
start()

#Fuction used for adding drinks or snacks to the users items. USing while loop 
def machine(items_available, run, items):
    while run:
       #Enter the item code here
        buy_item = int(input("\nYou may enter the product number code of your choice: "))
        if buy_item < len(items_available):
           #To add to the empty list
            items.append(items_available[buy_item])
            print('Okay, {} sounds perfect! That will be added to your bill.'.format(items_available[buy_item]['name']))
        else:
            print("\nTHE PRODUCT CODE IS WRONG! PLEASE PUT THE RIGHT CODE\n")
       #If user wants to add more or end it
        added_items = str(input("Enter c to add more items or Enter x to quit: "))
       #If user enters x you will got to the next part
        if added_items == "x":
            run = False  
   #Enter y or n 
    sugg = str(input('\nWould you like a suggestion for more items? y\\n '))
   #If y is entered it will show this output
    if sugg == 'y':
       #random.choice will randomize a product as a suggestion 
        print(dash1 + "\n\n{}\n\n".format(random.choice(sug_items)) + dash1)
       #Ask the user if theyre interested in purchasing
        added = str(input('Would like to purchase it? y\\n '))
       #If user enters y it will print this
        if added == 'y':
            buy_sugg = int(input('\nYou may enter the product number code of your choice: '))
            if buy_sugg < len(sug_items):
                items.append(sug_items[buy_sugg])
               #Will show the product name 
                print('Okay, {} sounds perfect! That will be added to your bill.'.format(sug_items[buy_sugg]['name']))
            else:
                print("\nTHE PRODUCT CODE IS WRONG! PLEASE PUT THE RIGHT CODE\n")
       #If user enters n you will got to the next part
        if added == 'n':
                print('ok lets continue on with your purchase\n')
   #If user enters n you will got to the next part
    if sugg == 'n':
        print("ok lets continue on with your purchase\n")
    else:
        run = False 

   #to show total price to the user
    print(dash1 + payment)
   #print(payment)
    print(f'The total price is {total(items)}')
   #Input total price or more here
    cash = int(input(("Please enter the amount of money needed: ")))
   #For cash change
    change = int(cash) - int(total(items))
   #If the user gives the exact amount needed it will print this
    if cash == total(items):
        print(dash1 + itemst)
        print('All of the items that you have pruchased will be dispensed.\n' + thankyou)
   #If the user gives more than the exact amount needed it will print this
    elif cash >= total(items):
        print(dash1 + itemst)
        #print(itemst)
        print('All of the items that you have pruchased will be dispensed.')
        print(f'Here is your change: {change} \n' + thankyou)
   #If the user gives less than the right amount 
    else:
        print('Please enter the right amount of money')
        return
   #For printing of receipt and total price of your purchase
    input("Enter to get receipt \n" + dash1)
    print(create_receipt(items, receipt))
    print(f'         Cash ---- {cash}')
    print(f'         Change ---- {change}')
    print('\n\t******** THANK YOU *******\n' + dash1)
   #Will print receipt and enjoy card

#Main for function call. It Executes Code When the File Runs as a Script.
if __name__ == "__main__":
    machine(items_available, run, items)