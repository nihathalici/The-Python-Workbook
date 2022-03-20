"""
Exercise 60: What Day of the Week Is January 1?

The following formula can be used to determine the day of the week for January 1
in a given year:

day_of_the_week = (year + floor((year − 1) / 4) − floor((year − 1) / 100) +
floor((year − 1) / 400)) % 7

The result calculated by this formula is an integer that represents the day of the
week. Sunday is represented by 0. The remaining days of the week following in
sequence through to Saturday, which is represented by 6.

Use the formula above to write a program that reads a year from the user and
reports the day of the week for January 1 of that year. The output from your program
should include the full name of the day of the week, not just the integer returned by
the formula.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

import datetime

year = int(input('Enter a year and you will get its January 1 day: '))

# the following formula finds the day of the week (as integer 0-6) of January 1st
weekday = (year + ((year - 1) // 4) - ((year - 1) // 100) + ((year - 1) // 400)) % 7

if weekday == 0:
    res = 'Sunday'
elif weekday == 1:
    res = 'Monday'
elif weekday == 2:
    res = 'Tuesday'
elif weekday == 3:
    res = 'Wednesday'
elif weekday == 4:
    res = 'Thursday'
elif weekday == 5:
    res = 'Friday'
elif weekday == 6:
    res = 'Saturday'

# extracting today's year in order to differentiate the tense of the output string
now = datetime.datetime.now()
current_year = now.year

if year > current_year:
    print('January 1st of %d will be a %s' % (year, res))
else:
    print('January 1st of %d was a %s' % (year, res))




