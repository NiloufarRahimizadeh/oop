# Setting a Default Value for an Attribute

class Car:

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        print(f"{self.manufacturer} has {self.odometer_reading} miles on it.")


my_new_car = Car("audi", "a4", 2020)
my_new_car.read_odometer()
# Not many cars are sold with exactly 0 miles on the odometer, so we 
# need a way to change the value of this attribute.

# Modifying Attribute Values

# You can change an attribute’s value in three ways:
# 1)you can change the value directly through an instance,
# 2)set the value through a method,
# 3)or increment the value (add a certain amount to it) through a method.

# Modifying an Attribute’s Value Directly
my_new_car.odometer_reading=23
my_new_car.manufacturer="toyota"
my_new_car.read_odometer()

# Modifying an Attribute’s Value Through a Method
