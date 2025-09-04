def cube(num):
    return num ** 3

def divisible(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False

print(divisible(9))
print(divisible(8))
