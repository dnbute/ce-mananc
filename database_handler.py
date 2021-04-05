import os
import json

class DatabaseHandler:
    def __init__(self, path):
        self.path = path
        self.recipes = []
    
    def read_recipes(self):
        path_name = os.path.join(os.getcwd(), self.path)
        files = os.listdir(os.path.join(os.getcwd(), self.path))
        for filename in files:
            with open(os.path.join(path_name, filename), 'r') as f:
                data = json.load(f)
                self.recipes.append(data)
                print(data)

