"""
Exercise 23: Area of a Regular Polygon

A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:

area = (n * s ** 2) / (4 * tan(pi / n))

Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.

"""
from math import tan, pi

s = float(input("Enter the length of each side: "))
n = int(input("Enter the number of sides: "))

area = (n * s ** 2) / (4 * tan(pi / n))

print("The area of the polygon is ", area)
