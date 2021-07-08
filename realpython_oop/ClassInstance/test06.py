# Modifying an Attribute’s Value Through a Method
class Car:

    def __init__(self):
        self.odometer_reading=40

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def odometer_update(self, mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can not roll back an odometer!")

    
my_new_car = Car()
my_new_car.odometer_update(23)
my_new_car.read_odometer()