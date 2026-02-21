def define_name():
    print("Please enter the name of the table you want to create")
    name = input()
    return name


def define_headers():
    headers = {}

    print("What fields should your tasks present ?")
    print("Press 'Enter' to confirm each entry")
    print("Enter 'q' when you are done.")

    i = 0
    choice = 0

    while True:
        choice = input()
        if choice == "q":
            break
        else:
            headers[i] = choice
            i += 1

    print("the column headers you defined are :")
    i = 0
    for i in range(0, len(headers)):
        print(f"Header {i + 1} is {headers[i]}")
    print("is it ok (y/n) ?")

    validation = input()

    if validation == "y":
        return headers
    else:
        pass


class Table:
    def __init__(self, table_name, headers):
        self.table_name = table_name
        self.headers = headers
