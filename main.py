import sys
import os
import database_handler


def main(argv):
    if len(argv) != 2:
        print("Please provide the path for the recipes")
    print("path = " + argv[1])
    database = database_handler.DatabaseHandler(argv[1], 4)
    database.read_recipes()
    database.print_recipes()
   
    



if __name__ == "__main__":
    main(sys.argv)
