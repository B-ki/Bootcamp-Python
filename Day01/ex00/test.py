from book import Book
from recipe import Recipe
from datetime import datetime

r1 = Recipe("Pizza", 2, 27, ["Flour", "Water", "Tomato", "Cheese"], "", "lunch")
r2 = Recipe('Burger', 1, 15, ['Bread', 'Steak', 'Salad', 'Cheese'], "", 'lunch')
r3 = Recipe('Fries', 2, 27, ['Potatoes'], "", 'starter')
r4 = Recipe('Cake', 1, 15, ['Flour', 'Sugar', 'Egg', 'Chocolate'], "", 'dessert')

newdict = {'starter' : [r3], 'lunch' : [r1, r2], 'dessert' : []}

b1 = Book('My cookbook', datetime.now(), datetime.now(), "")

print(r1)
print(r2)
print(r3)
print(r4)
print(newdict)
print()

b1.add_recipe(r1)
b1.add_recipe(r2)
b1.add_recipe(r3)
list = b1.get_recipes_by_types("lunch")
for i in list:
    print(i)
print()
print(b1.get_recipe_by_name('Pizza'))
print()
b1.add_recipe(r4)
for key, value in b1.recipes_list.items():
    print(key, " : ")
    for i in value:
        print(i)



