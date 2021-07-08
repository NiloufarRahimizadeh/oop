# Overriding Methods from the Parent Class
# You can override any method from the parent class that doesn’t fit what
# you’re trying to model with the child class.
# To do this, you define a method in the child class with the same name as 
# the method you want to override in the parent class.
# Python will disregard the parent class method and only
# pay attention to the method you define in the child class.
# Say the class Car had a method called fill_gas_tank(). This method is
# meaningless for an all-electric vehicle, so you might want to override this
# method. Here’s one way to do that:
# Now if someone tries to call fill_gas_tank() with an electric car, Python
# will ignore the method fill_gas_tank() in Car and run this code instead. When
# you use inheritance, you can make your child classes retain what you need
# and override anything you don’t need from the parent class.

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


class ElectricalCar(Car):

    def __init__(self, manufacturer, model, year, additional): #add anothe attribute
        super().__init__(manufacturer, model, year)
        self.battery_size = 75
        self.additional = additional

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


my_tesla = ElectricalCar("tesla", "model s", "2020", "")
my_tesla.fill_gas_tank()