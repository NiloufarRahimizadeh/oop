# Defining Attributes and Methods for the Child Class
# Once you have a child class that inherits from a parent class, you can add
# any new attributes and methods necessary to differentiate the child class
# from the parent class.
# Let’s add an attribute that’s specific to electric cars (a battery, for
# example) and a method to report on this attribute.

class Car:

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading}")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!")

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage


class ElectricalCar(Car):

    def __init__(self, manufacturer, model, year, additional): #add anothe attribute
        super().__init__(manufacturer, model, year)
        self.battery_size = 75
        self.additional = additional

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery")


my_tesla = ElectricalCar("tesla", "model s", "2020", "")
my_tesla.describe_battery()