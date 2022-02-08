"""
Exercise 28: Body Mass Index

Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should
use one of the following two formulas to compute the BMI before displaying it. If
you read the height in inches and the weight in pounds then body mass index is
computed using the following formula:

BMI = weight / (height * height) * 703

If you read the height in meters and the weight in kilograms then body mass index
is computed using this slightly simpler formula:

BMI = weight / height * height
"""
# Solution by Aldo Telese
# https://github.com/aldotele

mt = float(input("insert height in meters: "))
kg = float(input("insert weight in kilograms: "))

inches = mt * 39.37
pounds = kg * 2.20462

BMI = kg / (mt * mt)
print("A height of %.2f meters (or %.2f inches) and a weight of %.2f kg (or %.2f lbs) lead to a BMI of %.2f." \
      % (mt, inches, kg, pounds, BMI))


"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

height = float(input("Please enter a height in metres: "))
weight = float(input("Please enter a weight in kilograms: "))

BMI = (weight)  / (height * height)

print("The BMI of this person's height and weight is {}.".format(BMI))
"""
