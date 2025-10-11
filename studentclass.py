# create class
class Vehicle:

    # create init method
    def __init__(self, max_speed, mileage):
        # bind the arguements
        self.max_speed = max_speed
        self.mileage = mileage

# create object
ModelX = Vehicle(240, 18)

# access the variables inside init method
print("Model max speed:", ModelX.max_speed)
print("Model mileage:", ModelX.mileage)
