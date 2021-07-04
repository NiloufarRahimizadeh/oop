# Making an Instance from a Class
# Think of a class as a set of instructions for how to 
# make an instance.

from test01 import Dog


my_dog = Dog("Willi", 6)

# we tell Python to create a dog whose name is 'Willie' 
# and whose age is 6.
# When Python reads this line, it calls the __init__() 
# method in Dog with the arguments 'Willie' and 6.
# The __init__() method creates an instance representing 
# this particular dog and sets the name and age attributes 
# using the values we provided.
# Python then returns an instance representing this dog.
print(my_dog)
# Accessing Attributes
# Dot notation is used often in Python.
print(my_dog.name)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling Methods
# After we create an instance from the class Dog, we can use 
# dot notation to call any method defined in Dog.
my_dog.sit()
my_dog.roll_over()