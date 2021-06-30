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

# When we make an instance of Dog, Python will call 
# the __init__() method from the Dog class. We’ll 
# pass Dog()a name and an age as arguments; self is 
# passed automatically, so we don’t need to pass it.

# Whenever we want to make an instance from the Dog 
# class, we’ll provide values for only the last two 
# parameters, name and age.

# The two variables defined at each have the prefix 
# self. Any variable prefixed with self is available 
# to every method in the class, and we’ll also be able 
# to access these variables through any instance created 
# from the class.
# Variables that are accessible through instances like 
# this are called attributes.
# The instances we create later will have access 
# to these methods (sit and roll_overed). In other words, 
# they’ll be able to sit and roll over.
# if this class were part of an actual computer game, 
# these methods would contain code to make an animated 
# dog sit and roll over. If this class was written to 
# control a robot, these methods would direct movements 
# that cause a robotic dog to sit and roll over.