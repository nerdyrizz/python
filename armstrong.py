n = int(input("Enter a number:"))

sum = 0  # initialize
temp = n
while temp>0:
    digit =  temp % 10
    sum = sum + digit ** 3
    temp //= 10

if sum == n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number.")