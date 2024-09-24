print('Welcome to Grocery List Manager!')
choice = 0
itemList = []
while choice != 4:
    print('Choose an option:')
    print('[1] Add an item')
    print('[2] View the list')
    print('[3] Remove an item')
    print('[4] Exit')
    choice = int(input('Enter your choice: '))
    match choice:
        case 1:
            itemList.append(input('Enter an item to add: '))
            print(f'item {itemList[-1]} added to the grocery list')
        case 2:
            print(f'{itemList}')
        case 3:
            itemRemove = input('Enter an item to remove: ')
            itemList.remove(itemRemove)
            print(f'Item {itemRemove} has been removed')
        case 4:
            break
print('Bye bye')


