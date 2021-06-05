import argparse


parser = argparse.ArgumentParser(description="This program prints recipes \
consisting of the ingredients you provide.")

parser.add_argument("-i1", "--ingredient_1", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i2", "--ingredient_2", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i3", "--ingredient_3", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i4", "--ingredient_4", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i5", "--ingredient_5", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")

parser.add_argument("--salt", action="store_true", help="Specify if you'd like to use salt in your recipe.")
parser.add_argument("--pepper", default="False", help="Change to 'True' if you'd like to use pepper in your recipe.")

args = parser.parse_args()

ingredients = [args.ingredient_1, args.ingredient_2, args.ingredient_3,
               args.ingredient_4, args.ingredient_5]
if args.salt:
    ingredients.append("salt")
if args.pepper == "True":
    ingredients.append("pepper")

print(f"The ingredients you provided are: {ingredients}")


def find_a_recipe(ingredients):
    ...
    # processes the input and returns a recipe depending on the provided ingredients

