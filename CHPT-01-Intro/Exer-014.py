"""
Exercise 14: Height Units

Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.

Hint: One foot is 12 inches. One inch is 2.54 centimeters.
"""
# Author's solution:

IN_PER_FT = 12
CM_PER_IN = 2.54

print("Enter your height:")
feet = int(input(" Number of feet: "))
inches = int(input(" Number of inches: "))

cm = (feet * IN_PER_FT + inches) * CM_PER_IN

print("Your height in centimeters is:", cm)
