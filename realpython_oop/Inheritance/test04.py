# Instances as Attributes

# When modeling something from the real world in code, you may find that
# you’re adding more and more detail to a class. You’ll find that you have a
# growing list of attributes and methods and that your files are becoming
# lengthy. In these situations, you might recognize that part of one class can
# be written as a separate class. You can break your large class into smaller
# classes that work together.

#For example, if we continue adding detail to the ElectricCar class, we
# might notice that we’re adding many attributes and methods specific to
# the car’s battery. When we see this happening, we can stop and move those
# attributes and methods to a separate class called Battery. 
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

    def fill_gas_tank(self):
        print("This car need a gas tank!")


class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery.")


class ElectricalCar(Car):

    def __init__(self, manufacturer, model, year): 
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

my_tesla = ElectricalCar('tesla', 'model s', 2019)
my_tesla.battery.describe_battery()