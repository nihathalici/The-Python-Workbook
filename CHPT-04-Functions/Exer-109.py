"""
Exercise 109: Magic Dates

A magic date is a date where the day multiplied by the month is equal to the two digit
year. For example, June 10, 1960 is a magic date because June is the sixth month, and
6 times 10 is 60, which is equal to the two digit year. Write a function that determines
whether or not a date is a magic date. Use your function to create a main program
that finds and displays all of the magic dates in the 20th century. You will probably
find your solution to Exercise 106 helpful when completing this exercise.
"""
# Author's solution:
##
# Determine all of the magic dates in the 1900s.
#
from days_in_month import daysInMonth

## Determine whether or not a date is ‘‘magic’’
# @param day the day portion of the date
# @param month the month portion of the date
# @param year the year portion of the date
# @return True if the date is magic, False otherwise
def isMagicDate(day, month, year):
    if day * month == year % 100:
        return True
    return False

# Find and display all of the magic dates in the 1900s
def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, daysInMonth(month, year) + 1):
                if isMagicDate(day, month, year):
                    print("%02d/%02d/%04d is a magic date." % (day, month, year))

main()