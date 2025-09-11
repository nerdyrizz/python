try:
    number = int(input("Enter a number: "))
    print("The number is", number)
except ValueError as ex:
    print("Exeption:", ex)