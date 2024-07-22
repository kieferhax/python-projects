def get_item(x):
    if x == 1:
        return 'Cheeseburger'
    elif x == 2:
        return 'French Fry'
    elif x == 3:
        return 'Milk Shake'
    elif x == 4:
        return 'Soda'
    else:
        return 'Invalid Option'

def welcome():
    print('Welcome! Here are our menu items: ')
    print('Cheeseburger')
    print('French Fry')
    print('Milk Shake')
    print('Soda')

welcome()

option = int(input('What would you like to order today? '))
print(get_item(option))