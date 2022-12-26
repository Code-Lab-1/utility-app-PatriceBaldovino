#Utility App
'''Your task is to create a Vending Machine program using the Python programming language. 
The program should demonstrate your knowledge of programming and make use of the techniques 
introduced over the course of the module.'''

def start():
#Name of the Vending Machine
    print('''
    ___       __                   _ _       
   / __\__ _ / _| ___  /\   /\___ (_) | __ _ 
  / /  / _` | |_ / _ \ \ \ / / _ \| | |/ _` |
 / /__| (_| |  _|  __/  \ V / (_) | | | (_| |
 \____/\__,_|_|  \___|   \_/ \___/|_|_|\__,_|''')

#Vending Machine Art
    print(''' ____________________________________________
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
 |_________________________________________|''')
    print()
    #Introduction to Vending machine
    print('\t   Welcome to Cafe Voila <3')
    print('\t A cafe in a vending machine \n')
    print('Everything you can buy at a cafe is now in a machine!')

    print("\tThe coffee can get a bit pricy :)")
start()

#A list of items that are available
items_available = [
    {
        "code":0,
        "name":"Caffe Latte",
        'price':20,
    },
    {
        "code": 1,
        "name":"Frappe",
        'price':23,
    },
    {
        "code": 2,
        "name":"Cappuccino",
        'price':20,
    },
    {
        "code": 3,
        "name":"Double Espresso",
        'price':23,
    },
    {
        "code": 4,
        "name":"Macha Latte",
        'price':15,
    },
    {
        "code": 5,
        "name":"Strawberry & Cream",
        'price':15,
    },
    {
        "code": 6,
        "name":"Breakfast Sandwich",
        'price':15,
    },
    {
        "code": 7,
        "name":"Croissant",
        'price':9,
    },
    {
        "code": 8,
        "name":"Macarons (4 pieces)",
        'price':15,
    },
    {
        "code": 9,
        "name":"Cupcake",
        'price':7,
    }
]

#Variables for the Vending machine
items = []
reciept = """
-----------------------------------------------------\n
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
def create_reciept(items, reciept):

    for i in items:
        reciept += f"""
            {i["name"]} --- {i['price']}
        """

    reciept += f"""
        Total ---- {total(items)}
        """
    return reciept

#Printing of Menu Title
print('''
\t  ))                          ((
\t |~~|  Drinks & Snacks Menu  |~~|
\tC|__|                        |__|]\n''')  

print('-----------------------------------------------------')
#Printing of Menu using a for loop
for i in items_available:
        print(f"Items: {i['name']} - Price: {i['price']} ====== Code: {i['code']}")
        print()
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

#Fuction used for adding drinks or snacks to the users items
def machine(items_available, run, items):
    while run:
        #Enter the item code here
        buy_item = int(input("\nYou may enter the product code of your choice: "))
        if buy_item < len(items_available):
            items.append(items_available[buy_item])
        else:
            print("\n\tTHE PRODUCT CODE IS WRONG! PLEASE PUT THE RIGHT CODE")
        #If user wants to add more or end it
        added_items = str(input("Enter c to add more items or Enter x to quit: "))
        #If user enters x you will get your receipt
        if added_items == "x":
            run = False
    #For printing of receipt and total price of your purchase
    record = int(input(("To print receipt please enter the number 1: ")))
    #Will print receipt and enjoy card
    if record == 1:
        print('-----------------------------------------------------')
        print(create_reciept(items, reciept))
        print('-----------------------------------------------------')
        print('''
   ;)( ;                ___       _            _   _ 
  :----:     o8Oo./    | __|_ _  (_)___ _  _  | | | |
 C|====| ._o8o8o8Oo_.  | _|| ' \ | / _ \ || | |_| |_|
  |    |  \========/   |___|_||_|/ \___/\_, | (_) (_)
  `----'   `------\'            |__/     |__/ \n''')
    #If 1 is not entered it will be invalid
    else:
        print("\n\t     INVALID ENTRY")
        print('\tPlease follow instructions!')
#Main for function call
if __name__ == "__main__":
    machine(items_available, run, items)
