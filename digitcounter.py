num = int(input("Enter a number to count its digits: "))
n = num
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Number of digits in", n, "is",count)