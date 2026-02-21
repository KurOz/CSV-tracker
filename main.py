import sys
from menus import main_menu

while True:
    main_menu()
    choice = input()

    match choice:
        case "1":
            print("you chose 1")
        case "2":
            print("you chose 2")
        case "3":
            print("\nGood bye !")
            sys.exit()
        case _:
            print("Please enter a valid choice")
