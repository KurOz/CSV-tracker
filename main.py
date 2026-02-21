from menus import main_menu

while True:
    main_menu()
    choice = input()

    match choice:
        case str(1):
            print("you chose 1")
        case str(2):
            print("you chose 2")
        case str(3):
            exit
        case _:
            print("Please enter a valid choice")

print("\nGood bye !")
