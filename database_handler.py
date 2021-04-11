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
        self.chosen_recipe = self.recipes[random.randint(0, len(self.recipes) - 1)]
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
            self.recipes.remove(eaten_recipe)

    def write_chosen_recipe(self):
        path_name = os.path.join(os.getcwd(), self.path_last_days)
        with open(os.path.join(path_name, self.chosen_recipe["nume"] + '.json'), 'w') as f:
            json.dump(self.chosen_recipe, f, indent=4)

