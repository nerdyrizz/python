temp = int(input("Enter the temperature in Celsius: "))
if temp < 0:
    print("It's cold outside. Wear a warm coat!")
elif 0 <= temp <= 20:
    print("It's a bit chilly. A sweater should be fine.")
else:
    print("It's warm outside. Light clothing is recommended.")