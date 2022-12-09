import six
from datetime import datetime
from recipe import Recipe
type_list = ['lunch', 'starter', 'dessert']

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        if not isinstance(name, six.string_types):
            raise TypeError("Name is not string")
        if not type(last_update) is datetime:
            raise TypeError("Last_update is not datetime")
        if not type(creation_date) is datetime:
            raise TypeError("Creation_dae is not datetime")
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = {'starter' : [], 'lunch' : [], 'dessert' : []}


    def get_recipe_by_name(self, name):
        if not isinstance(name, six.string_types):
            raise TypeError("Recipe_type is not string")
        for key, value in self.recipes_list.items():
            for i in value:
                if i.name == name:
                    print(i)
                    return i


    def get_recipes_by_types(self, recipe_type):
        if not isinstance(recipe_type, six.string_types):
            raise TypeError(" is not string")
        if not recipe_type in type_list:
            raise ValueError("LOL GUS")
        ret = self.recipes_list[recipe_type]
        return ret


    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise TypeError("recipe is not a Recipe")
        for key, value in self.recipes_list.items():
            if key == recipe.recipe_type:
                value.append(recipe)
        self.last_update = datetime.now()

