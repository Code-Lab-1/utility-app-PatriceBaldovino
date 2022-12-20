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
    print('\t   Welcome to Cafe Voila <3')
    print('\t A cafe in a vending machine \n')
    print('Everything you can buy at a cafe is now in a machine!')

start()

#A list of drinks that are available
drinks_available = [
    {
        "item_id":0,
        "name":"Caffe Latte",
        'price':2,
    },
    {
        "item_id": 1,
        "name":"Frappe",
        'price':23,
    },
    {
        "item_id": 2,
        "name":"Cappuccino",
        'price':20,
    },
    {
        "item_id": 3,
        "name":"Double Espresso",
        'price':23,
    },
    {
        "item_id": 4,
        "name":"Macha Latte",
        'price':15,
    },
    {
        "item_id": 5,
        "name":"Strawberry & Cream",
        'price':15,
    },
    {
        "item_id": 6,
        "name":"Breakfast Sandwich",
        'price':15,
    },
    {
        "item_id": 7,
        "name":"Croissant",
        'price':9,
    },
    {
        "item_id": 8,
        "name":"Macarons (4 pieces)",
        'price':15,
    },
    {
        "item_id": 9,
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
sum = 0
run = True

#Printing of Drinks Menu
print('''
\t      ))                          ((
\t     |~~|  Drinks & Snacks Menu  |~~|
\t    C|__|                        |__|]\n''')  
print('-----------------------------------------------------')
for i in drinks_available:
        print(f"Items: {i['name']} - Price: {i['price']} - Code: {i['item_id']}")
        print()
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

#Fuction used for adding drinks or snacks to the users items
def machine(drinks_available, run, items):
    while run:
        #Enter the item code here
        buy_item = int(input("\nEnter the item code of the product you want to buy: "))

        #
        if buy_item < len(drinks_available,):
            items.append(drinks_available[buy_item])
        else:
            print("THE PRODUCT ID IS WRONG!")

        more_items = str(input("Enter c to add more items or Enter x to quit: "))

        if more_items == "x":
            run = False
    
    rec_bool = int(input(("1 - print the reciept 2 - only print the total sum .. ")))
    if rec_bool == 1:
        print(create_reciept(items, reciept))
    elif rec_bool == 2:
        print(sum(items))
    else:
        print("INVALID ENTRY")

def sum(items):
    sum = 0

    for i in items:
        sum += i["price"]

    return sum

def create_reciept(items, reciept):

    for i in items:
        reciept += f"""
            {i["name"]} --- {i['price']}
        """

    reciept += f"""
        Total ---- {sum(items)}
        """
    return reciept

if __name__ == "__main__":
    machine(drinks_available, run, items)