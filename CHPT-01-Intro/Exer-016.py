"""
Exercise 16: Area and Volume

Write a program that begins by reading a radius, r , from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r . Use the pi constant in the math module in your
calculations.

Hint: The area of a circle is computed using the formula area = πr**2 . The
volume of a sphere is computed using the formula volume = 4/3 * πr * 3 .
"""

import math

rd = float(input("Enter radius of the circle: "))
print("Area: {}, Volume: {}".format( round((math.pi*rd**2),2), round((4/3 * math.pi * (rd * rd * rd)),2)))


"""
import math

r = float(input("Please enter a radius r: "))

area = math.pi * (r * r)
vol = (4/3) * math.pi * (r * r * r)

print("The area of a circle with radius r is {} units squared.".format(area))
print("The volume of a sphere with radius r is {} units cubed.".format(vol))
"""
