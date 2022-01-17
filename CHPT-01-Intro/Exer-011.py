"""
Exercise 11: Fuel Efficiency

In the United States, fuel efficiency for vehicles is normally expressed in miles-per-
gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
"""

# Plug the number of miles per gallon into the formula.
# Divide the MPG into 235.21. The result will be the converted number of liters per 100 km.

mpg = float(input("Enter MPG: "))
print("L/100 km is {}".format((235.21 / mpg)))

"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

MPG = float(input("How many Miles Per Gallon (MPG): "))

litresPer100 = 235.215 / MPG
print("The L/100km is {}L".format(litresPer100))
"""

