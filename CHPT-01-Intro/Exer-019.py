"""
Exercise 19: Free Fall

Create a program that determines how quickly an object is travelling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume
that the acceleration due to gravity is 9.8 m/s**2 .

You can use the formula to compute the final speed, , when the initial speed, , acceleration,
a, and distance, d, are known.
"""
# Author's solution

from math import sqrt

GRAVITY = 9.8

# Read the height
d = float(input("Height (in meters): "))

# Compute the final velocity
vf = sqrt(2 * GRAVITY * d)

print("It will hit the ground at %.2f m/s" % vf)
