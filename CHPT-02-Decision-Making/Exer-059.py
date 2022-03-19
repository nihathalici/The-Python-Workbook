"""
Exercise 59: Next Day

Write a program that reads a date from the user and computes its immediate successor.
For example, if the user enters values that represent 2019-11-18 then your program
should display a message indicating that the day immediately after 2019-11-18 is
2019-11-19. If the user enters values that represent 2019-11-30 then the program
should indicate that the next day is 2019-12-01. If the user enters values that represent
2019-12-31 then the program should indicate that the next day is 2020-01-01. The
date will be entered in numeric form with three separate input statements; one for
the year, one for the month, and one for the day. Ensure that your program works
correctly for leap years.
"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))

nextDayYear = year
nextDayMonth = month
nextDayDate = day

if month != 12:
    nextDayYear = year
else:
    if day != 31:
        nextDayYear = year
    else:
        nextDayYear = year + 1

# Sep, April, June, November only have 30 days

if month != 9 and month != 4 and month != 6 and month != 6 and month != 11:
    if day != 31:
        nextDayMonth = month
        nextDayDate = day + 1
    else:
        if month != 12:
            nextDayMonth = month + 1
        else:
            nextDayMonth = 1
        nextDayDate = 1
else:
    if day != 30:
        nextDayMonth = month
        nextDayDate = day + 1
    else:
        if month != 12:
            nextDayMonth = month + 1
        else:
            nextDayMonth = 1
        nextDayDate = 1
        
if month == 2:
    isLeapYear = False

    if year % 400 == 0:
        isLeapYear = True
    elif year % 100 == 0 and not year % 400 == 0:
        isLeapYear = False
    elif year % 4 == 0 and not year % 100 == 0 and not year % 400 == 0:
        isLeapYear = True

    if day == 28:
        if isLeapYear:
            nextDayMonth = month
            nextDayDate = day + 1
        else:
            nextDayMonth = month + 1
            nextDayDate = 1
    else:
        nextDayMonth = month
        nextDayDate = day + 1
            

print("The next day is {}-{}-{}.".format(nextDayYear, nextDayMonth, nextDayDate))    
