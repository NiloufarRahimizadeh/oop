# Creating Multiple Instances
from test01 import Dog


my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
# In this example we create a dog named Willie and a dog 
# named Lucy. Each dog is a separate instance with its own 
# set of attributes, capable of the same set of actions.
# Even if we used the same name and age for the second dog, 
# Python would still create a separate instance from the Dog 
# class.

# as many instances from one class as you need, as long as 
# you give each instance a unique variable name or it occupies 
# a unique spot in a list or dictionary.

