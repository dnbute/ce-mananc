import sys
import os
import database_handler


def main(argv):
    if len(argv) != 3:
        print("Please provide the path for the recipes and for the last n days")
    print("recipe path = " + argv[1])
    print("database path = " + argv[2])
    database = database_handler.DatabaseHandler(argv[1], argv[2], 4)
    database.read_recipes()
    database.read_last_days()
    database.remove_eaten_recipes()
    database.print_recipes()
    database.pick_random_recipe()
    database.write_chosen_recipe()
   
    



if __name__ == "__main__":
    main(sys.argv)
