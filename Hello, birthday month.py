def hello():
    name = input("Enter name: ")
    month = input("Enter month: ")
    print("Happy birthday " + name)
    if month.lower() == "august":
        print("Happy birthday " + month)


hello()