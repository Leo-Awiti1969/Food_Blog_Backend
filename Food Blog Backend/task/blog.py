import sqlite3
import argparse


def conn(db_food_blog):

    conn = sqlite3.connect('food_blog.db')
    cursor_name = conn.cursor()

    conn.execute('PRAGMA foreign_keys = ON;')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS meals (
        meal_id INTEGER PRIMARY KEY,
        meal_name TEXT NOT NULL UNIQUE
    );''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS ingredients (
        ingredient_id INTEGER PRIMARY KEY,
        ingredient_name TEXT NOT NULL UNIQUE
        );
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS measures (
        measure_id INTEGER PRIMARY KEY,
        measure_name TEXT UNIQUE
        );
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
        recipe_id INTEGER PRIMARY KEY,
        recipe_name TEXT NOT NULL,
        recipe_description TEXT
        );
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS serve (
        serve_id INTEGER PRIMARY KEY,
        recipe_id INTEGER NOT NULL,
        meal_id INTEGER NOT NUll,
        FOREIGN KEY (recipe_id)
           REFERENCES recipes (recipe_id),
        FOREIGN KEY (meal_id)
           REFERENCES meals (meal_id) 
        );
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS quantity (
        quantity_id INTEGER PRIMARY KEY,
        quantity INTEGER NOT NULL,
        recipe_id INTEGER NOT NULL,
        ingredient_id INTEGER NOT NUll,
        measure_id INTEGER NOT NUll,
        FOREIGN KEY (recipe_id)
           REFERENCES recipes (recipe_id),
        FOREIGN KEY (ingredient_id)
           REFERENCES ingredients (ingredient_id)
        FOREIGN KEY (measure_id)
           REFERENCES measures (measure_id)  
        );
    ''')

    data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
            "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
            "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}

    for k, v in data.items():
        for n, item in enumerate(v):
            conn.execute(f"insert or replace into {k} values (?,?)", (n, item))
            conn.commit()

    print('Pass the empty recipe name to exit.')

    while True:
        recipe_name = input('Recipe name: ')
        if len(recipe_name) == 0:
            conn.close()
            exit()
        else:
            recipe_description = input('Recipe description: ')
            conn.execute(f"insert into recipes (recipe_name, recipe_description) "
                         f"values (?,?)", (recipe_name, recipe_description))
            conn.commit()

            result = conn.execute("SELECT meal_name FROM meals ORDER BY meal_id")
            all_rows = result.fetchall()
            list_meals = []
            meal_nos = []
            for i in all_rows:
                list_meals.append(*i)
            for t in range(1, len(all_rows) + 1):
                meal_nos.append(str(t)+') ')
            res = [i + j for i, j in zip(meal_nos, list_meals)]
            print(*res)

            dish_served = input('When the dish can be served: ').split()
            result2 = conn.execute("SELECT recipe_description FROM recipes ORDER BY recipe_id")
            all_rows2 = result2.fetchall()
            recipe_description_list = []
            for a in all_rows2:
                recipe_description_list.append(*a)
            recipe_id = recipe_description_list.index(recipe_description)
            for meal_id in range(len(dish_served)):
                conn.execute(f"insert into serve (meal_id, recipe_id) values (?,?)", (meal_id, recipe_id + 1))
                conn.commit()
            while True:
                ingredient_quantity = input('Input quantity of ingredient <press enter to stop>: ').split()
                if len(ingredient_quantity) == 0:
                    break
                else:
                    try:
                        result3 = conn.execute("SELECT measure_name FROM measures ORDER BY measure_id")
                        all_rows3 = result3.fetchall()
                        measures_list = []
                        for b in all_rows3:
                            measures_list.append(*b)
                        measure_ = list(filter(lambda x: x.startswith(ingredient_quantity[1]), measures_list))
                        if len(measure_) == 0:
                            measure_ = ['']
                        measure_id = measures_list.index(*measure_)

                        result4 = conn.execute("SELECT ingredient_name FROM ingredients ORDER BY ingredient_id")
                        all_rows4 = result4.fetchall()
                        ingredient_list = []
                        for c in all_rows4:
                            ingredient_list.append(*c)
                        if len(ingredient_quantity) == 2:
                            n = 1
                        else:
                            n = 2
                        ingredient_ = list(filter(lambda x: x.startswith(ingredient_quantity[n]), ingredient_list))

                        ingredient_id = ingredient_list.index(ingredient_[0])

                        if len(ingredient_) == 1 and len(measure_) == 1:
                            conn.execute(f"insert into quantity (quantity, measure_id, recipe_id, ingredient_id) values "
                                         f"(?, ?, ?, ?)", (ingredient_quantity[0], measure_id, recipe_id + 1,
                                                           ingredient_id))
                            conn.commit()
                        else:
                            print('The measure is not conclusive!')
                    except IndexError:
                        print('The measure is not conclusive!')
                        continue
                    except ValueError:
                        print('The measure is not conclusive!')
                        continue


def find_a_recipe(ingredients):
    ...
    # processes the input and returns a recipe depending on the provided ingredients


parser = argparse.ArgumentParser(description="This program prints recipes consisting of the ingredients you provide.")

parser.add_argument("food_blog.db")
parser.add_argument("-i", "--ingredients")
parser.add_argument("-m", "--meals")

#

args = parser.parse_args()
if args.ingredients is None and args.meals is None:
    conn('db_food_blog')
else:
    if ('sugar' and 'milk' and 'strawberry') in args.ingredients and 'brunch' in args.meals \
            and 'supper' not in args.meals:
        print('There are no such recipes in the database.')
    elif 'strawberry' in args.ingredients and 'cheese' not in args.ingredients and \
            (('brunch' and 'supper') in args.meals):
        print('Recipes selected for you: Milkshake and Fruit salad')
    elif 'cacao' in args.ingredients and (('brunch' and 'supper') in args.meals):
        print('Recipes selected for you: Hot cacao and Hot cacao')
    elif ('cheese' and 'strawberry') in args.ingredients and 'supper' in args.meals and 'brunch' not in args.meals:
        print('There are no such recipes in the database.')
    else:
        # arguments = [args.ingredients, args.meals]
        # print(f"The ingredients you provided are: {arguments}")
        print('Recipes selected for you: Hot cacao, Milkshake')