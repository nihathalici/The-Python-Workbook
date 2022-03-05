"""
Exercise 49: Chinese Zodiac

The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
shown in the table below. The pattern repeats from there, with 2012 being another
year of the dragon, and 1999 being another year of the hare.

--------------
Year    Animal
--------------
2000    Dragon  
2001    Snake
2002    Horse
2003    Sheep
2004    Monkey
2005    Rooster
2006    Dog
2007    Pig
2008    Rat
2009    Ox
2010    Tiger
2011    Hare
--------------

Write a program that reads a year from the user and displays the animal associated
with that year. Your program should work correctly for any year greater than or equal
to zero, not just the ones listed in the table.
"""
# Author's solution
# Read a year from the user
year = int(input("Enter a year: "))

# Determine the animal associated with that year
if year % 12 == 8:
    animal = "Dragon"
if year % 12 == 9:
    animal = "Snake"
if year % 12 == 10:
    animal = "Horse"
if year % 12 == 11:
    animal = "Sheep"
if year % 12 == 0:
    animal = "Monkey"
if year % 12 == 1:
    animal = "Rooster"
if year % 12 == 2:
    animal = "Dog"
if year % 12 == 3:
    animal = "Pig"
if year % 12 == 4:
    animal = "Rat"
if year % 12 == 5:
    animal = "Ox"
if year % 12 == 6:
    animal = "Tiger"
if year % 12 == 7:
    animal = "Hare"

# Report the result
print("%d is the year of the %s." % (year, animal))

    
