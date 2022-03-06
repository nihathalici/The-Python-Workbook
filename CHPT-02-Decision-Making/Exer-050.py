"""
Exercise 50: Richter Scale

The following table contains earthquake magnitude ranges on the Richter scale and
their descriptors:

------------------------------------
Magnitude                Descriptor
------------------------------------

Less than 2.0            Micro
2.0 to less than 3.0     Very Minor
3.0 to less than 4.0     Minor
4.0 to less than 5.0     Light
5.0 to less than 6.0     Moderate
6.0 to less than 7.0     Strong
7.0 to less than 8.0     Major
8.0 to less than 10.0    Great
10.0 or more             Meteoric
------------------------------------

Write a program that reads a magnitude from the user and displays the appropriate
descriptor as part of a meaningful message. For example, if the user enters 5.5 then
your program should indicate that a magnitude 5.5 earthquake is considered to be a
moderate earthquake.
"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

magnitude = float(input("Enter an earthquake magnitude: "))

if magnitude < 2.0:
	descriptor = "Micro"
elif magnitude >= 2.0 and magnitude < 3.0:
	descriptor = "Very minor"
elif magnitude >= 3.0 and magnitude < 4.0:
	descriptor = "Minor"
elif magnitude >= 4.0 and magnitude < 5.0:
	descriptor = "Light"
elif magnitude >= 5.0 and magnitude < 6.0:
	descriptor = "Moderate"
elif magnitude >= 6.0 and magnitude < 7.0:
	descriptor = "Strong"
elif magnitude >= 7.0 and magnitude < 8.0:
	descriptor = "Major"
elif magnitude >= 8.0 and magnitude < 10.0:
	descriptor = "Great"
else:
	descriptor = "Meteoric"
	
print("This earthquake is classified as '{}'. ".format(descriptor))



"""
# Alternative Solution by
# https://github.com/aldotele

magnitude = float(input("enter magnitude: "))

if magnitude >= 10:
    level = "meteoric"
elif magnitude >= 8:
    level = "great"
elif magnitude >= 7:
    level = "major"
elif magnitude >= 6:
    level = "strong"
elif magnitude >= 5:
    level = "moderate"
elif magnitude >= 4:
    level = "light"
elif magnitude >= 3:
    level = "minor"
elif magnitude >= 2:
    level = "very minor"
else:
    level = "micro"

print("an earthquake with magnitude {} is a {} one".format(magnitude, level))
"""
