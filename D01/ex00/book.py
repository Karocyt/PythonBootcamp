import datetime as dt
from recipe import Recipe


class Book:
    def __str__(self):
        """Return the string to print with the book info"""
        recs = "\n".join("".join(str(self.recipes[r_type][recipe])
                                 for recipe in self.recipes[r_type])
                         for r_type in self.recipes)
        return (self.name + f" created on {self.creation_date}\n"
                f"last modified on {self.last_update}\n"
                f"recipes:\n{recs}\n")

    def __init__(self, name: str, recipes: dict = {}):
        """Init book"""
        if name == "":
            raise ValueError("name cannot be empty")
        self.name: str = name
        self.recipes: dict = {"starter": {}, "lunch": {}, "dessert": {}}
        self.creation_date: dt.datetime = dt.datetime.now()
        self.last_update: dt.datetime = self.creation_date

    def get_recipe_by_name(self, name: str):
        """Print a recipe with the name `name` and return the instance"""
        for i in self.recipes:
            if name in self.recipes[i]:
                print(self.recipes[i][name])
                return self.recipes[i][name]
        else:
            print(f"{name} not found")
            return False

    def get_recipes_by_types(self, r_type: str):
        """Get all recipe names for a given recipe_type """
        for cat in self.recipes:
            if r_type == cat:
                return self.recipes[r_type]
        print(f"'{r_type} is not a valid recipe type")
        return []

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        if recipe.name == "" or recipe.recipe_type not in self.recipes:
            print("recipe name invalid.")
        else:
            self.recipes[recipe.recipe_type][recipe.name] = recipe
            self.last_update = dt.datetime.now()
