# Importing Multiple Classes from a Module
from car import ElectricalCar, Car



my_tesla = ElectricalCar("tesla", "model s", 2020)

print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.describe_battery()

# Importing an Entire Module