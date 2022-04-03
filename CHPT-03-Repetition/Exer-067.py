"""
Exercise 67: Compute the Perimeter of a Polygon

Write a program that computes the perimeter of a polygon. Begin by reading the
x and y coordinates for the first point on the perimeter of the polygon from the
user. Then continue reading pairs of values until the user enters a blank line for the
x-coordinate. Each time you read an additional coordinate you should compute the
distance to the previous point and add it to the perimeter. When a blank line is entered
for the x-coordinate your program should add the distance from the last point back
to the first point to the perimeter. Then the perimeter should be displayed. Sample
input and output values are shown below. The input values entered by the user are
shown in bold.

Enter the first x-coordinate: 0
Enter the first y-coordinate: 0
Enter the next x-coordinate (blank to quit): 1
Enter the next y-coordinate: 0
Enter the next x-coordinate (blank to quit): 0
Enter the next y-coordinate: 1
Enter the next x-coordinate (blank to quit):
The perimeter of that polygon is 3.414213562373095
"""

# Author's solution
##
# Compute the perimeter of a polygon constructed from points entered by the user. A blank line
# will be entered for the x-coordinate to indicate that all of the points have been entered.
#
from math import sqrt

# Store the perimeter of the polygon
perimeter = 0

# Read the coordinate of the first point
first_x = float(input("Enter the first x-coordinate: "))
first_y = float(input("Enter the first y-coordinate: "))

# Provide initial values for prev x and prev y
prev_x = first_x
prev_y = first_y

# Read the remaining coordinates
line = input("Enter the next x-coordinate (blank to quit): ")
while line != "":
    # Convert the x-coordinate to a number and read the y coordinate
    x = float(line)
    y = float(input("Enter the next y-coordinate: "))

    # Compute the distance to the previous point and add it to the perimeter
    dist = sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
    perimeter = perimeter + dist

    # Set up prev x and prev y for the next loop iteration
    prev_x = x
    prev_y = y

    # Read the next x-coordinate
    line = input("Enter the next x-coordinate (blank to quit): ")

# Compute the distance from the last point to the first point and add it to the perimeter
dist = sqrt((first_x - x) ** 2 + (first_y - y) ** 2)
perimeter = perimeter + dist

# Display the result
print("The perimeter of that polygon is", perimeter)
