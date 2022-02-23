"""
Exercise 41: Classifying Triangles

A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
scalene. All three sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of the three sides of a triangle from the
user. Then display a message that states the triangle’s type.
"""

tri_type = ""

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 and side2 == side3:
        tri_type = "equilateral"
elif side1 == side2 or side2 == side3 or side3 == side1:
        tri_type = "isosceles"
else:
        tri_tpe = "scalene"

print("That's a {} triangle".format(tri_type))
