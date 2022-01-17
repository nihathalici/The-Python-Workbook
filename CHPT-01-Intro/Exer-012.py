"""
Exercise 12: Distance Between Two Points on Earth

The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t 1 , g 1 ) and (t 2 , g 2 ) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:

distance = 6371.01 × arccos(sin(t 1 ) × sin(t 2 ) + cos(t 1 ) × cos(t 2 ) × cos(g 1 − g 2 ))

The value 6371.01 in the previous equation wasn’t selected at random. It is the
average radius of the Earth in kilometers.
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.

Hint: Python’s trigonometric functions operate in radians. As a result, you will
need to convert the user’s input from degrees to radians before computing the
distance with the formula discussed previously. The math module contains a
function named radians which converts from degrees to radians.
"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

import math

t1 = float(input("Please enter the x value of a point on Earth in degrees: "))
t2 = float(input("Please enter the y value for that point on Earth in degrees: "))

g1 = float(input("lease enter the x value of a 2nd point on Earth in degrees: "))
g2 = float(input("lease enter the y value for that point on Earth in degrees: "))

distance = 6371.01 * math.acos( math.sin(math.radians(t1)) * math.sin(math.radians(g1)) + \
           math.cos(math.radians(t1)) * math.cos(math.radians(g1)) * math.cos(math.radians(t2 - g2)))


print("The distance between these two points on Earth is {}km".format(distance))


