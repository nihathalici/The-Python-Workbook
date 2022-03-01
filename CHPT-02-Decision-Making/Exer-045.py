"""
Exercise 45: Date to Holiday Name

Canada has three national holidays which fall on the same dates each year.

-----------------------------------
Holiday               Date
-----------------------------------
New Year’s Day        January 1
Canada Day            July 1
Christmas Day         December 25
-----------------------------------

Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday.

"""
# Solution by Aldo Telese
# https://github.com/aldotele


month = input("Enter month: ")
day = input("Enter day: ")

if month.lower() == "january" or month.lower() == "jan" or month == "1" or month == "01":
    if day == "1" or day == "01":
        holiday = "New Year's Day"
elif month.lower() == "july" or month.lower() == "jul" or month == "7" or month == "07":
    if day == "1" or day == "01":
        holiday = "Canada Day"
elif month.lower() == "december" or month.lower() == "dec" or month == "12":
    if day == "25":
        holiday = "Christmas Day"
else:
    holiday = "The entered date doesn't correspond to any holiday."


"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26
# 4th month as july corrected 

month = int(input("Please enter in a month with a numerical value (1-12): "))
date = int(input("Please enter in a date: "))

holiday = ""

if month == 1 or month == 7 or month == 12:
    if month == 1 and date == 1:
        holiday = "New Year's Day"
    elif month == 7 and date == 1:
        holiday = "Canada Day"
    elif month == 12 and day == 25:
        holiday = "Christmas Day"

if holiday == "":
    print("That is not a holiday that falls on the same date each year.")
else:
    print("The date is {}.".format(holiday))
    
"""
