num = int(input("Enter a number: "))
n = int(input("Enter the power: "))
for i in range(1, n+1):
    print(num, "^", i, "=", num**i)