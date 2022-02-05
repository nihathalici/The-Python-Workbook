"""
Exercise 25: Units of Time (Again)

In this exercise you will reverse the process described in Exercise 24. Develop a
program that begins by reading a number of seconds from the user. Then your program
should display the equivalent amount of time in the form D:HH:MM:SS, where D,
HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours,
minutes and seconds should all be formatted so that they occupy exactly two digits.
Use your research skills determine what additional character needs to be included in
the format specifier so that leading zeros are used instead of leading spaces when a
number is formatted to a particular width.
"""

SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

seconds = int(input("Enter a number of seconds: "))

days = seconds / SECONDS_PER_DAY
seconds = seconds % SECONDS_PER_DAY

hours = seconds / SECONDS_PER_HOUR
seconds = seconds % SECONDS_PER_HOUR

minutes = seconds / SECONDS_PER_MINUTE
seconds = seconds % SECONDS_PER_MINUTE

print("The equivalent duration is %d:%02d:%02d:%02d." % (days, hours, minutes, seconds))

"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

totalSeconds = int(input("Please enter a number of seconds: "))

days = int(totalSeconds / 60 / 60 / 24)
totalSeconds -= days * 60 * 60 * 24

hours = int(totalSeconds / 60 / 60)
totalSeconds -= hours * 60 * 60

minutes = int(totalSeconds / 60)
totalSeconds -= minutes * 60

seconds = totalSeconds

print("In the form D:H:M:S : {}:{}:{}:{}".format(days, hours, minutes, seconds))
"""
