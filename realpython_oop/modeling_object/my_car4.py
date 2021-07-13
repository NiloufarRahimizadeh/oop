# Importing All Classes from a Module 
from car import *
# This method is not recommended for
# Importing a Module into a Module
# Sometimes you’ll want to spread out your classes over several modules
# to keep any one file from growing too large and avoid storing unrelated
# classes in the same module. When you store your classes in several modules,
# you may find that a class in one module depends on a class in another mod-
# ule. When this happens, you can import the required class into the first
# module. 
# Using Aliases

from car import ElectricalCar as EC
my_tesla = EC('tesla', 'roadster', 2019)

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)