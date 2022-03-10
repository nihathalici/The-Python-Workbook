"""
Exercise 54: Assessing Employees

At a particular company, employees are rated at the end of each year. The rating scale
begins at 0.0, with higher values indicating better performance and resulting in larger
raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
with each rating is shown in the following table. The amount of an employee’s raise
is $2,400.00 multiplied by their rating.

---------------------------------------
Rating        Meaning
---------------------------------------

0.0           Unacceptable Performance
0.4           Acceptable Performance
0.6 or more   Meritorious Performance
---------------------------------------

Write a program that reads a rating from the user and indicates whether the per-
formance for that rating is unacceptable, acceptable or meritorious. The amount
of the employee’s raise should also be reported. Your program should display an
appropriate error message if an invalid rating is entered.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26


value = float(input("Enter a value for the employee's performance: "))

descriptor = ""

if value == 0.0:
        descriptor = "Unacceptable performance"
elif value == 0.4:
        descriptor = "Acceptable performance"
elif value >= 0.6:
        descriptor = "Meritorious performance"

if descriptor != "":
        print("According to this scale, the employee has shown '{}'.".format(descriptor))
else:
        print("Invalid value entered. (Value is either 0.0, 0.4, or greater than 0.6)")

