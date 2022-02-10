"""
Exercise 30: Celsius to Fahrenheit and Kelvin

Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the Internet.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

T_celsius = float(input("Enter temperature in degree celsius: "))

T_fahrenheit = T_celsius * (9/5) + 32
T_kelvin = T_celsius + 273.15

print("%.2f degree celsius equal %.2f degree fahrenheit and %.2f degree kelvin" % (T_celsius, T_fahrenheit, T_kelvin))


"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

celsius = float(input("Please enter a temperature in Celsius: "))

fahrenheit = celsius * (9/5) + 32
kelvin = celsius + 273.15

print("In Fahrenheit: {}".format(fahrenheit))
print("In Kelvin: {}".format(kelvin))
"""

