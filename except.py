try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma:"))
    result = num1/num2
    print("The result is", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except SyntaxError:
    print("Comma is missing!!!")
except:
    print("Wrong input")
else:
    print("No exceptions were raised.")
finally:
    print("This will execute no martter what.")
