"""
Exercise 106: Days in a Month

Write a function that determines how many days there are in a particular month. Your
function will take two parameters: The month as an integer between 1 and 12, and
the year as a four digit integer. Ensure that your function reports the correct number
of days in February for leap years. Include a main program that reads a month and
year from the user and displays the number of days in that month. You may find your
solution to Exercise 58 helpful when solving this problem.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def daysInMonth(month, year):
    if month < 1 or month > 12 or len(str(year)) != 4:  # Error check
        return "The input {} is not valid.".format(year)
    
    if month == 11 or month == 4 \
        or month == 6 or month == 9:
        num_of_days = 30
    elif month == 2:
        # Condition depends on the return of the function
        if isLeap(year):
            num_of_days = 29
        else:
            num_of_days = 28
    
    else:
        num_of_days = 31
    return num_of_days


if __name__ == "__main__":
    month = int(input("Enter a month as an integer: "))
    year = int(input("Enter a year: "))
    print(daysInMonth(month, year))
