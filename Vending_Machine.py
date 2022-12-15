#Utility App
'''Your task is to create a Vending Machine program using the Python programming language. 
The program should demonstrate your knowledge of programming and make use of the techniques 
introduced over the course of the module.'''

def start():
#Name of the Vending Machine
    print('''
                _             ___      _   
    /\/\   ___ | | ____ _    / _ \___ | |_ 
   /    \ / _ \| |/ / _` |  / /_)/ _ \| __|
  / /\/\ \ (_) |   < (_| | / ___/ (_) | |_ 
  \/    \/\___/|_|\_\__,_| \/    \___/ \__|''')

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
    print('\t    Welcome to Moka Pot <3')
    print('\t A cafe in a vending machine \n')
    print('Everything you can buy at a cafe is now in a machine!')

start()

def main():
#A list of drinks that are available
    drinks_available = [
        {
            'name':'Caffe Latte',
            'price':20,
            'code':'A1'
        },
        {
            'name':'Frappe',
            'price':23,
            'code':'A2'
        },
        {
            'name':'Cappuccino',
            'price':20,
            'code':'A3'
        },
        {
            'name':'Double Espresso',
            'price':23,
            'code':'A4'
        },
        {
            'name':'Macha Latte',
            'price':15,
            'code':'A5'
        },
        {
            'name':'Strawberry & Cream',
            'price':15,
            'code':'A6'
        }
    ]
#A list of snacks that are available
    snacks_available = [
        {
            'name':'Breakfast Sandwich',
            'price':15,
            'code':'B1'
        },
        {
            'name':'Croissant',
            'price':9,
            'code':'B2'
        },
        {
            'name':'Macarons (4 pieces)',
            'price':15,
            'code':'B3'
        },
        {
            'name':'Cupcake',
            'price':7,
            'code':'B4'
        }
    ]

    item = []

    print('''\n\t      ))                 ((
\t     |~~|  Drinks Menu  |~~|
\t    C|__|               |__|]\n''')  
    print('-----------------------------------------------------')
    for i in drinks_available:
        print(f"Drink: {i['name']} - Price: {i['price']} - Code: {i['code']}")
        print()
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
            
        

main()