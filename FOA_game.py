#The Fruit Ordering App
#Here we will create a fruit ordering app implementing functions, modules, conditional loops, lists, arguments, parameters, return values, classes, instances, methods, __init__ method and more
from fruit_utils import Fruitmenu
from food_utils import Food
from drink_utils import Drink

fruit1 = Fruitmenu('Apple',3)
# fruit1.name = 'Apple'
# fruit1.price = 3
#__init__ method will make the 2 lines of code above redundant
# print(fruit1.info())
#by creating a list containing each fruit, we can intirate through the list to print(fruit1.info()) for each fruit thereby making the code above redundant

fruit2 = Fruitmenu('Orange',4)
# fruit2.name = 'Orange'
# fruit2.price = 4
# print(fruit2.info())

fruit3 = Fruitmenu('Avocado',5)
# fruit3.name = 'Avocado'
# fruit3.price = 5
# print(fruit3.info())

fruit4 = Fruitmenu('Watermelon',6)
# fruit4.name = 'Watermelon'
# fruit4.price = 6
# print(fruit4.info())

fruits = [fruit1,fruit2,fruit3,fruit4]
index = 0
print('Fruits')
for fruit in fruits:
    print(str(index) + '. ' + fruit.info())
    index += 1
print('.................')



food1 = Food('Amala',2,330)
food2 = Food('Custard',3,150)
food3 = Food('Yam',4,500)
foods = [food1,food2,food3]
index = 0
print('Food')
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1
print('.................')


drink1 = Drink('Fanta',9,20)
drink2 = Drink('Coke',8,25)
drink3 = Drink('Sprite',7,30)
drinks = [drink1,drink2,drink3]
print('Drink')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1
print('.................')






order = int(input('Enter your fruit menu item number: '))
# if order<0 or order>3:
#     return False
# else:
#     return True 
selected_fruit_menu = fruits[order]
print(f'Your selected fruit menu: {selected_fruit_menu.name}')
print('...............')

order =int(input('Enter your food order number: '))
selected_food = foods[order]
print(f'Your selected food is: {selected_food.name}')
print('...............')

order = int(input('Enter your drink order number: '))
selected_drink = drinks[order]
print(f'Your selected drink is: {selected_drink.name}')
print('...............')

count = int(input(f'How many packs do you want?\n(15% off(on each item)\n for 3 or more packs): '))
print('...............')

# result = selected_menu.price*count
print(f'You have bought {count} packs of {selected_fruit_menu.name}, {selected_food.name} and {selected_drink.name} combo.')
result = selected_fruit_menu.total_price(count) + selected_food.total_price(count) + selected_drink.total_price(count)
print(f'Your total bill is: ${result}\nThanks for shopping with us...')