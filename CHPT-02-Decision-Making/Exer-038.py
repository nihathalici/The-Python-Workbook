"""
Exercise 38: Name That Shape

Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
"""

sides = int(input("Enter the number of sides of the shape: "))

if sides == 3:
    print("It's a triangle.")
elif sides == 4:
    print("It's a square.")
elif sides == 5:
    print("It's a pentagon.")
elif sides == 6:
    print("It's a hexagon.")
elif sides == 7:
    print("It's a heptagon.")
elif sides == 8:
    print("It's a octagon.")
elif sides == 9:
    print("It's a nonagon.")
elif sides == 10:
    print("It's a decagon.")
else:
    print("The number is outside of range.")


"""
Author's solution:

nsides = int(input("Enter the number of sides: "))
name = ""

if nsides == 3:
    name = "triangle"
elif nsides == 4:
    name = "quadrilateral"
elif nsides == 5:
    name = "pentagon"
elif nsides == 6:
    name = "hexagon"
elif nsides == 7:
    name = "heptagon"
elif nsides == 8:
    name = "octagon"
elif nsides == 9:
    name = "nonagon"
elif nsides == 10:
    name = "decagon"

if name == "":
    print("That number of sides is not supported by this program.")
else:
    print("That’s a", name)
"""
