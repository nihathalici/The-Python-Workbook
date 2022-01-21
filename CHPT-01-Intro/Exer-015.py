"""
Exercise 15: Distance Units

In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.
"""

IN_PER_FT = 12
YRD_PER_FT = 0.33
MLS_PER_FT = 0.0001893939 

feet = int(input(" Number of feet: "))

print("Distance in inches: {}, yards: {}, miles: {}".format( (feet * IN_PER_FT), round((feet * YRD_PER_FT),2), round((feet * MLS_PER_FT),2)  ))

"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

feet = int(input("Please enter a distance in feet: "))

miles = feet * 0.000189394
yards = feet * 0.333333333
inches = feet * 12

print("In miles: {}".format(miles))
print("In yards: {}".format(yards))
print("In inches: {}".format(inches))
"""
