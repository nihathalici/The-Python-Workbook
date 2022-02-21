"""
Exercise 39: Month Name to Number of Days

The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
"""

month = input("Enter month name: ").lower()

if month == "january":
    print("{} has 31 days".format(month))
elif month == "february":
    print("{} has 28 or 29 days".format(month))
elif month == "march":
    print("{} has 31 days".format(month))
elif month == "april":
    print("{} has 30 days".format(month))
elif month == "may":
    print("{} has 31 days".format(month))
elif month == "june":
    print("{} has 30 days".format(month))
elif month == "july":
    print("{} has 31 days".format(month))
elif month == "august":
    print("{} has 31 days".format(month))
elif month == "september":
    print("{} has 30 days".format(month))
elif month == "october":
    print("{} has 31 days".format(month))
elif month == "november":
    print("{} has 30 days".format(month))
elif month == "december":
    print("{} has 31 days".format(month))


"""
Author's solution:

month = input("Enter the name of a month: ")

days = 31

if month == "April" or month == "June" or \
   month == "September" or month == "November":
    days = 30
elif month == "February":
    days = "28 or 29"

print(month, "has", days, "days in it.")
"""


"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

month = input("Please enter the name of a month: ").lower()

if month == "september" or month == "april" or month == "june" or month == "november":
    print("There are 30 days in this month.")
elif month == "february":
    print("There are 28 or 29 days in this month.")
else:
    print("There are 31 days in this month.")
"""
