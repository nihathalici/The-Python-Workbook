"""
Exercise 27: When is Easter?

Easter is celebrated on the Sunday immediately after the first full moon following the
spring equinox. Because its date includes a lunar component, Easter does not have
a fixed date in the Gregorian calendar. Instead, it can occur on any date between
March 22 and April 25.
Write a program that implements the Anonymous Gregorian Computus algorithm
to compute the date of Easter. Your program should read the year from the user and
then display a appropriate message that includes the date of Easter in that year.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

import datetime

year = int(input('enter a year and you will get its Easter date: '))

a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = (a + 11 * h + 22 * l) // 451

month = (h + l - 7 * m + 114) // 31
day = 1 + (h + l - 7 * m + 114) % 31

# extracting today's year in order to differentiate the tense of the output string
now = datetime.datetime.now()
current_year = now.year

if year > current_year:
    print('in %d, Easter will be on %.2d-%d'%(year, month, day))
else:
    print('in %d, Easter was on %.2d-%d'%(year, month, day))
