"""
Exercise 48: Birth Date to Astrological Sign

The horoscopes commonly reported in newspapers use the position of the sun at the
time of one’s birth to try and predict the future. This system of astrology divides the
year into twelve zodiac signs, as outline in the table below:

------------------------------------------
Zodiac Sign    Date Range
------------------------------------------

Capricorn      December 22 to January 19
Aquarius       January 20 to February 18
Pisces         February 19 to March 20
Aries          March 21 to April 19
Taurus         April 20 to May 20
Gemini         May 21 to June 20
Cancer         June 21 to July 22
Leo            July 23 to August 22
Virgo          August 23 to September 22
Libra          September 23 to October 22
Scorpio        October 23 to November 21
Sagittarius    November 22 to December 21
------------------------------------------

Write a program that asks the user to enter his or her month and day of birth. Then
your program should report the user’s zodiac sign as part of an appropriate output
message.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

month = int(input("Please enter your month of birth as a number: "))
date = int(input("Please enter your day of birth as a number: "))

assert month <= 12 and month >= 1
assert date <= 31 and date >= 1

zodiac = ""

if (month == 12 and date >= 22) or (month == 1 and date <= 19):
    zodiac = "Capricorn"

elif (month == 1 and date >= 20) or (month == 2 and date <= 18):
    zodiac = "Aquarius"

elif (month == 2 and date >= 21) or (month == 3 and date <= 19):
    zodiac = "Pisces"

elif (month == 3 and date >= 21) or (month == 4 and date <= 19):
    zodiac = "Aries"

elif (month == 4 and date >= 20) or (month == 5 and date <= 20):
    zodiac = "Taurus"

elif (month == 5 and date >= 21) or (month == 6 and date <= 20):
    zodiac = "Gemini"
	
elif (month == 6 and date >= 21) or (month == 7 and date <= 22):
    zodiac = "Cancer"
	
elif (month == 7 and date <= 23) or (month == 8 and date <= 22):
    zodiac = "Leo"
	
elif (month == 8 and date >= 23) or (month == 9 and date <= 22):
    zodiac = "Virgo"
	
elif (month == 9 and date >= 23) or (month == 10 and date <= 22):
    zodiac = "Libra"
	
elif (month == 10 and date <= 23) or (month == 11 and date <= 21):
    zodiac = "Scorpio"
	
elif (month == 11 and date <= 22) or (month == 12 and date <= 21):
    zodiac = "Sagittarius"
	
print("You are a thrifty {}!".format(zodiac))


"""
# Alternative Solution by
# https://github.com/aldotele

month = input('enter a month: ').lower()
day = int(input('enter a day: '))

if month == 'january':
    if day <= 19:
        sign = 'capricorn'
    else:
        sign = 'aquarius'
elif month == 'february':
    if day <= 18:
        sign = 'aquarius'
    else:
        sign = 'pisces'
elif month == 'march':
    if day <= 20:
        sign = 'pisces'
    else:
        sign = 'aries'
elif month == 'april':
    if day <= 19:
        sign = 'aries'
    else:
        sign = 'taurus'
elif month == 'may':
    if day <= 20:
        sign = 'taurus'
    else:
        sign = 'gemini'
elif month == 'june':
    if day <= 20:
        sign = 'gemini'
    else:
        sign = 'cancer'
elif month == 'july':
    if day <= 22:
        sign = 'cancer'
    else:
        sign = 'leo'
elif month == 'august':
    if day <= 22:
        sign = 'leo'
    else:
        sign = 'virgo'
elif month == 'september':
    if day <= 23:
        sign = 'virgo'
    else:
        sign = 'libra'
elif month == 'october':
    if day <= 22:
        sign = 'libra'
    else:
        sign = 'scorpio'
elif month == 'november':
    if day <= 21:
        sign = 'scorpio'
    else:
        sign = 'sagittarius'
elif month == 'december':
    if day <= 21:
        sign = 'sagittarius'
    else:
        sign = 'capricorn'
else:
    print('error: check month spelling')
    exit()

print('zodiacal sign: {}'.format(sign))
"""

