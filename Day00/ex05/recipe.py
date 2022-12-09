import string
import six
cookbook = {        
    'Sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'Cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'Salad': {
        'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def printName(mydic):
    if not type(mydic) is dict:
        print("Param1 is not a dict")
        exit()
    for key, value in mydic.items():
        print(key)


def printIngredients(mydic):
    if not type(mydic) is dict:
        print("Param1 is not a dict")
        exit()
    for key, value in mydic.items():
        if key == 'ingredients':
            print("Ingredients list: ", value)


def printTypeMeal(mydic):
    if not type(mydic) is dict:
        print("Param1 is not a dict")
        exit()
    for key, value in mydic.items():
        if key == 'meal':
            print("To be eaten for ", value, ".")


def printPrepTime(mydic):
    if not type(mydic) is dict:
        print("Param1 is not a dict")
        exit()
    for key, value in mydic.items():
        if key == 'prep_time':
            print ("Takes ", value, " of cooking.")


def printCookbook(mydic):
    print("\n---------------------\n")
    for key, value in mydic.items():
        print("Recipe for ", key, " :")
        printIngredients(value) 
        printTypeMeal(value) 
        printPrepTime(value)
        print("\n---------------------\n")


def printMeal(mydic, n):
    if not type(mydic) is dict:
        print("Param1 is not a dict")
        exit()
    if not isinstance(n, six.string_types):
        print("Param2 is not a string")
        exit()
    for key, value in mydic.items():
        if key == n:
            print("\n---------------------\n")
            print("Recipe for ", key, " :")
            printIngredients(value) 
            printTypeMeal(value) 
            printPrepTime(value)
            print("\n---------------------\n")


def delRecipe(mydic, n):
    if not type(mydic) is dict:
        print("Param1 is not a dict")
        exit()
    if not isinstance(n, six.string_types):
        print("Param2 is not a string")
        exit()
    del mydic[n] 


def addRecipe(mydic):
    if not type(mydic) is dict:
        print("Param1 is not a dict")
        exit()
    try:
        name = input("Enter a name: ")
        inputString = input("Enter ingredients separated by space: ")
        ingList = inputString.split(" ")
        meal = input("Enter a meal type: ")
        prep_time = input("Enter a prep_time in min (positive int): ")
    except EORError as e:
        print(e)
    newdic = {name: {'ingredients': ingList, 'meal': meal, 'prep_time': prep_time}}
    mydic.update(newdic)


def printOptions():
    print("List of available oiptions:")
    print("   1. Add a recipe")
    print("   2. Delete a recipe")
    print("   3. Print a recipe")
    print("   4. Print the cookbook")
    print("   5. Quit")


def getInt():
    while True:
        try:
            i = int(input("Please select an option:\n>> "))
        except ValueError:
            continue
        else:
            break
    return i


def getStr():
    while True:
        try:
            str = input("Please enter a recipe name:\n>> ")
        except ValueError:
            continue
        else:
            break
    return str


choice = 0
print("Welcome to the Python Cookbook !")
while choice == 0:
    printOptions()
    while choice < 1 or choice > 5:
        choice = getInt()
        if choice < 1 or choice > 5:
            print("Sorry, this option does not exist")
            printOptions()
    if choice == 1:
        addRecipe(cookbook)
    elif choice == 2:
        s = getStr()
        delRecipe(cookbook, s)
    elif choice == 3:
        s = getStr()
        printMeal(cookbook, s)
    elif choice == 4:
        printCookbook(cookbook)
    elif choice == 5:
        exit()
    choice = 0

