#! /usr/bin/env python3

cookbook = {
    "sandwich": {
        "ingredients": ("ham", "bread", "cheese", "tomatoes"),
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ("floor", "sugar", "eggs"),
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ("avocado", "arugula", "tomatoes", "spinach"),
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_recipe(name):
    recipe = cookbook[name]
    ilist = ", ".join(recipe["ingredients"])
    meal = recipe["meal"]
    prep_time = recipe["prep_time"]
    print(f"{name.capitalize()} recipe:\n"
          f"Ingredients: {ilist}\n"
          f"Perfect as a {meal}\n"
          f"Done in {prep_time} minutes only!\n")


def print_recipe_menu():
    name = input("Please enter the recipe's name: ")
    if name not in cookbook:
        print("Invalid recipe name, try to print the cookbook")
    else:
        print_recipe(name)


def print_cookbook():
    print("This is all we got!\n\n")
    for name in cookbook:
        print_recipe(name)


def add_recipe():
    name = ""
    while name == "":
        name = input("Please enter a name for your new recipe\n")
    if name.lower() in cookbook:
        print("We already have this one, but we apreciate your effort!")
        return
    meal = input(f"What meal is the best to eat {name}?\n")
    ingredients = input(
        "What is in your delicious dish ? "
        "(comma separated ingredients)").split(",")
    print(ingredients)
    if ingredients[0] == "":
        print("A recipe needs ingredients, unless you can make "
              "food appear from thin air? Nah, you would be long gone.")
        return
    ingredients = (item.strip() for item in ingredients)
    prep_time = input("How long does it takes to cook? (number, minutes)\n")
    try:
        prep_time = int(prep_time)
        if prep_time <= 0:
            raise Exception()
    except Exception:
        print("Should be a positive number, "
              "I do think you got nothing of how this works!")
        return
    cookbook[name.lower()] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }
    print(f"We now have {name} in our cookbook, thanks!")


def del_recipe():
    name = input().lower()
    if name not in cookbook:
        print(f"We couldn't find '{name}' in the cookbook...")
    else:
        del cookbook[name]
        print(f"We deleted {name} from the cookbook")


MENU = ("1: Add a recipe\n"
        "2: Delete a recipe\n"
        "3: Print a recipe\n"
        "4: Print the cookbook\n"
        "5: Quit\n")

utils = (add_recipe, del_recipe, print_recipe_menu, print_cookbook)


def prog():
    while True:
        print()
        tmp = input(MENU)
        try:
            choice = int(tmp)
        except ValueError:
            print("ERROR: invalid choice")
            continue
        if choice == 5:
            print("See you soon ;)")
            return
        if choice == 0 or choice > 4:
            print("ERROR: invalid choice")
            continue
        try:
            utils[choice - 1]()
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    prog()
