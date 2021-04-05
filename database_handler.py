import os
import json

class DatabaseHandler:
    def __init__(self, path, num_days):
        self.path = path
        self.recipes = []
        self.num_days = num_days
        self.last_days = []
    
    def read_recipes(self):
        path_name = os.path.join(os.getcwd(), self.path)
        files = os.listdir(os.path.join(os.getcwd(), self.path))
        for filename in files:
            with open(os.path.join(path_name, filename), 'r') as f:
                data = json.load(f)
                self.recipes.append(data)

    def print_recipes(self):
        for recipe in self.recipes:
            print("nume = {}, ingredient = {}".format(recipe["nume"], recipe["nume"]))

    def read_last_days(self):
        pass

