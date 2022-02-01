"""
Exercise 21: Area of a Triangle

The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:

area = b * h / 2

Write a program that allows the user to enter values for b and h. The program should
then compute and display the area of a triangle with base length b and height h.
"""

t_len = float(input("Enter length: "))
t_hei = float(input("Enter height: "))

print("The area of the triangle: {}".format((t_len * t_hei / 2)))

"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

base = float(input("Please enter the base of a triangle in units: "))
height = float(input("Please enter the perpendicular height of that triangle in units: "))

area = (base*height) / 2

print("The area of this triangle is {} units squared.".format(area))

"""
