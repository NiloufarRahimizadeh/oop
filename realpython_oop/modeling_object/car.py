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

    def get_range(self):
        if self.battery_size ==75:
            range = 260
        elif self.battery_size ==100:
            range =316

        print(f"This car can go about {range} miles on a full charge.")


class ElectricalCar(Car):

    def __init__(self, manufacturer, model, year): 
        super().__init__(manufacturer, model, year)
        self.battery = Battery()