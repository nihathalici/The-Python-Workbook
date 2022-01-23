"""
Exercise 17: Heat Capacity

The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy, q, required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:

Write a program that reads the mass of some water and the temperature change from
the user. Your program should display the total amount of energy that must be added
or removed to achieve the desired temperature change.

Hint: The specific heat capacity of water is 4.186 g ◦ J C . Because water has a
density of 1.0 grams per milliliter, you can use grams and milliliters inter-
changeably in this exercise.

Extend your program so that it also computes the cost of heating the water. Elec-
tricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt hour. Use
your program to compute the cost of boiling the water needed for a cup of coffee.

Hint: You will need to look up the factor for converting between Joules and
kilowatt hours to complete the last part of this exercise.
"""
# Author's solution:

WATER_HEAT_CAPACITY = 4.186
ELECTRICITY_PRICE = 8.9
J_TO_KWH = 2.777e-7

volume = float(input("Amount of water in milliliters: "))
d_temp = float(input("Temperature increase (degrees Celsius):"))

# Compute the energy in Joules
q = volume * d_temp * WATER_HEAT_CAPACITY

print("That will require %d Joules of energy." % q)

# Compute the cost
kwh = q * J_TO_KWH
cost = kwh * ELECTRICITY_PRICE

print("That much energy will cost %.2f cents." % cost)
