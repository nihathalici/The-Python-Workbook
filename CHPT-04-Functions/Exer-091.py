"""
Exercise 91: Gregorian Date to Ordinal Date

An ordinal date consists of a year and a day within it, both of which are integers. The
year can be any year in the Gregorian calendar while the day within the year ranges
from one, which represents January 1, through to 365 (or 366 if the year is a leap
year) which represents December 31. Ordinal dates are convenient when computing
differences between dates that are a specific number of days (rather than months). For
example, ordinal dates can be used to easily determine whether a customer is within
a 90 day return period, the sell-by date for a food-product based on its production
date, and the due date for a baby.
Write a function named ordinalDate that takes three integers as parameters.
These parameters will be a day, month and year respectively. The function should
return the day within the year for that date as its only result. Create a main program
that reads a day, month and year from the user and displays the day within the year for
that date. Your main program should only run when your file has not been imported
into another program.
"""

# Solution by Aldo Telese
# https://github.com/aldotele
# Modified by nihathalici

# first thing to do is understanding if the year has 365 or 366 days
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# second thing is to get the total days within a month of a specific year
def days_in_month(month, year):
    days = 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    elif month == 2:
        if is_leap(year):
            days = 29
        else:
            days = 28
    elif month < 1 or month > 12:
        raise ValueError('Month must be between 1 and 12.')
    return days

def greg_to_ord_date(day, month, year):
    ordinal = 0
    for m in range(1, month):
        ordinal += days_in_month(m, year)
    
    if day > days_in_month(month, year) or day < 1:
        raise ValueError('The entered day is not valid: it is outside that month\'s range of days')
    else:
        ordinal += day
    
    return ordinal

def main():
    day = int(input('Enter day of the month as integer: '))
    month = int(input('Enter month of the year as integer: '))
    year = int(input('Enter year: '))

    print('It was {}. day of {}.'.format(greg_to_ord_date(day, month, year), year))

if __name__ == '__main__':
    main()