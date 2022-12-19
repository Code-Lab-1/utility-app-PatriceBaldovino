my_dict = {'id': 1, 'name': 'bobbyhadz','title':'yuh', 'age': 30}
titles = {'name':'BOB'}
result = '\n'.join(f'{key}: {value}' for key, value in my_dict.items())

# id: 1
# name: bobbyhadz
# age: 30
for i in my_dict:
    print(f"{my_dict['name']}")
    print(result)
    print()
    