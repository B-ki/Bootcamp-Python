import six
type_list = ['lunch', 'starter', 'dessert']

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if not type(name).__name__ == 'str':
            raise TypeError("Name is not string")
        if not isinstance(description, str):
            raise TypeError("Description is not string")
        if not isinstance(recipe_type, six.string_types):
            raise TypeError("Recipe_type is not string")
        if recipe_type not in type_list:
            raise ValueError("Type must be lunch, starter or dessert")
        if not type(cooking_lvl) is int:
            raise TypeError("Cooking_lvl is not int")
        if not type(cooking_time) is int:
            raise TypeError("Cooking_time is not int")
        if type(ingredients) is not list or not all(isinstance(item, str) for item in ingredients):
            raise TypeError("Ingredients is not list of strings")
        if not name or not cooking_lvl or not cooking_time or not ingredients or not recipe_type:
            raise ValueError("Only description can be empty")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        text =  f"{self.name} - Cooking_lvl: {self.cooking_lvl}, Cooking_time: {self.cooking_time}, Type: {self.recipe_type}, Ingrediens: {*self.ingredients,}"
        return text

