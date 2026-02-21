import pandas
from menus import main_menu

choice = 0
while choice != str(3):
    main_menu()
    choice = input()

df = pandas.read_csv("./test_file.csv", header=1)

print(df)
