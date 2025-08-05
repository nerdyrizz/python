units = int(input("Enter the number of units consumed: "))
if units < 50:
    charge = units * 2.60
    surcharge = 25
elif units <= 100:
    charge = 130 + ((units - 50) * 3.25)
    surcharge = 35
elif units <= 200:
    charge = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45
else:
    charge = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75
total_bill = charge + surcharge
print("\n Electricity Bill = %.2f" % total_bill)