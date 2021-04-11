import os
import json
import random

class DatabaseHandler:
    def __init__(self, path_retete, path_last_days, num_days):
        self.path_retete = path_retete
        self.path_last_days = path_last_days
        self.recipes = []
        self.num_days = num_days
        self.last_days = []
        random.seed()

    def read_recipes(self):
        path_name = os.path.join(os.getcwd(), self.path_retete)
        files = os.listdir(os.path.join(os.getcwd(), self.path_retete))
        for filename in files:
            with open(os.path.join(path_name, filename), 'r') as f:
                data = json.load(f)
                self.recipes.append(data)

    def print_recipes(self):
        for recipe in self.recipes:
            print("nume = {}, ingredient = {}".format(recipe["nume"], recipe["ingredient"]))

    def pick_random_recipe(self):
        recipe_index = random.randint(0, len(self.recipes) - 1)
        self.chosen_recipe = self.recipes[recipe_index]
        print("Chosen recipe {}".format(self.chosen_recipe["nume"]))
        while response := input("Is the recipe ok? y/n\n") == 'n':
            indexes = list(range(0, recipe_index)) + list(range(recipe_index + 1, len(self.recipes) - 1))
            recipe_index = random.choice(indexes)
            self.chosen_recipe = self.recipes[recipe_index]
            print("Chosen recipe {}".format(self.chosen_recipe["nume"]))
        

    def read_last_days(self):
        path_name = os.path.join(os.getcwd(), self.path_last_days)
        files = os.listdir(os.path.join(os.getcwd(), self.path_last_days))
        for filename in files:
            with open(os.path.join(path_name, filename), 'r') as f:
                data = json.load(f)
                self.last_days.append(data)

    def remove_eaten_recipes(self):
        for eaten_recipe in self.last_days:
            self.recipes = [recipe for recipe in self.recipes if not(recipe["ingredient"] == eaten_recipe["ingredient"])]

    def write_chosen_recipe(self):
        path_name = os.path.join(os.getcwd(), self.path_last_days)
        files = os.listdir(path_name)
        files = [path_name + '\\' + file for file in files]

        if len(files) == self.num_days:
            oldest_file = min(files, key=os.path.getmtime)
            os.remove(os.path.join(path_name, oldest_file))

        with open(os.path.join(path_name, self.chosen_recipe["nume"] + '.json'), 'w') as f:
            json.dump(self.chosen_recipe, f, indent=4)