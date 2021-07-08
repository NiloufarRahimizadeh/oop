# Working with Classes and Instances
# You can use classes to represent many real-world situations. Once you write
# a class, you’ll spend most of your time working with instances created from
# that class.

# One of the first tasks you’ll want to do is modify the attributes 
# associated with a particular instance. You can modify the attributes 
# of an instance directly or write methods that update attributes in 
# specific ways.

# The Car Class
class Car:
    # Class attribute
    tyre = 4
    # Instance attribute
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()


Car.tyre=3    
print(Car.tyre)
my_new_car = Car("audi", "a4", 2020)
print(my_new_car.get_descriptive_name())