#! /usr/bin/env python3

from book import Book
from recipe import Recipe

tourte = Recipe("tourte", 3, 60, ["tomate", "caca"], "descr", "starter")
t2 = Recipe("tourte2", 3, 10, ["tomate", "caca"], "descr", "lunch")
t3 = Recipe("tourte3", 3, 10, ["tomate", "caca"], "descr", "dessert")
to_print = str(tourte)
print(to_print)

b = Book("myBook")
print(b)

b.get_recipe_by_name("prout")
b.add_recipe(tourte)
b.add_recipe(t2)
b.add_recipe(t3)
b.get_recipes_by_types("starter")
b.get_recipes_by_types("scsc")
b.get_recipe_by_name("tourte2")
print(b)
