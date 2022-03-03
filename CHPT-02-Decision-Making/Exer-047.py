"""
Exercise 47: Season from Month and Day

The year is divided into four seasons: spring, summer, fall (or autumn) and winter.
While the exact dates that the seasons change vary a little bit from year to year
because of the way that the calendar is constructed, we will use the following dates
for this exercise:

--------------------------
Season      First Day
--------------------------
Spring      March 20
Summer      June 21
Fall        September 22
Winter      December 21
--------------------------

Create a program that reads a month and day from the user. The user will
enter the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date that
was entered.

This solution to the season identification problem uses several elif parts so that the condi-
tions remain as simple as possible. Another way of approaching this problem is to minimize
the number of elif parts by making the conditions more complex.
"""

# Author's solution
# Read the date from the user
month = input("Enter the name of the month: ")
day = int(input("Enter the day number: "))

# Determine the season
if month == "January" or month == "February":
    season = "Winter"
elif month == "March":
    if day < 20:
        season = "Winter"
    else:
        season = "Spring"
elif month == "April" or month == "May":
    season = "Spring"
elif month == "June":
    if day < 21:
        season = "Spring"
    else:
        season = "Summer"
elif month == "July" or month == "August":
    season = "Summer"
elif month == "September":
    if day < 22:
        season = "Summer"
    else:
        season = "Fall"
elif month == "October" or month == "November":
    season = "Fall"
elif month == "December":
    if day < 21:
        season = "Fall"
    else:
        season = "Winter"

# Display the result
print(month, day, "is in", season)
    

"""
# Alternative Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

month = input("Please enter the name of a month: ").lower()
day = int(input("Please enter a day from that month: "))

season = ""

spring, summer, fall, winter = False

if month == "march" or month == "april" or month == "may" or month == "june":
	if month == "march" and day >= 20:
		spring = True
		
	elif month == "april" or month == "may":
		spring  = True
		
	elif month == "june" and day < 21:
		spring = True
		
if month == "june" or month == "july" or month == "august" or month == "septemper":
	if month  == "june" and day >= 21:
		summer = True
		
	elif month == "july" or month == "august":
		summer = True
		
	elif month == "semptember" and day < 22:
		summber = True
		

if month == "septemper" or month == "october" or month == "november" or month == "december":
	if month == "september" and day >= 22:
		fall = True
		
	elif month == "october" or month == "november":
		fall = True
		
	elif month == "december" and day < 21:
		fall = True
		
if month == "december" or month == "january" or month == "february" or month == "march":
	if month == "december" and day >= 20:
		winter = True
		
	elif month == "january" or month == "february":
		winter = True
		
	elif month == "march" and day < 20:
		winter = True
		
if spring:
	print("That date falls in spring.")
elif summer:
	print("That date falls in summer.")
elif fall:
	print("That date falls in fall.")
elif winter:
	print("That date falls in winter.")
"""


"""
# Alternative Solution by
# https://github.com/aldotele

# exercise 47: Season From Month and Day

month = input("enter month: ")
day = int(input("enter day: "))

month = month.lower()
season = ''

if month == "march":
    if day < 20:
        season = "winter"
    elif day <= 31:
        season = "spring"
if month == "june":
    if day < 21:
        season = "spring"
    elif day <= 30:
        season = "summer"
if month == "september":
    if day < 22:
        season = "summer"
    elif day <= 30:
        season = "fall"
if month == "december":
    if day < 21:
        season = "fall"
    elif day <= 31:
        season = "winter"
elif (month == "april" and day <= 30) or (month == "may" and day <= 31):
    season = "spring"
elif (month == "july" and day <= 31) or (month == "august" and day <= 31):
    season = "summer"
elif (month == "october" and day <= 31) or (month == "november" and day <= 30):
    season = "fall"
elif (month == "january" and day <= 31) or (month == "february" and day <= 29):
    season = "winter"
else:
    print('not valid. Check month spelling and make sure number of days is within range.')
    quit()

print('{} {} is {}'.format(month, day, season))

# a way to minimize the if statement is making them more complex
"""
