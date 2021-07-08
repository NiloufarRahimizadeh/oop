# Inheritance
# If the class you’re writing is a specialized version of another 
# class you wrote, you can use inheritance.
# When one class inherits from another, it takes on the attributes 
# and methods of the first class.
# The original class is called the parent class, and the new class 
# is the child class.
# The child class can inherit any or all of the attributes and methods 
# of its parent class, but it’s also free to define new attributes and 
# methods of its own.

# The __init__() Method for a Child Class

# When you’re writing a new class based on an existing class, you’ll 
# often want to call the __init__() method from the parent class. 
# This will initialize any attributes that were defined in the parent 
# __init__() method and make them available in the child class.
          
# As an example, let’s model an electric car. An electric car is just 
# a specific kind of car.

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

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)


my_tesla = ElectricalCar("tesla", "model s", 2020)
print(my_tesla.get_descriptive_name())

# The __init__() method  takes in the information required to make a 
# Car instance.
# The super() function  is a special function that allows you to call 
# a method from the parent class.
# The name super comes from a convention of calling the parent class 
# a superclass and the child class a subclass.