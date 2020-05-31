class Recipe:
    def __str__(self):
        """Return the string to print with the recipe info"""
        ingr = ", ".join(self.ingredients)
        return (self.name.capitalize() +
                f" {self.recipe_type} recipe (level: "
                f"{self.cooking_lvl}/5):\n"
                f"ingredients: {ingr}\n"
                f"description: {self.description}\n"
                f"cooking time: {self.cooking_time}\n")

    def __init__(self, name: str, cooking_lvl: int,
                 cooking_time: int, ingredients: list, descr, recipe_type):
        """Init recipe"""
        if name == "":
            raise ValueError("the recipe name cannot be empty")
        self.name: str = name
        self.cooking_lvl: int = cooking_lvl
        if self.cooking_lvl < 0 or self.cooking_lvl > 5:
            raise ValueError("invalid cooking level")
        self.cooking_time: int = cooking_time
        if self.cooking_time < 0:
            raise ValueError("negative cooking time")
        self.ingredients: list = ingredients
        for i, ingr in enumerate(ingredients):
            self.ingredients[i] = str(ingredients[i])
            if self.ingredients[i] == "":
                raise ValueError(f"ingredients num {i} is an empty string")
        self.description: str = descr
        if recipe_type in ["starter", "lunch", "dessert"]:
            self.recipe_type: str = recipe_type
        else:
            raise ValueError(f"'{recipe_type}' is not a valid recipe type "
                             "(starter, lunch or dessert)")
