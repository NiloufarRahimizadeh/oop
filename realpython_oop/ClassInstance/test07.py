# Incrementing an Attribute’s Value Through a Method
class Car:

    def __init__(self):
        self.odometer_reading=40

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles



my_new_car = Car()
my_new_car.increment_odometer(10)
my_new_car.read_odometer()