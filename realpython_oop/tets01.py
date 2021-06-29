# Object-oriented programming is one of the most 
# effective approaches to writing software.

# In object-oriented programming you write classes 
# that represent real-world things and situations, 
# and you create objects based on these classes.
# When you write a class, you define the general
# behavior that a whole category of objects can have.
# When you create individual objects from the class, 
# each object is automatically equipped with the general 
# behavior; you can then give each object whatever unique 
# traits you desire.
# You’ll be amazed how well real-world situations can 
# be modeled with object-oriented programming.
# Making an object from a class is called instantiation, 
# and you work with instances of a class.
# You’ll specify the kind of information that can be stored 
# in instances, and you’ll define actions that can be taken 
# with these instances.
# You’ll also write classes that extend the functionality of 
# existing classes, so similar classes can share code 
# efficiently.
# Creating the Dog Class
# By convention, capitalized names refer to classes in Python.
class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

# The __init__() Method
# A function that’s part of a class is a method.
# The __init__() method at w is a special method 
# that Python runs automatically whenever we create 
# a new instance based on the Dog class.
# The __init__() method at w is a special method 
# that Python runs automatically whenever we create 
# a new instance based on the Dog class.
# The self parameter is required in the method 
# definition, and it must come first before the 
# other parameters.
# Every method call associated with an instance 
# automatically passes self, which is a reference 
# to the instance itself; it gives the individual 
# instance access to the attributes and methods in 
# the class.