def factorial(n):
    ''' this is an recursive function to calculate factorial of a number '''

    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial.__doc__)
print("The factorial of 0 is ", factorial(0))
print("The factorial of 1 is ", factorial(1))
print("The factorial of 2 is ", factorial(2))
print("The factorial of 5 is ", factorial(5))
print("The factorial of 10 is ", factorial(10))