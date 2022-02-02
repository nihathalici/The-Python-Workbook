"""
Exercise 22: Area of a Triangle (Again)

In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s 1 , s 2 and s 3
be the lengths of the sides. Let s = (s 1 + s 2 + s 3 )/2. Then the area of the triangle
can be calculated using the following formula:

area = math.sqrt(s * (s-s1) * (s-s2) * (s-s3))

Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

import math

s1 = float(input("Please enter side a of a triangle: "))
s2 = float(input("Please enter side b of a triangle: "))
s3= float(input("Please enter side c of a triangle: "))

s = (s1+s2+s3) / 2

area = math.sqrt(s * (s-s1) * (s-s2) * (s-s3))

print("The area of the triangle is {} units squared.".format(area))
