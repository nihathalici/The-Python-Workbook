"""
Exercise 18: Volume of a Cylinder

The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

import math

radius = float(input("Please enter a radius for a cylinder: "))
height = float(input("Please enter the height of than cylinder: "))

volume = math.pi * (radius * radius) * height

print("The volume of this cylinder is {0:0.01f} units cubed.".format(volume))
